
import logging

from job.Symbol import Symbol

class ChuckyJob(object):
    
    # When implementing additional command-line flags, the
    # constructor's parameter list is likely to become
    # longer and longer.
    # Suggested improvement: provide setters for each of the
    # configurable fields and remove the constructor
    
    def __init__(self, function, target_name, target_decl_type, target_type, n_neighbors):
        self.function = function
        self.n_neighbors = n_neighbors
        self.logger = logging.getLogger('chucky')
        self._initializeSymbol(target_name, target_type, target_decl_type)
        
    def _initializeSymbol(self, name, aType, declType):
        self.symbol = Symbol()
        self.symbol.setName(name)
        self.symbol.setType(aType)
        self.symbol.setDeclType(declType)
    
    def getSymbol(self):
        return self.symbol
    
    def getSymbolName(self):
        return self.symbol.target_name
    
    def getSymbolType(self):
        return self.symbol.target_type
     
    def __eq__(self, other):
        return self.symbol == other.symbol
     
    def __hash__(self):
        return self.symbol.__hash__()
    
    def __str__(self):
        if self.symbol.target_decl_type:
            s = '{} ({}) - {} {} [{}]'
            s = s.format(
                    self.function,
                    self.function.node_id,
                    self.symbol.target_decl_type,
                    self.symbol.target_name,
                    self.symbol.target_type)
            return s
        else:
            s = '{} ({}) - {} [{}]'
            s = s.format(
                    self.function,
                    self.function.node_id,
                    self.symbol.target_name,
                    self.symbol.target_type)
            return s
