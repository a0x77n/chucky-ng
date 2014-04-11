from conditionAnalyser.selection.symbol_tainter import SymbolTainter


class ConditionSelector:
    
    def getRelevantConditions(self, function, symbolName, symbolType):
        symbol_tainter = SymbolTainter()
        if symbolType == 'Callee':
            taintset = set()
            callees = function.calleesByName(symbolName)
            for callee in callees:
                for argument in callee.arguments():
                    taintset = taintset | symbol_tainter.taint_upwards(argument)
                for return_value in callee.return_value():
                    taintset = taintset | symbol_tainter.taint_downwards(return_value)
        else:
            symbol = function.symbolsByName(symbolName)
            taintset = symbol_tainter.taint(symbol)
        conditions = map(lambda x : x.traverse_to_using_conditions(), taintset)
        conditions = set([c for sublist in conditions for c in sublist])
        return conditions
