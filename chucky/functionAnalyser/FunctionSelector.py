from joernInterface.indexLookup.FunctionLookup import FunctionLookup


"""
Selection of functions based on different criteria,
e.g., symbol usage
"""

class FunctionSelector:

    # FIXME: introduce functions that only retrieve symbol
    # nodes and not entire nodes as that will greatly
    # improve performance

    """
    Determine functions using the same symbol as the
    function of interest
    """
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

    def select_functions_by_parameter(self, name, decl_type):
        return FunctionLookup.lookup_functions_by_parameter(name, decl_type)

    def select_functions_by_local_variable(self, name, decl_type):
        return FunctionLookup.lookup_functions_by_variable(name, decl_type)

    def select_functions_by_callee(self, name):
        return FunctionLookup.lookup_functions_by_callee(name)
