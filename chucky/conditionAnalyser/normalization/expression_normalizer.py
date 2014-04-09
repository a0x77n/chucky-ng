import logging

NUM = '$NUM'
CMP = '$CMP'
RET = '$RET'
ARG = '$ARG'

class ExpressionNormalizer():

    def __init__(self, argset, retset):
        self.argset = map(lambda x : x.code, argset)
        self.retset = map(lambda x : x.code, retset)
        self.logger = logging.getLogger('chucky')

    def _handle_identifier(self, node):
        if self.retset and node.code in self.retset:
            self.logger.debug('[IDENTIFIER] $RET')
            return [RET]
        elif self.argset and node.code in self.argset:
            self.logger.debug('[IDENTIFIER] $ARG')
            return [ARG]
        else:
            self.logger.debug('[IDENTIFIER] {}'.format(node.code))
            return [node.code]

    def _handle_argument(self, node):
        child = node.children()[0]
        child_subtree = self.normalize_expression(child)
        argument = child_subtree[0]
        self.logger.debug('[ARGUMENT] {}'.format(argument))
        return [argument]

    def _handle_argument_list(self, node):
        arguments = node.children()
        subtrees = []
        for argument in arguments:
            subtrees.append(self._handle_argument(argument))
        subtree_roots = map(lambda x : x[0], subtrees)
        root = ', '.join(subtree_roots)
        self.logger.debug('[ARGUMENTLIST] {}'.format(root))
        return [root]

    def _handle_callee(self, node):
        self.logger.debug('[CALLEE] {}'.format(node.code))
        return [node.code]

    def _handle_cast_expression(self, node):
        left, right = node.children()
        left_subtree = self.normalize_expression(left)
        right_subtree = self.normalize_expression(right)
        left_root = left_subtree[0]
        right_root = right_subtree[0]
        root = '({}) ( {} )'.format(left_root, right_root)
        self.logger.debug('[CAST_EXPRESSION] {}'.format(root))
        return [root] + left_subtree + right_subtree

    def _handle_unary_expression(self, node):
        if node.code.startswith('sizeof'):
            self.logger.debug('[UNARY_EXPRESSION] {}'.format(node.code))
            return [node.code]
        elif node.code.startswith('--') or node.code.startswith('++'):
            left, right = node.children()
            left_subtree = self.normalize_expression(left)
            right_subtree = self.normalize_expression(right)
            left_root = left_subtree[0]
            right_root = right_subtree[0]
            root = '{} {}'.format(left_root, right_root)
            self.logger.debug('[CAST_EXPRESSION] {}'.format(root))
            return [root] + left_subtree + right_subtree
        else:
            self.logger.warning('Unknown unary expression %s', node.code)
            return [node.code]

    def _handle_primary_expression(self, node):
        if node.code.startswith('\'') or node.code.startswith('\"'):
            self.logger.debug('[PRIMARY_EXPRESSION] {}'.format(node.code))
            return [node.code]
        else:
            self.logger.debug('[PRIMARY_EXPRESSION] $NUM ({})'.format(node.code))
            return ['$NUM']
    
    def _handle_inc_dec_operation(self, node):
        left, right = node.children()
        left_subtree = self.normalize_expression(left)
        right_subtree = self.normalize_expression(right)
        left_root = left_subtree[0]
        right_root = right_subtree[0]
        root = '{} {}'.format(left_root, right_root)
        self.logger.debug('[INC_DEC_OPERATION] {}'.format(node.code))
        return [root] + left_subtree # + right_subtree

    def _handle_binary_operation(self, node, operator):
        left, right = node.children()
        left_subtree = self.normalize_expression(left)
        right_subtree = self.normalize_expression(right)
        left_root = left_subtree[0]
        right_root = right_subtree[0]
        root = '( {} {} {} )'.format(left_root, operator, right_root)
        self.logger.debug('[BINARY_OPERATION] {}'.format(root))
        return [root] + left_subtree + right_subtree

    def _handle_arithmetic_expression(self, node, operator):
        left, right = node.children()
        left_subtree = self.normalize_expression(left)
        right_subtree = self.normalize_expression(right)
        left_root = left_subtree[0]
        right_root = right_subtree[0]
        if left_root == NUM and right_root == NUM:
            root = NUM
        else:
            root = '( {} {} {} )'.format(left_root, operator, right_root)
        self.logger.debug('[ARITHMETIC_EXPRESSION] {}'.format(root))
        return [root] + left_subtree + right_subtree

    def _handle_assignment_expression(self, node):
        left, right = node.children()
        left_subtree = self.normalize_expression(left)
        right_subtree = self.normalize_expression(right)
        left_root = left_subtree[0]
        right_root = right_subtree[0]
        root = '{} = {}'.format(left_root, right_root)
        self.logger.debug('[ASSIGNMENT_EXPRESSION] {}'.format(root))
        return [root] + left_subtree + right_subtree

    def _handle_array_indexing(self, node):
        left, right = node.children()
        left_subtree = self.normalize_expression(left)
        right_subtree = self.normalize_expression(right)
        left_root = left_subtree[0]
        right_root = right_subtree[0]
        root = '{} [ {} ]'.format(left_root, right_root)
        self.logger.debug('[ARRAY_INDEXING] {}'.format(root))
        return [root] + left_subtree + right_subtree

    def _handle_call_expression(self, node):
        left, right = node.children()
        callee_tree = self._handle_callee(left)
        argument_list_tree = self._handle_argument_list(right)
        callee = callee_tree[0]
        argument_list = argument_list_tree[0]
        call_expression = '{} ( {} )'.format(callee, argument_list)
        self.logger.debug('[CALL_EXPRESSION] {}'.format(call_expression))
        return [call_expression, callee]

    def _handle_conditional_expression(self, node):
        left, middle, right = node.children()
        left_subtree = self.normalize_expression(left)
        middle_subtree = self.normalize_expression(middle)
        right_subtree = self.normalize_expression(right)
        left_root = left_subtree[0]
        middle_root = middle_subtree[0]
        right_root = right_subtree[0]
        root = '{} ? {} : {}'.format(left_root, middle_root, right_root)
        self.logger.debug('[CONDITIONAL_EXPRESSION] {}'.format(root))
        return [root] + left_subtree + middle_subtree + right_subtree

    def normalize_expression(self, node):
        node_type = node.node_type

        if node_type == 'Identifier':
            return self._handle_identifier(node)
        elif node_type == 'Argument':
            return self._handle_argument(node)
        elif node_type == 'ArgumentList':
            return self._handle_argument_list(node)
        elif node_type == 'Callee':
            return self._handle_callee(node)
        elif node_type == 'CastTarget':
            return [node.code]
        elif node_type == 'UnaryExpression':
            return self._handle_unary_expression(node)
        elif node_type == 'IncDecOp':
            return self._handle_inc_dec_operation(node)
        elif node_type == 'IncDec':
            return [node.code]
        elif node_type == 'PtrMemberAccess':
            return self._handle_identifier(node)
        elif node_type == 'MemberAccess':
            return self._handle_identifier(node)
        elif node_type == 'PrimaryExpression':
            return self._handle_primary_expression(node)
        elif node_type == 'AdditiveExpression':
            return self._handle_arithmetic_expression(node, node.operator)
        elif node_type == 'MultiplicativeExpression':
            return self._handle_arithmetic_expression(node, node.operator)
        elif node_type == 'AndExpression':
            return self._handle_binary_operation(node, node.operator)
        elif node_type == 'BitAndExpression':
            return self._handle_binary_operation(node, node.operator)
        elif node_type == 'InclusiveOrExpression':
            return self._handle_binary_operation(node, node.operator)
        elif node_type == 'ExclusiveOrExpression':
            return self._handle_binary_operation(node, node.operator)
        elif node_type == 'OrExpression':
            return self._handle_binary_operation(node, node.operator)
        elif node_type == 'ShiftExpression':
            return self._handle_binary_operation(node, node.operator)
        elif node_type == 'RelationalExpression': 
            return self._handle_binary_operation(node, CMP)
        elif node_type == 'EqualityExpression':
            return self._handle_binary_operation(node, CMP)
        elif node_type == 'AssignmentExpr':
            return self._handle_assignment_expression(node)
        elif node_type == 'ArrayIndexing':
            return self._handle_array_indexing(node)
        elif node_type == 'CallExpression':
            return self._handle_call_expression(node)
        elif node_type == 'CastExpression':
            return self._handle_cast_expression(node)
        elif node_type == 'ConditionalExpression':
            return self._handle_conditional_expression(node)
        else:
            self.logger.warning('Unknown type: %s', node_type)
            return [node.code]
