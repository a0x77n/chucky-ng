from embedding.SallyDataDirectoryCreator import SallyDataDirectoryCreator
from embedding.SallyBasedEmbedder import SallyBasedEmbedder
from functionAnalyser.FunctionConditions import FunctionConditions


class ConditionEmbedder:
    
    def __init__(self, outputdir):
        
        self.outputdir = outputdir
                
        self.dataDirCreator = SallyDataDirectoryCreator(self.outputdir)
        self.embedder = SallyBasedEmbedder()
    
    def embed(self, functions, symbolName, symbolType):
        
        funcConditions = []
        for i, symbolUser in enumerate(functions, 1):
            
            x = FunctionConditions(symbolUser)
            x.setSymbolName(symbolName)
            x.setSymbolType(symbolType)
            funcConditions.append(x)
        
        self.dataDirCreator.create(funcConditions)
        self.embedder.embed(self.outputdir, 'bin')
