from joernInterface.JoernInterface import jutils
from joernInterface.nodes.Node import Node
from joernInterface.nodes.Callee import Callee
from joernInterface.nodes.Identifier import Identifier
from joernInterface.nodes.ASTNode import ASTNode
from joernInterface.nodes.Symbol import Symbol
from joernInterface.nodes.CallExpression import CallExpression
from joernInterface.nodes.Parameter import Parameter
from joernInterface.nodes.IdentifierDecl import IdentifierDecl

class Function(Node):
    
    def __init__(self, node_id, properties = None):
        Node.__init__(self, node_id, properties) 
        assert self.node_type == 'Function'

    def __str__(self):
        return '{}'.format(self.name)

    def symbols(self):
        lucene_query = 'functionId:"{}" AND type:Symbol'.format(self.node_id)
        symbols = jutils.lookup(lucene_query)
        return map(lambda x : Symbol(x[0], x[1].get_properties()), symbols)

    def callees(self, callee = None):
        lucene_query = 'functionId:"{}" AND type:CallExpression'.format(self.node_id)
        traversal = None
        if callee:
            traversal_steps = []
            traversal_steps.append("as('call')")
            traversal_steps.append("children()")
            traversal_steps.append("filter{{it.type == 'Callee' && it.code == '{}'}}".format(callee))
            traversal_steps.append("back('call')")
            traversal = '.'.join(traversal_steps)
        result = jutils.lookup(lucene_query, traversal = traversal)
        return map(lambda x : CallExpression(x[0], x[1].get_properties()), result)

    def parameters(self, param = None):
        lucene_query = 'functionId:"{}" AND type:Parameter'.format(self.node_id)
        traversal = None
        if param:
            traversal_steps = []
            traversal_steps.append("as('param')")
            traversal_steps.append("children()")
            traversal_steps.append("filter{{it.type == 'Identifier' && it.code == '{}'}}".format(param))
            traversal_steps.append("back('param')")
            traversal = '.'.join(traversal_steps)
        result = jutils.lookup(lucene_query, traversal = traversal)
        return map(lambda x : Parameter(x[0], x[1].get_properties()), result)

    def local_variables(self, var = None):
        lucene_query = 'functionId:"{}" AND type:IdentifierDecl'.format(self.node_id)
        traversal = None
        if var:
            traversal_steps = []
            traversal_steps.append("as('var')")
            traversal_steps.append("children()")
            traversal_steps.append("filter{{it.type == 'Identifier' && it.code == '{}'}}".format(var))
            traversal_steps.append("back('var')")
            traversal = '.'.join(traversal_steps)
        result = jutils.lookup(lucene_query, traversal = traversal)
        result = jutils.lookup(lucene_query)
        return map(lambda x : IdentifierDecl(x[0], x[1].get_properties()), result)

    #def callees(self):
    #    lucene_query = 'functionId:"{}" AND type:Callee'.format(self.node_id)
    #    result = jutils.lookup(lucene_query)
    #    return map(lambda x : Callee(x[0], x[1].get_properties()), result)

    #def parameters(self):
    #    lucene_query = 'functionId:"{}" AND type:Identifier'.format(self.node_id)
    #    traversal = 'filterParameters()'
    #    symbols = jutils.lookup(lucene_query, traversal = traversal)
    #    return map(lambda x : Identifier(x[0], x[1].get_properties()), symbols)

    #def variables(self):
    #    lucene_query = 'functionId:"{}" AND type:Identifier'.format(self.node_id)
    #    traversal = 'filterVariables()'
    #    symbols = jutils.lookup(lucene_query, traversal = traversal)
    #    return map(lambda x : Identifier(x[0], x[1].get_properties()), symbols)

    def api_symbol_nodes(self):
        traversal = 'functionToAPISymbolNodes()'
        result = jutils.raw_lookup(self.node_selection, traversal)
        return map(lambda x : ASTNode(x[0], x[1].get_properties()), result)
    
    #def symbolsByName(self, code):
    #    lucene_query = 'type:Symbol AND functionId:"{}" AND code:"{}"'
    #    lucene_query = lucene_query.format(self.node_id, code)
    #    result = jutils.lookup(lucene_query)
    #    return Symbol(result[0][0], result[0][1].get_properties())

    
    #def calleesByName(self, code):
    #    lucene_query = 'type:Callee AND functionId:"{}" AND code:"{}"'
    #    lucene_query = lucene_query.format(self.node_id, code)
    #    result = jutils.lookup(lucene_query)
    #    return map(lambda x : Callee(x[0], x[1].get_properties()), result)
    
    @property
    def name(self):
        return self.get_property('name')

    @property
    def signature(self):
        return self.get_property('signature')

