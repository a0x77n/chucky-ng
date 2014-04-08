from JoernInterface import jutils

class Node(object):

    def __init__(self, node_id, properties = None):
        self.node_id = node_id
        self.properties = properties
        self.node_selection = 'g.v("{}")'.format(self.node_id)
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
        _, node = jutils.raw_lookup(self.node_selection)[0]
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
        return '{}'.format(self.code)

    def parent(self):
        traversal = 'parents()'
        result = jutils.raw_lookup(self.node_selection, traversal = traversal)
        return map(lambda x : ASTNode(x[0], x[1].get_properties()), result)

    def children(self):
        traversal = 'children()'
        result = jutils.raw_lookup(self.node_selection, traversal = traversal)
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
        return self.get_property('functionId')

class Condition(ASTNode):

    def __init__(self, node_id, properties = None):
        ASTNode.__init__(self, node_id, properties) 

class Parameter(ASTNode):

    def __init__(self, node_id, properties = None):
        ASTNode.__init__(self, node_id, properties) 

class Identifier(ASTNode):

    def __init__(self, node_id, properties = None):
        ASTNode.__init__(self, node_id, properties) 

    def declaration_type(self):
        traversal = 'identifierToType()'
        projection = ['code']
        result = jutils.raw_lookup(self.node_selection, traversal, projection)
        if result:
            return result[0][0]
        else:
            return None

    @staticmethod
    def lookup_parameter(code, decl_type = None):
        lucene_query = 'type:Parameter'
        traversal = 'ithChildren(\'1\').filter{{it.code == \'{}\'}}'.format(code)
        if decl_type:
            traversal += '.as(\'identifier\').identifierToType().filter{{it.code == \'{}\'}}.back(\'identifier\')'.format(decl_type)
        result = jutils.lookup(lucene_query, traversal)
        return map(lambda x : Identifier(x[0], x[1].get_properties()), result)

    @staticmethod
    def lookup_variable(code, decl_type = None):
        lucene_query = 'type:IdentifierDecl'
        traversal = 'ithChildren(\'1\').filter{{it.code == \'{}\'}}'.format(code)
        if decl_type:
            traversal += '.as(\'identifier\').identifierToType().filter{{it.code == \'{}\'}}.back(\'identifier\')'.format(decl_type)
        result = jutils.lookup(lucene_query, traversal)
        return map(lambda x : Identifier(x[0], x[1].get_properties()), result)

class Callee(ASTNode):

    def __init__(self, node_id, properties = None):
        ASTNode.__init__(self, node_id, properties) 

    def __str__(self):
        return '{}'.format(self.code)

    def arguments(self):
        traversal = 'calleeToArguments()'
        result = jutils.raw_lookup(self.node_selection, traversal = traversal)
        return map(lambda x : Symbol(x[0], x[1].get_properties()), result)

    def return_value(self):
        traversal = 'calleeToReturnValue()'
        result = jutils.raw_lookup(self.node_selection, traversal = traversal)
        return map(lambda x : Symbol(x[0], x[1].get_properties()), result)

    @staticmethod
    def lookup_callees_by_name(code):
        lucene_query = 'type:Callee AND code:"{}"'.format(code)
        symbols = jutils.lookup(lucene_query)
        return map(lambda x : Symbol(x[0], x[1].get_properties()), symbols)

