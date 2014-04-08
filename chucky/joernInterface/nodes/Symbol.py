from joernInterface.nodes.Node import Node
from joernInterface.JoernInterface import jutils
from joernInterface.nodes.Condition import Condition


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
        from joernInterface.nodes.Function import Function
        return Function(self.function_id)

    @property
    def code(self):
        return self.get_property('code')

    @property
    def function_id(self):
        return self.get_property('functionId')


    @property
    def name(self):
        return self.get_property('name')

    @property
    def signature(self):
        return self.get_property('signature')

