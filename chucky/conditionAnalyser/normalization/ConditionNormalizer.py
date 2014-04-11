from conditionAnalyser.normalization.expression_normalizer import ExpressionNormalizer
from joernInterface.JoernInterface import jutils

class ConditionNormalizer:
    
    def normalize(self, conditions, function, symbolName, symbolType):
        argset = self._arguments(function, symbolName, symbolType)
        retset = self._return_values(function, symbolName, symbolType)
        argList = ', '.join(map(lambda x : '\"{}\"'.format(x), argset))
        retList = ', '.join(map(lambda x : '\"{}\"'.format(x), retset))
        
        retval = []
        for condition in conditions:
            traversal = 'normalize([{}], [{}])'.format(argList, retList)
            command = '.'.join([condition.node_selection, traversal])
            x = jutils.joern.runGremlinQuery(command)
            retval.append(x)
        return retval
        
    def _arguments(self, function, symbolName, symbolType):
        if symbolType == 'Callee':
            callees = function.calleesByName(symbolName)
            arguments = map(lambda x : x.arguments(), callees)
            arguments = [arg for sublist in arguments for arg in sublist]
            return set(arguments)
        else:
            return set()

    def _return_values(self, function, symbolName, symbolType):
        if symbolType == 'Callee':
            callees = function.calleesByName(symbolName)
            arguments = map(lambda x : x.return_value(), callees)
            arguments = [arg for sublist in arguments for arg in sublist]
            return set(arguments)
        else:
            return set()
