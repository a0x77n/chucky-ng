from joernInterface.nodes.ASTNode import ASTNode
from joernInterface.JoernInterface import jutils
from joernInterface.nodes.Symbol import Symbol

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
    