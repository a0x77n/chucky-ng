from settings import Defaults

from joernInterface.JoernInterface import jutils
from joernInterface.nodes.ASTNode import ASTNode
from joernInterface.indexLookup.ParameterLookup import ParameterLookup
from joernInterface.indexLookup.IdentifierDeclLookup import IdentifierDeclLookup
from joernInterface.indexLookup.CallExpressionLookup import CallExpressionLookup

from collections import defaultdict as dict

import logging

SOURCE = Defaults.SOURCE
SINK = Defaults.SINK
NOSINK = 'nosink'

class SliceFilter(object):
   
    def __init__(self, job):
        self.job = job
        self.logger = logging.getLogger('chucky')

    def filter(self, systems):
        if self.job.category == SOURCE:
            return self._filter_by_sinks(systems)
        else:
            return systems # no implemented yet

    def _filter_by_sinks(self, systems):

        accept = self._select_accepted_sinks()
        self.logger.debug("Filter by sink(s) ({})".format(', '.join(accept)))
        common_sinks = dict(set)
        other_sinks = dict(set)

        for source, symbol in systems:
            sinks = self._select_sinks(source, symbol)
            for sink in sinks:
                if sink in accept:
                    common_sinks[sink].add((source, symbol))
                else:
                    other_sinks[sink].add((source, symbol))
            if not sinks:
                if not accept:
                    common_sinks[NOSINK].add((source, symbol))
                else:
                    other_sinks[NOSINK].add((source, symbol))
        try:
            result = set()
            for sink in sorted(common_sinks, key = lambda x : len(common_sinks[x]), reverse = True):
                if len(result) >= self.job.n_neighbors:
                    break;
                else:
                    self.logger.debug('+ Selected sink {}, {} matching slices.'.format(sink, len(common_sinks[sink])))
                    result.update(common_sinks[sink])
                break
            #for sink in sorted(other_sinks, key = lambda x : len(other_sinks[x]), reverse = True):
            #    if len(result) >= self.job.n_neighbors:
            #        break;
            #    else:
            #        self.logger.debug('- Selected sink {}, {} matching slices.'.format(sink, len(other_sinks[sink])))
            #        result.update(other_sinks[sink])
        except Exception, e:
            self.logger.error(e)
            return []
        else:
            if len(result) >= self.job.n_neighbors:
                return list(result)
            elif len(result) > 1:
                return list(result)
            else:
                return []

    def _select_accepted_sinks(self):
        node_selection = self.job.target.node_selection
        if self.job.symbol_type == 'CallExpression':
            symbol = self.job.symbol.return_symbol()
        else:
            symbol = self.job.symbol_name
        return self._select_sinks(self.job.target, symbol)

    def _select_sinks(self, statement, symbol):
        traversal = "statementToSinks('{}')".format(symbol)
        command = '.'.join([statement.node_selection, traversal])
        sinks = jutils.runGremlinCommands([command])
        return sinks
