from joernInterface.nodes.ASTNode import ASTNode
from joernInterface.JoernInterface import jutils

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
