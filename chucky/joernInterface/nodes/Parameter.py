from joernInterface.JoernInterface import jutils
from joernInterface.nodes.ASTNode import ASTNode
from joernInterface.nodes.Identifier import Identifier
from joernInterface.nodes.Symbol import Symbol

class Parameter(ASTNode):

    def __init__(self, node_id, properties = None):
        ASTNode.__init__(self, node_id, properties) 
        assert self.node_type == 'Parameter'

    def declaration_type(self):
        traversal = "children().filter{it.type == 'ParameterType'}"
        projection = ['code']
        result = jutils.raw_lookup(self.node_selection, traversal, projection)
        return result[0][0]

    def identifier(self):
        traversal = "children().filter{it.type == 'Identifier'}"
        result = jutils.raw_lookup(self.node_selection, traversal = traversal)
        return Identifier(result[0][0], result[0][1].get_properties())

    def symbol(self):
        traversal = "defines()"
        result = jutils.raw_lookup(self.node_selection, traversal = traversal)
        return Symbol(result[0][0], result[0][1].get_properties())
