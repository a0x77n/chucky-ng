
import os

"""
Interface to a Sally data directory that provides
caching to reduce the necessary number of database
queries.
"""
class SallyDataStore:
    def __init__(self, directory):
        self.cachedir = directory
        
        if not os.path.isdir(self.cachedir):
            path = os.path.join(directory, 'data')
            os.makedirs(path)
            open(os.path.join(directory, 'TOC'), 'w').close()
        
        self._openTOC()
    
    """
    Retrieves the filename of the data point
    for the given function. If necessary, the file
    will be created first.
    """
    def getDataFileForFunction(self, func):    
        
        if not self._isFunctionCached(func):
            self._cacheFunction(func)
            
        number = self.getDataPointNumberForFunction(func)
            
        return os.path.join(self.cachedir,
                            'data',
                            str(number))

    def getDataPointNumberForFunction(self, func):
        return self.toc[func.getKey()]
    
    
    def _openTOC(self):
        self.toc = dict()
        self.tocFile = open(os.path.join(self.cachedir, 'TOC'), 'r')
        number = 0
        for number, key in enumerate(self.tocFile):
            self.toc[int(key)] = number
        self._next_file_number = len(self.toc)
    
        self.tocFile.close()
        self.tocFile = open(os.path.join(self.cachedir, 'TOC'), 'a')
    
    def _cacheFunction(self, func):
        self._writeDataFile(func)
        self._writeToTOC(func)
    
    def _writeDataFile(self, func):
        
        filename = os.path.join(
                self.cachedir,
                'data',
                str(len(self.toc)))
        
        
        f = open(filename, 'w')   
        # FIXME: this can be made more generic:
        # func should just offer a get_features
        # function that we call here. Same goes
        # for the ids.
        
        for feature in func.getFeatures():
            f.write(str(feature) + '\n')
        f.close()
    
    def _writeToTOC(self, func):
        self.toc[func.getKey()] = len(self.toc)
        self.tocFile.write(str(func.getKey()) + '\n')
    
    def _isFunctionCached(self, func):
        return func.getKey() in self.toc
    