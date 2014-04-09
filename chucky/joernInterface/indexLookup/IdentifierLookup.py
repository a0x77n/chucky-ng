
from joernInterface.nodes.Identifier import Identifier
from joernInterface.JoernInterface import jutils

class IdentifierLookup:
    
    @staticmethod
    def lookup_parameter(code, decl_type = None):
        lucene_query = 'type:Parameter'
        traversal = 'ithChildren(\'1\').filter{{it.code == \'{}\'}}'.format(code)
        if decl_type:
            traversal += '.as(\'identifier\').identifierToType().filter{{it.code == \'{}\'}}.back(\'identifier\')'.format(decl_type)
        result = jutils.lookup(lucene_query, traversal)
        return map(lambda x : Identifier(x[0], x[1].get_properties()), result)

    @staticmethod
    def lookup_variable(code, decl_type = None):
        lucene_query = 'type:IdentifierDecl'
        traversal = 'ithChildren(\'1\').filter{{it.code == \'{}\'}}'.format(code)
        if decl_type:
            traversal += '.as(\'identifier\').identifierToType().filter{{it.code == \'{}\'}}.back(\'identifier\')'.format(decl_type)
        result = jutils.lookup(lucene_query, traversal)
        return map(lambda x : Identifier(x[0], x[1].get_properties()), result)
