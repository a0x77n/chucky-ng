import py2neo.neo4j
import jutils

class Node(object):

    def __init__(self, node_id, properties = None):
        self.node_id = node_id
        self.properties = properties
        if not self.properties:
            self.load_properties()

    def __str__(self):
        return str(self.node_id)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.node_id == other.node_id

    def __ne__(self, other):
        return self.node_id != other.node_id

    def __hash__(self):
        return self.node_id

    def load_properties(self):
        node_selection = 'g.v("{}")'.format(self.node_id)
        _, node = jutils.raw_lookup(node_selection)[0]
        self.properties = node.get_properties()

    def get_property(self, label):
        if label in self.properties:
            return self.properties[label]
        else:
            return None

    @property
    def node_type(self):
        return self.get_property('type')

class ASTNode(Node):

    def __init__(self, node_id, properties = None):
        Node.__init__(self, node_id, properties)

    def __str__(self):
        return str(self.code)

    def parent(self):
        node_selection = 'g.v("{}")'.format(self.node_id)
        traversal = 'in(\'IS_AST_PARENT\')'
        result = jutils.raw_lookup(node_selection, traversal = traversal)
        return map(lambda x : ASTNode(x[0], x[1].get_properties()), result)

    def childs(self):
        node_selection = 'g.v("{}")'.format(self.node_id)
        traversal = 'out(\'IS_AST_PARENT\')'
        result = jutils.raw_lookup(node_selection, traversal = traversal)
        return map(lambda x : ASTNode(x[0], x[1].get_properties()), result)

    def function(self):
        return Function(self.function_id)

    @property
    def code(self):
        return self.get_property('code')

    @property
    def operator(self):
        return self.get_property('operator')

    @property
    def function_id(self):
        return self.get_property('function_id')

class Condition(ASTNode):

    def __init__(self, node_id, properties = None):
        Node.__init__(self, node_id, properties) 

class Symbol(Node):

    def __init__(self, node_id, properties = None):
        Node.__init__(self, node_id, properties) 

    def __str__(self):
        return self.code

    def is_callee(self):
        lucene_query = 'type:CallExpression AND functionId:"{}"'
        lucene_query = lucene_query.format(self.function_id)
        traversal = (
            'out(\'IS_AST_PARENT\')'
            '.filter{{ it.type == \'Identifier\' && it.code == "{}" }}'
        ).format(self.code)
        result = jutils.lookup(lucene_query, traversal = traversal)
        if result:
            return True
        else:
            return False

    def arguments(self):
        x = []
        node_selection = 'g.v("{}")'.format(self.node_id)
        traversal = 'hasArguments()'
        result = jutils.raw_lookup(node_selection, traversal)
        if result:
            for node_id, node in result:
                x.append(Symbol(node_id, node))
        return set(x)

    def argument_of(self):
        x = []
        node_selection = 'g.v("{}")'.format(self.node_id)
        traversal = 'isArgumentOf()'
        result = jutils.raw_lookup(node_selection, traversal)
        if result:
            for node_id, node in result:
                x.append(Symbol(node_id, node))
        return set(x)

    def assigns(self):
        x = []
        node_selection = 'g.v("{}")'.format(self.node_id)
        traversal = 'assigns()'
        result = jutils.raw_lookup(node_selection, traversal)
        if result:
            for node_id, node in result:
                x.append(Symbol(node_id, node))
        return set(x)

    def assigned_by(self):
        x = []
        node_selection = 'g.v("{}")'.format(self.node_id)
        traversal = 'isAssignedBy()'
        result = jutils.raw_lookup(node_selection, traversal)
        if result:
            for node_id, node in result:
                x.append(Symbol(node_id, node))
        return set(x)

    def traverse_to_using_conditions(self):
        node_selection = 'g.v("{}")'.format(self.node_id)
        traversal = 'in(\'USE\').filter{ it.type == \'Condition\' }'
        result = jutils.raw_lookup(node_selection, traversal = traversal)
        return map(lambda x : Condition(x[0], x[1].get_properties()), result)

    def function(self):
        return Function(self.function_id)

    @staticmethod
    def find_symbols_by_name(code):
        lucene_query = 'type:Symbol AND code:"{}"'.format(code)
        symbols = jutils.lookup(lucene_query)
        return map(lambda x : Symbol(x[0], x[1].get_properties()), symbols)

    @property
    def code(self):
        return self.get_property('code')

    @property
    def function_id(self):
        return self.get_property('functionId')

class Function(Node):
    
    def __init__(self, node_id, properties = None):
        Node.__init__(self, node_id, properties) 

    def __str__(self):
        return self.name

    def relatives(self, symbol):
        """ All function sharing the same symbol """
        if self != symbol.function():
            raise RuntimeError()
        lucene_query = 'type:Symbol AND code:"{}"'.format(symbol.code)
        traversal = 'transform{ g.v(it.functionId) }'
        relatives = []
        results = jutils.lookup(lucene_query, traversal = traversal)
        if results:
            for node_id, node in results:
                relatives.append(Function(node_id, node))
        return relatives

    def symbols(self):
        lucene_query = 'functionId:"{}" AND type:Symbol'.format(self.node_id)
        symbols = jutils.lookup(lucene_query)
        return map(lambda x : Symbol(x[0], x[1].get_properties()), symbols)

    def find_symbol_by_name(self, code):
        lucene_query = 'type:Symbol AND functionId:"{}" AND code:"{}"'
        lucene_query = lucene_query.format(self.node_id, code)
        result = jutils.lookup(lucene_query)
        if result:
            return Symbol(result[0][0], result[0][1].get_properties())
        else:
            return None

    def api_symbols(self):
        lucene_query = 'functionId:"{}"'.format(self.node_id)
        traversal = (
            'filter{ it.type == \'IdentifierDeclType\''
            '|| it.type == \'ParameterType\''
            '|| (it.type == \'Identifier\' && it.in.has(\'type\', \'CallExpression\') )'
            '}'
        )
        result = jutils.lookup(lucene_query, traversal)
        return map(lambda x : ASTNode(x[0], x[1].get_properties()), result)

    @staticmethod
    def find_functions_by_name(name):
        lucene_query = 'type:Function AND functionName:"{}"'.format(name)
        symbols = jutils.lookup(lucene_query)
        return map(lambda x : Function(x[0], x[1]), symbols)

    @property
    def name(self):
        return self.get_property('functionName')

    @property
    def signature(self):
        return self.get_property('signature')

