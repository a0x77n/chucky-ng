from joern_nodes import *

import logging

PARAMETER = 'Parameter'
VARIABLE = 'Variable'
CALLEE = 'Callee'


class ConfigRecord(object):
    
    def __init__(self, function, target_name, target_decl_type, target_type, n_neighbors):
        self.function = function
        self.target_name = target_name
        self.target_decl_type = target_decl_type
        self.target_type = target_type
        self.n_neighbors = n_neighbors
        self.logger = logging.getLogger('chucky')

    def __str__(self):
        if self.target_decl_type:
            s = '{} ({}) - {} {} [{}]'
            s = s.format(
                    self.function,
                    self.function.node_id,
                    self.target_decl_type,
                    self.target_name,
                    self.target_type)
            return s
        else:
            s = '{} ({}) - {} [{}]'
            s = s.format(
                    self.function,
                    self.function.node_id,
                    self.target_name,
                    self.target_type)
            return s

class ConfigGenerator(object):

    def __init__(self, identifier, identifier_type, n_neighbors):
        self.identifier = identifier
        self.identifier_type = identifier_type
        self.n_neighbors = n_neighbors

    def generate(self):
        configurations = []
        if self.identifier_type == 'function':
            functions = Function.lookup_functions_by_name(self.identifier)
            for function in functions:
                parameters = function.parameters()
                parameters = map(lambda x : (x.code, x.declaration_type()), parameters)
                parameters = set(parameters)
                for parameter, parameter_type in parameters:
                    configuration = ConfigRecord(
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
                    configuration = ConfigRecord(
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
                    configuration = ConfigRecord(
                            function,
                            callee,
                            None,
                            CALLEE,
                            self.n_neighbors)
                    configurations.append(configuration)
        elif self.identifier_type == 'parameter':
            parameters = Identifier.lookup_parameter(self.identifier)
            for parameter in parameters:
                configuration = ConfigRecord(
                        parameter.function(),
                        parameter.code,
                        parameter.declaration_type(),
                        PARAMETER,
                        self.n_neighbors)
                configurations.append(configuration)
        elif self.identifier_type == 'variable':
            variables = Identifier.lookup_variables(self.identifier)
            for variable in variables:
                configuration = ConfigRecord(
                        variable.function(),
                        variable.code,
                        variable.declaration_type(),
                        VARIABLE,
                        self.n_neighbors)
                configurations.append(configuration)
        elif self.identifier_type == 'callee':
            callees = Callee.lookup_callees_by_name(self.identifier)
            for callee in callees:
                configuration = ConfigRecord(
                        callee.function(),
                        callee.code,
                        None,
                        CALLEE,
                        self.n_neighbors)
                configurations.append(configuration)
        return configurations
