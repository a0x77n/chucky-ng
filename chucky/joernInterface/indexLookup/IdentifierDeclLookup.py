
from joernInterface.nodes.IdentifierDecl import IdentifierDecl
from joernInterface.JoernInterface import jutils

class IdentifierDeclLookup:
    
    @staticmethod
    def lookup(code, decl_type = None, function_id = None):
        if function_id:
            lucene_query = 'type:IdentifierDecl AND functionId:{}'.format(functionId)
        else:
            lucene_query = 'type:IdentifierDecl'
        traversal_steps = []
        traversal_steps.append('as(\'identifier\')')
        traversal_steps.append('ithChildren(\'1\').filter{{it.code == \'{}\'}}'.format(code))
        traversal_steps.append('back(\'identifier\')')
        if decl_type:
            traversal_steps.append('ithChildren(\'0\').filter{{it.code == \'{}\'}}'.format(decl_type))
            traversal_steps.append('back(\'identifier\')')
        traversal = '.'.join(traversal_steps)

        result = jutils.lookup(lucene_query, traversal)
        return map(lambda x : IdentifierDecl(x[0], x[1].get_properties()), result)
