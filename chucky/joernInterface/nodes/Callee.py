from joernInterface.nodes.ASTNode import ASTNode

class Callee(ASTNode):

    def __init__(self, node_id, properties = None):
        ASTNode.__init__(self, node_id, properties) 
        assert self.node_type == 'Callee'
