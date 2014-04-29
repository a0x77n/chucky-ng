
import subprocess
import shlex
import os.path

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
    
    # FIXME: knn.py offers a python-class so we don't 
    # have to make a call via the shell here
    
    def _nearestNeighbors(self, entity, k, allEntities):
        
        limitFilename = self._createLimitFile(allEntities)
        
        nodeId = entity.getId()
        
        command = 'knn.py -k {n_neighbors} --dirname {bagdir} -l {limit}'
        command = command.format(n_neighbors=k, bagdir=self.cachedir, limit=limitFilename)
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
    
    def _createLimitFile(self, entities):
        filename = os.path.join(self.cachedir, 'limitfile')
        f = file(filename, 'w')
        f.writelines([str(e.getId()) + '\n' for e in entities] )
        f.close()
        return filename
    
            