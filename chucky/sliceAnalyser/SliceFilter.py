from settings import Defaults

from joernInterface.JoernInterface import jutils
from joernInterface.nodes.ASTNode import ASTNode
from joernInterface.indexLookup.ParameterLookup import ParameterLookup
from joernInterface.indexLookup.IdentifierDeclLookup import IdentifierDeclLookup
from joernInterface.indexLookup.CallExpressionLookup import CallExpressionLookup

import logging

SOURCE = Defaults.SOURCE
SINK = Defaults.SINK

class SliceFilter(object):
   
    def __init__(self, job):
        self.job = job
        self.logger = logging.getLogger('chucky')

    #def __setattr__(self, name, value):
    #    try:
    #        if name == 'source':
    #            if value.node_type in ['Statement']:
    #                object.__setattr__(self, name, value)
    #            else:
    #                raise AttributeError()
    #        elif name == 'sink':
    #            if value.node_type in ['Statement']:
    #                object.__setattr__(self, name, value)
    #            else:
    #                raise AttributeError()
    #        else:
    #            object.__setattr__(self, name, value)
    #    except:
    #        raise AttributeError()


    def filter_by_sink(self, systems):
        node_selection = self.job.target.node_selection
        traversal = "statementToSinks('{}')".format(self.job.symbol_name)
        command = '.'.join([node_selection, traversal])
        accept = jutils.runGremlinCommands([command])
        self.logger.debug("Filter by sink(s) ({})".format(', '.join(accept)))
        results = []
        for source, symbol in systems:
            traversal = "statementToSinks('{}')".format(symbol)
            command = '.'.join([source.node_selection, traversal])
            sinks = jutils.runGremlinCommands([command])
            if not accept and not sinks:
                results.append((source, symbol))
            else:
                for sink in sinks:
                    if sink in accept:
                        #print 'Match', sink
                        results.append((source, symbol))
                        # one match suffices
                        break
        #print 'Done'
        if len(results) > 4:
            return results
        return systems

    def filter_by_source(self, systems):
        return systems
        #results = []
        #for source, sink in systems:
        #    results.append(sink)
        #return list(set(results))

    def _accepted_types(self):
        if self.types:
            return "[{}]".format(','.join(map(lambda x : "\'{}\'".format(x), self.types)))
        else:
            return "[]"
