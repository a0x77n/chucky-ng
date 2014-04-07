from joern_nodes import *
from job.Job import ChuckyJob

import logging

PARAMETER = 'Parameter'
VARIABLE = 'Variable'
CALLEE = 'Callee'

"""
Creates a list of jobs for Chucky Engine based
on user queries.
"""

class JobGenerator(object):

    # Suggested improvement: see ChuckyJob
    
    def __init__(self, identifier, identifier_type, n_neighbors):
        self.identifier = identifier
        self.identifier_type = identifier_type
        self.n_neighbors = n_neighbors

    """
    Generates a suitable configuration based on the objects
    internal state.

    @returns a list of ConfigRecords.
    """
    
    def generate(self):
        configurations = []
        if self.identifier_type == 'function':
            functions = Function.lookup_functions_by_name(self.identifier)
            for function in functions:
                parameters = function.parameters()
                parameters = map(lambda x : (x.code, x.declaration_type()), parameters)
                parameters = set(parameters)
                for parameter, parameter_type in parameters:
                    configuration = ChuckyJob(
                            function,
                            parameter,
                            parameter_type,
                            PARAMETER,
                            self.n_neighbors)
                    configurations.append(configuration)
                variables = function.variables()
                variables = map(lambda x : (x.code, x.declaration_type()), variables)
                variables = set(variables)
                for variable, variable_type in variables:
                    configuration = ChuckyJob(
                            function,
                            variable,
                            variable_type,
                            VARIABLE,
                            self.n_neighbors)
                    configurations.append(configuration)
                callees = function.callees()
                callees = map(lambda x : x.code, callees)
                callees = set(callees)
                for callee in callees:
                    configuration = ChuckyJob(
                            function,
                            callee,
                            None,
                            CALLEE,
                            self.n_neighbors)
                    configurations.append(configuration)
        elif self.identifier_type == 'parameter':
            parameters = Identifier.lookup_parameter(self.identifier)
            for parameter in parameters:
                configuration = ChuckyJob(
                        parameter.function(),
                        parameter.code,
                        parameter.declaration_type(),
                        PARAMETER,
                        self.n_neighbors)
                configurations.append(configuration)
        elif self.identifier_type == 'variable':
            variables = Identifier.lookup_variables(self.identifier)
            for variable in variables:
                configuration = ChuckyJob(
                        variable.function(),
                        variable.code,
                        variable.declaration_type(),
                        VARIABLE,
                        self.n_neighbors)
                configurations.append(configuration)
        elif self.identifier_type == 'callee':
            callees = Callee.lookup_callees_by_name(self.identifier)
            for callee in callees:
                configuration = ChuckyJob(
                        callee.function(),
                        callee.code,
                        None,
                        CALLEE,
                        self.n_neighbors)
                configurations.append(configuration)
        return configurations
