from nearestNeighbor.FunctionSelector import FunctionSelector
from nearestNeighbor.APISymbolEmbedder import APISymbolEmbedder
import os

class GlobalAPIEmbedding():
    def __init__(self, cachedir):
        
        self.cachedir = cachedir
        self.embeddingdir = cachedir
        self.embeddingFilename = 'embedding.libsvm'
        
        if self._embeddingExists():
            self._loadEmbedding()
        else:
            self._createEmbedding()
    
    def _embeddingExists(self):
        return os.path.exists(self.embeddingFilename)
    
    def _createEmbedding(self):
        
        entitySelector = FunctionSelector()
        functions = entitySelector.selectAllFunctions()
        embedder = APISymbolEmbedder(None, self.embeddingdir)
        embedder.embed(functions)