from joern_nodes import *
from JoernInterface import jutils

import logging

class SymbolTainter(object):

    def __init__(self, debug = False):
        self.logger = logging.getLogger('chucky')

    def taint_upwards(self, start):
        taintset = set()
        taintset.add(start)
        node_selection = 'g.v("{}")'.format(start.node_id)
        traversal = 'taintUpwards()'
        result = jutils.raw_lookup(node_selection, traversal)
        for node_id, node in result:
            taintset.add(Symbol(node_id, node.get_properties()))
        return taintset

    def taint_downwards(self, start):
        taintset = set()
        taintset.add(start)
        node_selection = 'g.v("{}")'.format(start.node_id)
        traversal = 'taintDownwards()'
        result = jutils.raw_lookup(node_selection, traversal)
        for node_id, node in result:
            taintset.add(Symbol(node_id, node.get_properties()))
        return taintset

    def taint(self, start):
        return self.taint_upwards(start) | self.taint_downwards(start)
