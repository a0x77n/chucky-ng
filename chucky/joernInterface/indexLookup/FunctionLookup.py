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
        traversal = 'ithChildren(\'1\').filter{{it.code == \'{}\'}}'.format(code)
        if decl_type:
            traversal += '.identifierToType().filter{{it.code == \'{}\'}}'.format(decl_type)
        traversal += '.functions().dedup()'
        result = jutils.lookup(lucene_query, traversal)
        return map(lambda x : Function(x[0], x[1]), result)

    @staticmethod
    def lookup_functions_by_variable(code, decl_type = None):
        lucene_query = 'type:IdentifierDecl'
        traversal = 'ithChildren(\'1\').filter{{it.code == \'{}\'}}'.format(code)
        if decl_type:
            traversal += '.identifierToType().filter{{it.code == \'{}\'}}'.format(decl_type)
        traversal += '.functions().dedup()'
        result = jutils.lookup(lucene_query, traversal)
        return map(lambda x : Function(x[0], x[1]), result)

    @staticmethod
    def lookup_functions_by_symbol(code):
        lucene_query = 'type:Symbol AND code:"{}"'.format(code)
        traversal = 'functions().dedup()'
        result = jutils.lookup(lucene_query, traversal)
        return map(lambda x : Function(x[0], x[1]), result)
