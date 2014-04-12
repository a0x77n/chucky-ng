from conditionAnalyser.selection.ConditionSelector import ConditionSelector
from conditionAnalyser.normalization.ConditionNormalizer import ConditionNormalizer
from joernInterface.JoernInterface import jutils

import itertools

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
        #conditions = ConditionSelector().getRelevantConditions(self.obj, self.symbolName, self.symbolType)
        #normalizedConditions = ConditionNormalizer().normalize(conditions, self.obj, self.symbolName, self.symbolType)
        #normalizedConditions = set(itertools.chain(*normalizedConditions))
        #for i, feat in enumerate(sorted(normalizedConditions)):
        #    print i, '\t', feat

        normalizedConditions = self.conditions()
        normalizedConditions = set(normalizedConditions)
        #for i, feat in enumerate(sorted(normalizedConditions)):
        #    print i, '\t', feat
        #return itertools.chain(*normalizedConditions)
        return normalizedConditions

    def conditions(self):
        lucene_query = 'conditions = []; argList = []; retList = []; queryNodeIndex(\'type:"{}" AND functionId:"{}" AND code:"{}"\')'
        if self.symbolType == 'Callee':
            lucene_query = lucene_query.format('Callee', self.obj.node_id, self.symbolName)
            traversal = (
                    'copySplit('
                    '_().calleeToArguments().store(argList, {it.code}).taintUpwards(),'
                    '_().calleeToReturnValue().store(retList, {it.code}).taintDownwards())'
                    '.fairMerge().dedup()'
            )
        else:
            lucene_query = lucene_query.format('Symbol', self.obj.node_id, self.symbolName)
            traversal = (
                    'copySplit('
                    '_().taintUpwards(),'
                    '_().taintDownwards())'
                    '.fairMerge().dedup()'
            )
        traversal += '.symbolToUsingConditions().dedup()'
        traversal += '.store(conditions).iterate()'
        command = '.'.join([lucene_query, traversal])
        command += '; g.transform{ conditions }.scatter().normalize(argList, retList)'
        x = jutils.joern.runGremlinQuery(command)
        return x
