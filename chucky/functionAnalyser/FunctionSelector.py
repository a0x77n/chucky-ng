from joernInterface.indexLookup.FunctionLookup import FunctionLookup


"""
Selection of functions based on different criteria,
e.g., symbol usage
"""

class FunctionSelector:

    def __init__(self, job):
        self.job = job

    """
    Determine functions using the same symbol as the
    function of interest
    """
    def select_all(self):
        if self.job.symbol_type == 'Parameter':
            return self._select_by_parameter()
        elif self.job.symbol_type == 'IdentifierDecl':
            return self._select_by_variable()
        elif self.job.symbol_type == 'CallExpression':
            return self._select_by_call()
        else:
            raise RuntimeError('symbols of type %s are not supported', self.job.symbol_type)

    #def selectFunctionsUsingSymbol(self, name, decl_type):
    #    if symbol.target_type == 'Parameter':
    #        functions = FunctionLookup.lookup_functions_by_parameter(
    #                symbol.target_name,
    #                symbol.target_decl_type)
    #    elif symbol.target_type == 'Variable':
    #        functions = FunctionLookup.lookup_functions_by_variable(
    #                symbol.target_name,
    #                symbol.target_decl_type)
    #    elif symbol.target_type == 'Callee':
    #        functions = FunctionLookup.lookup_functions_by_callee(
    #                symbol.target_name)
    #    
    #    return functions

    def _select_by_parameter(self):
        return FunctionLookup.lookup_functions_by_parameter(
                self.job.symbol_name,
                self.job.symbol_decl_type)

    def _select_by_local_variable(self):
        return FunctionLookup.lookup_functions_by_variable(
                self.job.symbol_name,
                self.job.symbol_decl_type)

    def _select_by_callee(self):
        return FunctionLookup.lookup_functions_by_callee(
                self.job.symbol_name)
