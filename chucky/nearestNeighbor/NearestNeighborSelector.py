
import os.path
from joerntools.KNN import KNN
from joernInterface.nodes.Function import Function

"""
Employs an embedder to first embed a set of entities (e.g., functions)
and then determine the k nearest neighbors to a given entity.
"""
class NearestNeighborSelector:
    
    """
    @param basedir: directory for temporary files. We assume
                    that the cache lives at $basedir/cache
    
    @param embeddingDir: the directory to store the embedding.    
    """
    
    def __init__(self, basedir, embeddingDir):
        self.embeddingDir = embeddingDir
        self.k = 10
        self.cachedir = os.path.join(basedir, "cache")
    
    def setK(self, k):
        self.k = k
    
    """
    Get nearest neighbors of entity in set of allEntities
    """
    def getNearestNeighbors(self, entity, allEntities):
        
        if len(allEntities) < self.k:
            return []

        return self._nearestNeighbors(entity, self.k, allEntities)
    
    
    def _nearestNeighbors(self, entity, k, allEntities):
        
        limitFilename = self._createLimitFile(allEntities)
        
        nodeId = entity.getId()
        
        f = file(limitFilename, 'r')
        limit = [l.rstrip() for l in f.readlines()]
        f.close()
        
        knn = KNN()
        knn.setEmbeddingDir(self.cachedir)
        knn.setK(k)
        knn.setLimitArray(limit)
        knn.setNoCache(False)
        knn.initialize()
        
        ids = knn.getNeighborsFor(str(nodeId))
        return [Function(i) for i in ids]
    
    
    def _createLimitFile(self, entities):
        filename = os.path.join(self.cachedir, 'limitfile')
        f = file(filename, 'w')
        f.writelines([str(e.getId()) + '\n' for e in entities] )
        f.close()
        return filename
    
            
