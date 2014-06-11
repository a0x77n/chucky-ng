from joernInterface.JoernInterface import jutils

class FunctionConditions:
    
    def __init__(self, obj):
        self.obj = obj
    
    def setSymbolName(self, name):
        self.symbolName = name
    
    def setSymbolType(self, aType):
        self.symbolType = aType
    
    def getKey(self):
        return int(self.obj.node_id)
    
    def getFeatures(self):
        normalizedConditions = self.normalize_conditions()
        #print
        #print self.getKey()
        #for i, feat in enumerate(sorted(normalizedConditions)):
        #    print i, '\t', feat
        return normalizedConditions

    def normalize_conditions(self):
        if self.symbolType == 'CallExpression':
            declaration = "map = [:]"
            initialization1 = (
                    "queryNodeIndex('type:\"Callee\" AND functionId:\"{}\" AND code:\"{}\"')"
                    ".calleeToCall()"
                    ".callToLVal()"
                    ".sideEffect{{map[it.code] = \"\$RET\"}}.iterate()"
            ).format(self.obj.node_id, self.symbolName)
            initialization2 = (
                    "queryNodeIndex('type:\"Callee\" AND functionId:\"{}\" AND code:\"{}\"')"
                    ".calleeToCall().callToArguments()"
                    ".argumentToAtomName()"
                    ".sideEffect{{map[it.code] = \"\$ARG\"}}.iterate()"
            ).format(self.obj.node_id, self.symbolName)
            node_selection =  'queryNodeIndex(\'type:"{}" AND functionId:"{}" AND code:"{}"\')'
            node_selection = node_selection.format('Callee', self.obj.node_id, self.symbolName)
            traversal = (
                    "copySplit("
                    "_().calleeToCall().callToArguments().uses().taintUpwards(),"
                    "_().statements().defines().taintDownwards())"
                    ".fairMerge().dedup()"
                    ".symbolToUsingConditions().dedup()"
                    ".normalize(map)"
            )
            command = '.'.join([node_selection, traversal])
            x = jutils.runGremlinCommands([declaration, initialization1, initialization2, command])
        else:
            node_selection = 'queryNodeIndex(\'type:"Symbol" AND functionId:"{}" AND code:"{}"\')'
            node_selection = node_selection.format(self.obj.node_id, self.symbolName)
            traversal = (
                    "copySplit("
                    "_().taintUpwards(),"
                    "_().taintDownwards())"
                    ".fairMerge().dedup()"
                    ".symbolToUsingConditions().dedup()"
                    ".normalize()"
            )
            command = '.'.join([node_selection, traversal])
            x = jutils.runGremlinCommands([command])
        return set(x)
