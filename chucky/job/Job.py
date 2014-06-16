from settings import Defaults

DEFAULT_N = Defaults.N_NEIGHBORS

class ChuckyJob(object):
    
    def __init__(self, target, symbol):
        self.target = target
        self.symbol = symbol
        self.n_neighbors = DEFAULT_N

    def __setattr__(self, name, value):
        try:
            if name == 'symbol':
                if value.node_type in ['CallExpression', 'Parameter', 'IdentifierDecl']:
                    object.__setattr__(self, name, value)
                else:
                    raise AttributeError()
            else:
                object.__setattr__(self, name, value)
        except:
            raise AttributeError()
        
    def __eq__(self, other):
        if self.target != other.target:
            return False
        if self.symbol_type != other.symbol_type:
            return False
        if self.symbol_name != other.symbol_name:
            return False
        if self.symbol_decl_type != other.symbol_decl_type:
            return False
        return True

    def __hash__(self):
        return hash(self.target) ^ hash(self.symbol_name)
    
    def __str__(self):
        s = '{} ({}) - {} {} [{}]'
        s = s.format(
                self.target,
                self.target.node_id,
                self.symbol_decl_type or '_',
                self.symbol_name,
                self.symbol_type)
        return s

    @property
    def function(self):
        return self.target

    @property
    def symbol_type(self):
        return self.symbol.node_type

    @property
    def symbol_name(self):
        if self.symbol_type == 'CallExpression':
            return self.symbol.callee().code
        else:
            return self.symbol.identifier().code

    @property
    def symbol_decl_type(self):
        if self.symbol_type == 'CallExpression':
            return None
        else:
            return self.symbol.declaration_type()
