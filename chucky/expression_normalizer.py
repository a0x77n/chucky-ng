import logging

class ExpressionNormalizer():

    def __init__(self, argset, retset):
        self.argset = map(lambda x : x.code, argset)
        self.retset = map(lambda x : x.code, retset)
        self.logger = logging.getLogger('chucky')

    def _normalize_node(self, ast_node, join_function):
        expressions = []
        childs = ast_node.childs()
        for child in childs:
            for expr in self._normalize(child):
                yield expr
            expressions.append(expr)
        expr = '( ' + join_function(expressions) + ' )'
        self.logger.debug(expr)
        yield expr

    def _normalize_identifier_node(self, code):
        if self.argset and code in self.argset:
            self.logger.debug('$ARG (%s)', code)
            yield '$ARG'
        elif self.retset and code in self.retset:
            self.logger.debug('$RET (%s)', code)
            yield '$RET'
        else:
            self.logger.debug(code)
            yield code

    def _normalize_primary_expression_node(self, code):
        if code.startswith('\'') or code.startswith('\"'):
            self.logger.debug(code)
            yield code
        else:
            self.logger.debug('$NUM')
            yield '$NUM'

    def _normalize(self, node):
        #print 'Node "{}"\t"{}"\t"{}"\t"{}"'.format(node, node_type, operator,code)
        node_type = node.node_type
        operator = node.operator
        code = node.code

        if node_type == 'AdditiveExpression' \
                or node_type == 'MultiplicativeExpression':
            join_func = lambda x : '$NUM' if (x[0] == '$NUM' and x[1] == 'NUM') else ' '.join([x[0], operator, x[1]])
            for expr in self._normalize_node(node, join_func):
                yield expr
        elif node_type == 'AndExpression' \
                or node_type == 'BitAndExpression' \
                or node_type == 'InclusiveOrExpression' \
                or node_type == 'ExclusiveOrExpression' \
                or node_type == 'OrExpression':
            join_func = lambda x : ' '.join([x[0], operator, x[1]])
            for expr in self._normalize_node(node, join_func):
                yield expr
        elif node_type == 'RelationalExpression' \
                or node_type == 'EqualityExpression':
            join_func = lambda x : ' $CMP '.join(x)
            for expr in self._normalize_node(node, join_func):
                yield expr
        elif node_type == 'ShiftExpression':
            join_func = lambda x : ' '.join([x[0], operator, x[1]])
            for expr in self._normalize_node(node, join_func):
                yield expr
        elif node_type == 'ConditionalExpression':
            join_func = lambda x : ' '.join([x[0], '?', x[1], ':', x[2]])
            for expr in self._normalize_node(node, join_func):
                yield expr
        elif node_type == 'PtrMemberAccess':
            join_func = lambda x : ' -> '.join(x)
            for expr in self._normalize_node(node, join_func):
                yield expr
        elif node_type == 'MemberAccess':
            join_func = lambda x : ' . '.join(x)
            for expr in self._normalize_node(node, join_func):
                yield expr
        elif node_type == 'ArrayIndexing':
            join_func = lambda x : ' '.join([x[0], '[', x[1], ']'])
            for expr in self._normalize_node(node, join_func):
                yield expr
        elif node_type == 'CallExpression':
            join_func = lambda x : ' '.join([x[0], '(', x[1], ')'])
            for expr in self._normalize_node(node, join_func):
                yield expr
        elif node_type == 'ArgumentList':
            join_func = lambda x : ' , '.join(x)
            for expr in self._normalize_node(node, join_func):
                yield expr
        elif node_type == 'Argument':
            join_func = lambda x : x[0]
            for expr in self._normalize_node(node, join_func):
                yield expr
        elif node_type == 'AssignmentExpr':
            join_func = lambda x : ' {} '.format(operator).join(x)
            for expr in self._normalize_node(node, join_func):
                yield expr
        elif node_type == 'CastExpression':
            join_func = lambda x : ' '.join(['(', x[0], ')', x[1]])
            for expr in self._normalize_node(node, join_func):
                yield expr
        elif node_type == 'CastTarget':
            yield node.code
        elif node_type == 'UnaryExpression':
            if node.code.startswith('sizeof'):
                yield node.code
            elif code.startswith('--') or code.startswith('++'):
                join_func = lambda x : ' '.join(x)
                for expr in self._normalize_node(node, join_func):
                    yield expr
            else:
                self.logger.warning('Unknown type %s', node_type)
                yield code
        elif node_type == 'IncDecOp':
            join_func = lambda x : ' '.join(x)
            for expr in self._normalize_node(node, join_func):
                yield expr
        elif node_type == 'IncDec':
            yield code
        elif node_type == 'Identifier':
            for expr in self._normalize_identifier_node(node.code):
                yield expr
        elif node_type == 'PrimaryExpression':
            for expr in self._normalize_primary_expression_node(node.code):
                yield expr
        else:
            self.logger.warning('Unknown type %s', node_type)
            yield code

    def generate(self, root):
        self.logger.debug('Normalizing expresssion %s.', root)
        for expr in self._normalize(root):
            yield expr
