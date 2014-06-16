from joernInterface.JoernInterface import jutils
from settings import Defaults

SOURCE = Defaults.SOURCE
SINK = Defaults.SINK

class SliceConditions(object):
   
    def __init__(self, statement, symbol):
        self.statement = statement
        self.symbol = symbol
        self.category = SOURCE

    def __setattr__(self, name, value):
        if name == 'category':
            if value in [SOURCE, SINK]:
                object.__setattr__(self, name, value)
            else:
                raise AttributeError()
        else:
            object.__setattr__(self, name, value)

    def getKey(self):
        return int(self.statement.node_id)
    
    def getFeatures(self):
        node_selection = self.statement.node_selection
        traversal_steps = []
        if self.category == SOURCE:
            traversal_steps.append("forwardSlice('{}')".format(self.symbol))
        else:
            traversal_steps.append("backwardSlice('{}')".format(self.symbol))
        traversal_steps.append("astNodes().filter{it.type == 'Condition'}")
        traversal_steps.append("dedup()")
        traversal_steps.append("normalize(['{}' : '\$SYM'])".format(self.symbol))
        traversal = '.'.join(traversal_steps)
        x = jutils.runGremlinCommands(['.'.join([node_selection, traversal])])
        #print '.'.join([node_selection, traversal])
        #print self.statement
        #for feat in x:
        #    print self.getKey(), feat
        #print
        return x
