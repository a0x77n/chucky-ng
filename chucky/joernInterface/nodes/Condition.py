from joernInterface.nodes.ASTNode import ASTNode

class Condition(ASTNode):

    def __init__(self, node_id, properties = None):
        ASTNode.__init__(self, node_id, properties)
