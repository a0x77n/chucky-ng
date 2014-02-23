from joern_nodes import *

import logging

class ConfigRecord():
    
    def __init__(self, function, symbol, n):
        self.function = function
        self.symbol = symbol
        self.n = n
        self.logger = logging.getLogger('chucky')

    def __str__(self):
        s = '{} ({}) - {} ({})'
        s = s.format(
                self.function,
                self.function.node_id,
                self.symbol,
                self.symbol.node_id)
        return s

    @staticmethod
    def generate(identifier, identifier_type, n):
        if identifier_type == 'symbol':
            symbols = Symbol.find_symbols_by_name(identifier)
            for symbol in symbols:
                yield ConfigRecord(symbol.function(), symbol, n)
        elif identifier_type == 'function':
            functions = Function.find_functions_by_name(identifier)
            for function in functions:
                for symbol in function.symbols():
                    yield ConfigRecord(function, symbol, n)
