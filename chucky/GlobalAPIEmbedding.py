
import os
from joerntools.APIEmbedder import APIEmbedder

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
        embedder = APIEmbedder()
        embedder.setOutputDirectory(self.embeddingdir)
        embedder.run()
        