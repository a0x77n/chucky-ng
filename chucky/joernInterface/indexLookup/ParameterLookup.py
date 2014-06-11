
from joernInterface.nodes.Parameter import Parameter
from joernInterface.JoernInterface import jutils

class ParameterLookup:
    
    @staticmethod
    def lookup(code, decl_type = None, function_id = None):
        if function_id:
            lucene_query = 'type:Parameter AND functionId:{}'.format(function_id)
        else:
            lucene_query = 'type:Parameter'
        traversal_steps = []
        traversal_steps.append('as(\'parameter\')')
        traversal_steps.append('ithChildren(\'1\').filter{{it.code == \'{}\'}}'.format(code))
        traversal_steps.append('back(\'parameter\')')
        if decl_type:
            traversal_steps.append('ithChildren(\'0\').filter{{it.code == \'{}\'}}'.format(decl_type))
            traversal_steps.append('back(\'parameter\')')
        traversal = '.'.join(traversal_steps)

        result = jutils.lookup(lucene_query, traversal)
        return map(lambda x : Parameter(x[0], x[1].get_properties()), result)
