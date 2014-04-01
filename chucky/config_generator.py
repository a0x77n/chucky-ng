from joern_nodes import *

import logging

class ConfigRecord():
    
    def __init__(self, function, target_name, target_type, n_neighbors):
        self.function = function
        self.target_name = target_name
        self.target_type = target_type
        self.n_neighbors = n_neighbors
        self.logger = logging.getLogger('chucky')

    def __str__(self):
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
                for parameter in set(map(lambda x : x.code, function.parameters())):
                    configurations.append(
                            ConfigRecord(function, parameter, 'Parameter', self.n_neighbors))
                for variable in set(map(lambda x : x.code, function.variables())):
                    configurations.append(
                            ConfigRecord(function, variable, 'Variable', self.n_neighbors))
                for callee in set(map(lambda x : x.code, function.callees())):
                    configurations.append(
                            ConfigRecord(function, callee, 'Callee', self.n_neighbors))
        elif self.identifier_type == 'parameter':
            functions = Function.lookup_functions_by_parameter(self.identifier)
            for function in functions:
                configurations.append(
                        ConfigRecord(function, self.identifier, 'Parameter', self.n_neighbors))
        elif self.identifier_type == 'variable':
            functions = Function.lookup_functions_by_variable(self.identifier)
            for function in functions:
                configurations.append(
                        ConfigRecord(function, self.identifier, 'Variable', self.n_neighbors))
        elif self.identifier_type == 'callee':
            functions = Function.lookup_functions_by_callee(self.identifier)
            for function in functions:
                configurations.append(
                        ConfigRecord(function, self.identifier, 'Callee', self.n_neighbors))
        return configurations

    def group_callees_by_function_id(self, callees):
        groups = {}
        for callee in callees:
            if callee.function_id not in groups:
                groups[callee.function_id] = []
            groups[callee.function_id].append(callee)
        return groups.items()

    def group_callees_by_code(self, callees):
        groups = {}
        for callee in callees:
            if callee.code not in groups:
                groups[callee.code] = []
            groups[callee.code].append(callee)
        return groups.items()
