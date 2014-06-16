from joernInterface.nodes.ASTNode import ASTNode
from joernInterface.JoernInterface import jutils

class Statement(ASTNode):

    def __init__(self, node_id, properties = None):
        ASTNode.__init__(self, node_id, properties)

    def follow_symbol_downwards(self, symbol, hops = 1):
        traversal = "outE('REACHES').filter{{it.var == '{}'}}.inV".format(symbol)
        if hops > 1:
            traversal += "out('REACHES').loop(1){{it.loops < {}}}{{true}}".format(hops-1)
        results = jutils.raw_lookup(self.node_selection, traversal)
        return map(lambda x : Statement(x[0], x[1].get_properties()), results)
