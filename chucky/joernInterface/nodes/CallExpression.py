from joernInterface.JoernInterface import jutils
from joernInterface.nodes.ASTNode import ASTNode
from joernInterface.nodes.Symbol import Symbol
from joernInterface.nodes.Callee import Callee

class CallExpression(ASTNode):

    def __init__(self, node_id, properties = None):
        ASTNode.__init__(self, node_id, properties) 
        assert self.node_type == 'CallExpression'

    def arguments(self):
        traversal = "ithChildren('1').children().uses()"
        result = jutils.raw_lookup(self.node_selection, traversal = traversal)
        return map(lambda x : Symbol(x[0], x[1].get_properties()), result)

    def argument(self, i):
        traversal = "ithChildren('1').children().filter{{it.childNum == '{}'}}.uses()".format(i)
        result = jutils.raw_lookup(self.node_selection, traversal = traversal)
        return Symbol(result[0][0], result[0][1].get_properties())

    def return_symbol(self):
        traversal = 'statements().defines()'
        result = jutils.raw_lookup(self.node_selection, traversal = traversal)
        if result:
            return Symbol(result[0][0], result[0][1].get_properties())
        else:
            None

    def callee(self):
        traversal = "ithChildren('0')"
        result = jutils.raw_lookup(self.node_selection, traversal = traversal)
        return Callee(result[0][0], result[0][1].get_properties())
