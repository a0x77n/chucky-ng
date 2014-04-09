
import subprocess
import shlex
import os.path

from nearestNeighbor.APISymbolEmbedder import APISymbolEmbedder
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
        cachedir = os.path.join(basedir, "cache")
        
        self.embedder = APISymbolEmbedder(cachedir, embeddingDir)
        
    
    def setEmbedder(self, embedder):
        self.embedder = embedder
    
    
    def setK(self, k):
        self.k = k
    
    """
    Get nearest neighbors of entity in set of allEntities
    """
    def getNearestNeighbors(self, entity, allEntities):
        
        if len(allEntities) < self.k:
            return []

        self.embedder.embed(allEntities)
        return self._nearestNeighbors(entity, self.k)
    
    # FIXME: knn.py offers a python-class so we don't 
    # have to make a call via the shell here
    
    def _nearestNeighbors(self, entity, k):
        
        nodeId = entity.getId()
        
        command = 'knn.py -k {n_neighbors} --dirname {bagdir}'
        command = command.format(n_neighbors=k, bagdir=self.embeddingDir)
        args = shlex.split(command)
        knn = subprocess.Popen(
                args,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        neighbors = []
        (stdout, stderr) = knn.communicate(str(nodeId))
        returncode = knn.poll()
        if returncode:
            raise subprocess.CalledProcessError(returncode, command, stderr)
        for neighbor in stdout.strip().split('\n'):
            neighbors.append(Function(neighbor))
        return neighbors
