from settings import Defaults

from job.Job import ChuckyJob
from joernInterface.indexLookup.FunctionLookup import FunctionLookup
from joernInterface.indexLookup.ParameterLookup import ParameterLookup
from joernInterface.indexLookup.IdentifierDeclLookup import IdentifierDeclLookup
from joernInterface.indexLookup.CallExpressionLookup import CallExpressionLookup
import re

DEFAULT_N = Defaults.N_NEIGHBORS
FUNCTION = Defaults.FUNCTION
PARAMETER = Defaults.PARAMETER
VARIABLE = Defaults.VARIABLE
CALLEE = Defaults.CALLEE

"""
Creates a list of jobs for Chucky Engine based
on user queries.
"""

class JobGenerator(object):

    def __init__(self, identifier, identifier_type):
        self.identifier = identifier
        self.identifier_type = identifier_type
        self.n_neighbors = DEFAULT_N
        self.limit = None

    """
    Generates a suitable configuration based on the objects
    internal state.

    @returns a list of ConfigRecords.
    """
    
    def generate(self):
        configurations = []
        if self.identifier_type == FUNCTION:
            functions = FunctionLookup.lookup_functions_by_name(self.identifier)
            for function in functions:
                parameters = function.function_parameters()
                configurations += self._jobs_from_symbols(parameters)
                variables = function.local_variables()
                configurations += self._jobs_from_symbols(variables)
                callees = function.function_calls()
                configurations += self._jobs_from_symbols(callees)
        elif self.identifier_type == PARAMETER:
            parameters = ParameterLookup.lookup(self.identifier, function_id = self.limit)
            configurations += self._jobs_from_symbols(parameters)
        elif self.identifier_type == VARIABLE:
            variables = IdentifierDeclLookup.lookup(self.identifier, function_id = self.limit)
            configurations += self._jobs_from_symbols(variables)
        elif self.identifier_type == CALLEE:
            callees = CallExpressionLookup.lookup(self.identifier, function_id = self.limit)
            configurations += self._jobs_from_symbols(callees)

        configurations = list(set(configurations))
            
        return configurations
        
    def _jobs_from_symbols(self, symbols):
        def f(x):
            job = ChuckyJob(x.function(), x)
            job.n_neighbors = self.n_neighbors
            return job
        return map(f, symbols)
