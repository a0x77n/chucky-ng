from conditionAnalyser.selection.ConditionSelector import ConditionSelector
from conditionAnalyser.normalization.ConditionNormalizer import ConditionNormalizer

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
        conditions = ConditionSelector().getRelevantConditions(self.obj, self.symbolName, self.symbolType)
        normalizedConditions = ConditionNormalizer().normalize(conditions, self.obj, self.symbolName, self.symbolType)
        return set(itertools.chain(*normalizedConditions))
        
