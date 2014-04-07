
import tempfile
import os.path

class ChuckyWorkingEnvironment():
    
    def __init__(self, basedir, logger):
        
        self.basedir = basedir
        self.logger = logger
        
        self.workingdir = tempfile.mkdtemp(dir=self.basedir)
        self.bagdir = os.path.join(self.workingdir, 'bag')
        self.exprdir = os.path.join(self.workingdir, 'exp')
        os.makedirs(os.path.join(self.bagdir, 'data'))
        self.logger.debug('Working directory is %s.', self.workingdir)
    
    def destroy(self):
        pass
        # shutil.rmtree(self.workingdir) # clean up