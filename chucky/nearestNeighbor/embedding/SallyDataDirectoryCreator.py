from nearestNeighbor.embedding.SallyDataStore import SallyDataStore
import os

class SallyDataDirectoryCreator:
    
    def __init__(self, cacheDir, outputDir):
        self.cachedir = cacheDir
        self.outputdir = outputDir
        
        self.dataStore = SallyDataStore(self.cachedir)
        self._initializeOutputDir()
 
    """
    Create a sally data directory for the given functions
    and write it to outputdir. This data directory can then
    be embedded using a SallyBasedEmbedder.
    """
    
    def create(self, functions):

        for func in functions:
            # self.logger.info('Processing %s (%s/%s).', func, i, len(functions))
            
            filename = self.dataStore.getDataFileForFunction(func)
            number = self.dataStore.getDataPointNumberForFunction(func)
            self._addDataPoint(filename, number, func)
            
        self._closeOutputdir()
    
    def _addDataPoint(self, filename, number, func):
        
        source = filename
        target = os.path.join(self.outputdir, 'data', str(len(self.toc)))
        os.symlink(os.path.abspath(source),os.path.abspath(target))
    
        self.tocFile.write(str(func.getKey()) + '\n')
        self.toc[func.getKey()] = len(self.toc)
    
    def _initializeOutputDir(self):

        self.toc = dict()
        self.tocFile = open( os.path.join(self.outputdir, 'TOC'), 'w')
    
    def _closeOutputdir(self):
        self.tocFile.close()
        