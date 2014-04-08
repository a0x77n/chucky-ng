
import subprocess
import shlex
from joern_nodes import Function

class NearestNeighborSelector:
    
    def __init__(self, embeddingDir):
        self.bagdir = embeddingDir
    
    # FIXME: knn.JoernInterface offers a python-class so we don't 
    # have to make a call via the shell here
    
    """
    Determine k nearest neighbors for self.job.function.node_id
    by calling knn.JoernInterface
    """
    def getKNearestNeighbors(self, nodeId, k):
        command = 'knn.py -k {n_neighbors} --dirname {bagdir}'
        command = command.format(n_neighbors=k, bagdir=self.bagdir)
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