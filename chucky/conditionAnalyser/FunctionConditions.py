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
        #for i, feat in enumerate(sorted(normalizedConditions)):
        #    print i, '\t', feat
        return normalizedConditions

    def normalize_conditions(self):
        declarations = 'argList = []; retList = []' 
        node_selection =  'queryNodeIndex(\'type:"{}" AND functionId:"{}" AND code:"{}"\')'
        if self.symbolType == 'Callee':
            node_selection = node_selection.format('Callee', self.obj.node_id, self.symbolName)
            taint_traversal = (
                    'copySplit('
                    '_().calleeToArguments().aggregate(argList, {it.code}).taintUpwards(),'
                    '_().calleeToReturnValue().aggregate(retList, {it.code}).taintDownwards())'
                    '.fairMerge().dedup()'
            )
        else:
            node_selection = node_selection.format('Symbol', self.obj.node_id, self.symbolName)
            taint_traversal = (
                    'copySplit('
                    '_().taintUpwards(),'
                    '_().taintDownwards())'
                    '.fairMerge().dedup()'
            )
        condition_traversal = 'symbolToUsingConditions().dedup()'
        normalization = 'normalize(argList, retList)'
        command = '.'.join([node_selection, taint_traversal, condition_traversal, normalization])
        x = jutils.runGremlinCommands([declarations, command])
        return set(x)
