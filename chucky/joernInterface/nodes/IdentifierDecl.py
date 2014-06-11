from joernInterface.JoernInterface import jutils
from joernInterface.nodes.ASTNode import ASTNode
from joernInterface.nodes.Identifier import Identifier

class IdentifierDecl(ASTNode):

    def __init__(self, node_id, properties = None):
        ASTNode.__init__(self, node_id, properties) 
        assert self.node_type == 'IdentifierDecl'

    def declaration_type(self):
        traversal = "children().filter{it.type == 'IdentifierDeclType'}"
        projection = ['code']
        result = jutils.raw_lookup(self.node_selection, traversal, projection)
        return result[0][0]

    def identifier(self):
        traversal = "children().filter{it.type == 'Identifier'}"
        result = jutils.raw_lookup(self.node_selection, traversal = traversal)
        return Identifier(result[0][0], result[0][1].get_properties())
