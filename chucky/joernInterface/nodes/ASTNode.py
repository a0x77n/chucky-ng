from joernInterface.nodes.Node import Node
from joernInterface.JoernInterface import jutils


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
        from joernInterface.nodes.Function import Function
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