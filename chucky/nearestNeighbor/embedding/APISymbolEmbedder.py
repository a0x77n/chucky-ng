from nearestNeighbor.embedding.SallyBasedEmbedder import SallyBasedEmbedder
from nearestNeighbor.embedding.SallyDataDirectoryCreator import SallyDataDirectoryCreator

import os
from nearestNeighbor.embedding.FunctionAPISymbols import FunctionAPISymbols

class APISymbolEmbedder:
    
    def __init__(self, workEnv):
        
        self.workEnv = workEnv
        self.basedir = workEnv.basedir
        self.outputdir = self.workEnv.bagdir    
        self.cachedir = os.path.join(self.basedir, 'cache')
                
        self.dataDirCreator = SallyDataDirectoryCreator(self.cachedir, self.outputdir)
        self.embedder = SallyBasedEmbedder()
    
    def embed(self, functions):
         
        functions = [FunctionAPISymbols(x) for x in functions]
        self.dataDirCreator.create(functions)
        self.embedder.embed(self.outputdir)