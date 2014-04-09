from conditionNormalization.expression_normalizer import ExpressionNormalizer

class ConditionNormalizer:
    
    def normalize(self, conditions, function, symbolName, symbolType):
        argset = self._arguments(function, symbolName, symbolType)
        retset = self._return_values(function, symbolName, symbolType)
        expr_normalizer = ExpressionNormalizer(argset, retset)
        
        retval = []
        for condition in conditions:
            root_expr = condition.children()[0]
            # self.logger.debug('Normalizing condition ( {} ) ({})'.format(root_expr, root_expr.node_id))
            x = [expr for expr in expr_normalizer.normalize_expression(root_expr)]
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