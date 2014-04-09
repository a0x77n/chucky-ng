from embedding.SallyBasedEmbedder import SallyBasedEmbedder
from embedding.SallyDataDirectoryCreator import SallyDataDirectoryCreator

from embedding.FunctionAPISymbols import FunctionAPISymbols

class APISymbolEmbedder:
    
    def __init__(self, cachedir, outputdir):
        
        self.outputdir = outputdir
                
        self.dataDirCreator = SallyDataDirectoryCreator(self.outputdir, cachedir)
        self.embedder = SallyBasedEmbedder()
    
    def embed(self, functions):
         
        functions = [FunctionAPISymbols(x) for x in functions]
        self.dataDirCreator.create(functions)
        self.embedder.embed(self.outputdir)