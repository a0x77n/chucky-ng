from embedding.SallyDataDirectoryCreator import SallyDataDirectoryCreator
from embedding.SallyBasedEmbedder import SallyBasedEmbedder
from sliceAnalyser.SliceConditions import SliceConditions
from settings import Defaults

SOURCE = Defaults.SOURCE
SINK = Defaults.SINK

class ConditionEmbedder:
    
    def __init__(self, outputdir):
        self.outputdir = outputdir
                
        self.dataDirCreator = SallyDataDirectoryCreator(self.outputdir)
        self.embedder = SallyBasedEmbedder()
    
    def embed(self, criterions, category = SINK):

        feature_providers = []
        
        for stmt, symb in criterions:
            feature_provider = SliceConditions(stmt, symb)
            feature_provider.category = category
            feature_providers.append(feature_provider)

        self.dataDirCreator.create(feature_providers)
        self.embedder.embed(self.outputdir, 'bin')
