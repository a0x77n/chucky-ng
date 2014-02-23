from joern_nodes import *

import logging

class SymbolTainter(object):

    def __init__(self, debug = False):
        self.logger = logging.getLogger('chucky')
    
    def start_symbol(self, function, symbol):
        lucene_query = 'type:Symbol AND code:"{}" AND functionId:"{}"'
        lucene_query = lucene_query.format(symbol, function)
        projection = ['id']
        symbol = jutils.lookup(lucene_query, projection = projection)
        if symbol:
            return symbol[0][0]
        return None
    
    def _taint_up(self, up, new):
        if new:
            up = up | new
            tmp = set()
            for symbol in new:
                x = symbol.arguments()
                if x:
                    self.logger.debug('%s has arguments %s.', symbol, ', '.join(map(str, x)))
                    tmp = x
                    continue
                else:
                    self.logger.debug('%s has arguments --', symbol)
                y = symbol.assigned_by()
                if y:
                    self.logger.debug('%s is assigned by %s.', symbol, ', '.join(map(str, y)))
                    tmp = y
                    continue
                else:
                    self.logger.debug('%s is assigned by  --', symbol)
            return self._taint_up(up, tmp - up)
        else:
            return up

    def _taint_down(self, down, new):
        if new:
            down = down | new
            tmp = set()
            for symbol in new:
                x = symbol.argument_of()
                if x:
                    self.logger.debug('%s is arguments of %s.', symbol, ', '.join(map(str, x)))
                    tmp = x 
                    continue
                else:
                    self.logger.debug('%s is argument of  --', symbol)
                y = symbol.assigns()
                if y:
                    self.logger.debug('%s assigns %s.', symbol, ', '.join(map(str, y)))
                    tmp = y
                    continue
                else:
                    self.logger.debug('%s assigns --', symbol)
            return self._taint_down(down, tmp - down)
        else:
            return down

    def taint(self, start_symbol):
        symbols = self._taint_up(set(), set([start_symbol]))
        symbols = symbols | self._taint_down(set(), set([start_symbol]))
        return symbols
