from joern.all import JoernSteps

class jutils:
    joern = JoernSteps()

    @staticmethod
    def connectToDatabase():
        jutils.joern.connectToDatabase()
    
    @staticmethod
    def lookup(lucene_query, traversal = None, projection = None):
        node_selection = "queryNodeIndex('{}')".format(lucene_query)
        return jutils.raw_lookup(node_selection, traversal, projection)

    @staticmethod
    def raw_lookup(node_selection, traversal=None, projection=None):
        if not projection:
            attributes = ['it.id', 'it']
        else:
            f = lambda x : 'it.{}'.format(x)
            attributes = map(f, projection)
        transform = "transform{{ [ {} ] }}".format(', '.join(attributes))

        if not traversal:
            command = '.'.join([node_selection, transform])
        else:
            command = '.'.join([node_selection, traversal, transform])
        
        print command
        return jutils.joern.runGremlinQuery(command)

