from settings import Defaults

from joernInterface.JoernInterface import jutils
from joernInterface.nodes.Symbol import Symbol
from joernInterface.nodes.Statement import Statement
from joernInterface.indexLookup.ParameterLookup import ParameterLookup
from joernInterface.indexLookup.IdentifierDeclLookup import IdentifierDeclLookup
from joernInterface.indexLookup.CallExpressionLookup import CallExpressionLookup

SOURCE = Defaults.SOURCE
SINK = Defaults.SINK

class SliceSelector(object):
   
    def __init__(self, job):
        self.job = job

    def select_all(self):
        if self.job.symbol_type == 'CallExpression':
            return self._select_by_call()
        elif self.job.symbol_type == 'Parameter':
            return self._select_by_parameter()
        else:
            return []

    def _select_by_call(self):
        if self.job.category == SINK:
            return []
        else:
            calls = CallExpressionLookup.lookup(self.job.symbol_name)
            results = []
            for call in calls:
                source = call.statement()
                results.append((source, call.return_symbol()))
            return results
                
    def _select_by_parameter(self):
        if self.job.category == SINK:
            return []
        else:
            #params = ParameterLookup.lookup(self.job.symbol_name, self.job.symbol_decl_type)
            #results = []
            node_selection = "queryNodeIndex('type:Parameter')"
            traversal_steps = []
            traversal_steps.append("as('param')")
            traversal_steps.append("children().filter{{it.type == 'Identifier' && it.code == '{}'}}.back('param')".format(self.job.symbol_name))
            traversal_steps.append("children().filter{{it.type == 'ParameterType' && it.code == '{}'}}.back('param')".format(self.job.symbol_decl_type))
            traversal = '.'.join(traversal_steps)
            transform = "transform{ [it.id, it, it.defines().next().id, it.defines().next()] }"
            command = '.'.join([node_selection, traversal, transform])
            results = jutils.runGremlinCommands([command])
            return map(lambda x : (Statement(x[0], x[1].get_properties()), Symbol(x[2], x[3].get_properties())), results)
