from joernInterface.JoernInterface import jutils
from joernInterface.nodes.Function import Function

class FunctionLookup:
    
    @staticmethod
    def lookup_functions_by_name(name):
        lucene_query = 'type:Function AND name:"{}"'.format(name)
        result = jutils.lookup(lucene_query)
        return map(lambda x : Function(x[0], x[1]), result)

    @staticmethod
    def lookup_functions_by_callee(code):
        lucene_query = 'type:Callee AND code:"{}"'.format(code)
        traversal = 'functions().dedup()'
        result = jutils.lookup(lucene_query, traversal)
        return map(lambda x : Function(x[0], x[1]), result)

    @staticmethod
    def lookup_functions_by_parameter(code, decl_type = None):
        lucene_query = 'type:Parameter'
        traversal = 'as(\'param\').children().filter{{it.type == \'Identifier\' && it.code == \'{}\'}}'.format(code)
        if decl_type:
            traversal = 'back(\'param\').children().filter{{it.type == \'ParameterType\' && it.code == \'{}\'}}'.format(code)
        traversal = 'ithChildren(\'1\').filter{{it.code == \'{}\'}}'.format(code)
        traversal += '.functions().dedup()'
        result = jutils.lookup(lucene_query, traversal)
        return map(lambda x : Function(x[0], x[1]), result)

    @staticmethod
    def lookup_functions_by_identifier_decl(code, decl_type = None):
        lucene_query = 'type:IdentifierDecl'
        traversal = 'as(\'decl\').children().filter{{it.type == \'Identifier\' && it.code == \'{}\'}}'.format(code)
        if decl_type:
            traversal = 'back(\'decl\').children().filter{{it.type == \'IdentifierDeclType\' && it.code == \'{}\'}}'.format(code)
        traversal += '.functions().dedup()'
        result = jutils.lookup(lucene_query, traversal)
        return map(lambda x : Function(x[0], x[1]), result)

    @staticmethod
    def lookup_functions_by_symbol(code):
        lucene_query = 'type:Symbol AND code:"{}"'.format(code)
        traversal = 'functions().dedup()'
        result = jutils.lookup(lucene_query, traversal)
        return map(lambda x : Function(x[0], x[1]), result)

    @staticmethod
    def lookup_all_functions():
        lucene_query = 'type:Function'
        result = jutils.lookup(lucene_query)
        return map(lambda x : Function(x[0], x[1]), result)
