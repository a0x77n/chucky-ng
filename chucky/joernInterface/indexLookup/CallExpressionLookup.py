from joernInterface.JoernInterface import jutils
from joernInterface.nodes.CallExpression import CallExpression

class CallExpressionLookup:
    
    @staticmethod
    def lookup(code, function_id = None):
        if function_id:
            lucene_query = 'type:CallExpression AND functionId:{}'.format(function_id)
        else:
            lucene_query = 'type:CallExpression'
        traversal_steps = []
        traversal_steps.append('as(\'callExpression\')')
        traversal_steps.append('ithChildren(\'0\').filter{{it.code == \'{}\'}}'.format(code))
        traversal_steps.append('back(\'callExpression\')')
        traversal = '.'.join(traversal_steps)
        results = jutils.lookup(lucene_query, traversal = traversal)
        return map(lambda x : CallExpression(x[0], x[1].get_properties()), results)