class Symbol(Node):

    def __init__(self, node_id, properties = None):
        Node.__init__(self, node_id, properties) 

    def __str__(self):
        return '{}'.format(self.code)

    def traverse_to_using_conditions(self):
        traversal = 'symbolToUsingConditions()'
        result = jutils.raw_lookup(self.node_selection, traversal = traversal)
        return map(lambda x : Condition(x[0], x[1].get_properties()), result)

    def function(self):
        return Function(self.function_id)

    @staticmethod
    def lookup_symbols_by_name(code):
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
        return '{}'.format(self.name)

    def symbols(self):
        lucene_query = 'functionId:"{}" AND type:Symbol'.format(self.node_id)
        symbols = jutils.lookup(lucene_query)
        return map(lambda x : Symbol(x[0], x[1].get_properties()), symbols)

    def callees(self):
        lucene_query = 'functionId:"{}" AND type:Callee'.format(self.node_id)
        result = jutils.lookup(lucene_query)
        return map(lambda x : Callee(x[0], x[1].get_properties()), result)

    def parameters(self):
        lucene_query = 'functionId:"{}" AND type:Identifier'.format(self.node_id)
        traversal = 'filterParameters()'
        symbols = jutils.lookup(lucene_query, traversal = traversal)
        return map(lambda x : Identifier(x[0], x[1].get_properties()), symbols)

    def variables(self):
        lucene_query = 'functionId:"{}" AND type:Identifier'.format(self.node_id)
        traversal = 'filterVariables()'
        symbols = jutils.lookup(lucene_query, traversal = traversal)
        return map(lambda x : Identifier(x[0], x[1].get_properties()), symbols)

    def lookup_symbol_by_name(self, code):
        lucene_query = 'type:Symbol AND functionId:"{}" AND code:"{}"'
        lucene_query = lucene_query.format(self.node_id, code)
        result = jutils.lookup(lucene_query)
        return Symbol(result[0][0], result[0][1].get_properties())

    def lookup_callees_by_name(self, code):
        lucene_query = 'type:Callee AND functionId:"{}" AND code:"{}"'
        lucene_query = lucene_query.format(self.node_id, code)
        result = jutils.lookup(lucene_query)
        return map(lambda x : Callee(x[0], x[1].get_properties()), result)

    def api_symbol_nodes(self):
        traversal = 'functionToAPISymbolNodes()'
        result = jutils.raw_lookup(self.node_selection, traversal)
        return map(lambda x : ASTNode(x[0], x[1].get_properties()), result)

    @staticmethod
    def lookup_functions_by_name(name):
        lucene_query = 'type:Function AND name:"{}"'.format(name)
        result = jutils.lookup(lucene_query)
        return map(lambda x : Function(x[0], x[1]), result)

    @staticmethod
    def lookup_functions_by_callee(code):
        lucene_query = 'type:Callee AND code:"{}"'.format(code)
        traversal = 'functions().dedup()'
        result = jutils.lookup(lucene_query, traversal)
        return map(lambda x : Function(x[0], x[1]), result)

    @staticmethod
    def lookup_functions_by_parameter(code, decl_type = None):
        lucene_query = 'type:Parameter'
        traversal = 'ithChildren(\'1\').filter{{it.code == \'{}\'}}'.format(code)
        if decl_type:
            traversal += '.identifierToType().filter{{it.code == \'{}\'}}'.format(decl_type)
        traversal += '.functions().dedup()'
        result = jutils.lookup(lucene_query, traversal)
        return map(lambda x : Function(x[0], x[1]), result)

    @staticmethod
    def lookup_functions_by_variable(code, decl_type = None):
        lucene_query = 'type:IdentifierDecl'
        traversal = 'ithChildren(\'1\').filter{{it.code == \'{}\'}}'.format(code)
        if decl_type:
            traversal += '.identifierToType().filter{{it.code == \'{}\'}}'.format(decl_type)
        traversal += '.functions().dedup()'
        result = jutils.lookup(lucene_query, traversal)
        return map(lambda x : Function(x[0], x[1]), result)

    @staticmethod
    def lookup_functions_by_symbol(code):
        lucene_query = 'type:Symbol AND code:"{}"'.format(code)
        traversal = 'functions().dedup()'
        result = jutils.lookup(lucene_query, traversal)
        return map(lambda x : Function(x[0], x[1]), result)

    @property
    def name(self):
        return self.get_property('name')

    @property
    def signature(self):
        return self.get_property('signature')
