from joernInterface.JoernInterface import jutils
from joernInterface.nodes.Symbol import Symbol

class SymbolLookup:

    @staticmethod
    def lookup_symbols_by_name(code):
        lucene_query = 'type:Symbol AND code:"{}"'.format(code)
        symbols = jutils.lookup(lucene_query)
        return map(lambda x : Symbol(x[0], x[1].get_properties()), symbols)
