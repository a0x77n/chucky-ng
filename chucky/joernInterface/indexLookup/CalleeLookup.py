
from joernInterface.JoernInterface import jutils
from joernInterface.nodes.Symbol import Symbol

class CalleeLookup:
    
    @staticmethod
    def calleesByName(code):
        lucene_query = 'type:Callee AND code:"{}"'.format(code)
        symbols = jutils.lookup(lucene_query)
        return map(lambda x : Symbol(x[0], x[1].get_properties()), symbols)