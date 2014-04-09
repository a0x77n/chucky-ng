from demux_tool import DemuxTool
from conditionNormalization.expression_normalizer import ExpressionNormalizer
from joernInterface.JoernInterface import jutils


import logging
import shlex
import subprocess

from nearestNeighbor.NearestNeighborSelector import NearestNeighborSelector
from ChuckyWorkingEnvironment import ChuckyWorkingEnvironment
from nearestNeighbor.FunctionSelector import FunctionSelector
from joernInterface.indexLookup.FunctionLookup import FunctionLookup
from conditionSelection.ConditionSelector import ConditionSelector
from conditionNormalization.ConditionNormalizer import ConditionNormalizer

class ChuckyEngine():

    def __init__(self, basedir):
        self.basedir = basedir
        self.logger = logging.getLogger('chucky')

        jutils.connectToDatabase()

    def analyze(self, job):

        self.job = job
        self.workingEnv = ChuckyWorkingEnvironment(self.basedir, self.logger)
        
        try:            
            nearestNeighbors = self._getKNearestNeighbors()
            
            if nearestNeighbors == []:
                self.logger.warning('Job skipped, no neighbors found')
                self.workingEnv.destroy()
                return

            self._calculateCheckModels(nearestNeighbors)
            result = self._anomaly_rating()
            self._outputResult(result, nearestNeighbors)

        except subprocess.CalledProcessError as e:
            self.logger.error(e)
            self.logger.error('Do not clean up.')
        else:
            self.logger.debug('Cleaning up.')
            self.workingEnv.destroy()

    """
    Determine the k nearest neighbors for the
    current job.
    """
    def _getKNearestNeighbors(self):
        
        symbol = self.job.getSymbol()
        self.knn = NearestNeighborSelector(self.workingEnv.basedir, self.workingEnv.bagdir)
        self.knn.setK(self.job.n_neighbors)
        
        entitySelector = FunctionSelector()
        symbolUsers = entitySelector.selectFunctionsUsingSymbol(symbol)
        
        return self.knn.getNearestNeighbors(self.job.function, symbolUsers)
    
    def _calculateCheckModels(self, symbolUsers):
        
        expr_saver = DemuxTool(self.workingEnv.exprdir)

        for i, symbolUser in enumerate(symbolUsers, 1):
            self.logger.info('Processing %s (%s/%s).', symbolUser, i, len(symbolUsers))            
            
            symbolName = self.job.getSymbolName()
            symbolType = self.job.getSymbolType()
            conditions = ConditionSelector().getRelevantConditions(symbolUser, symbolName, symbolType)
            normalizedConditions = ConditionNormalizer().normalize(conditions, symbolUser, symbolName, symbolType)
            
            # Embed using demux. Replace by embed using embedding module
            
            for condition in normalizedConditions:
                for expr in condition:
                    expr_saver.demux(symbolUser.node_id, expr)
            if not conditions:
                # empty feature hack
                expr_saver.demux(symbolUser.node_id, None)

        self._create_function_embedding()
    

    def _create_function_embedding(self):
        config = 'sally -q -c sally.cfg'
        config = config + ' --hash_file {}/feats.gz --vect_embed bin'
        config = config.format(self.workingEnv.exprdir)
        inputdir = '{}/data'
        inputdir = inputdir.format(self.workingEnv.exprdir)
        outfile = '{}/embedding.libsvm'
        outfile = outfile.format(self.workingEnv.exprdir)
        command = ' '.join([config, inputdir, outfile])
        subprocess.check_call(shlex.split(command))


    """
    Determine anomaly score.
    """
    def _anomaly_rating(self):
        command = "echo %d |" % (self.job.function.node_id)
        command += 'python ../python/anomaly_score.py -e -d {dir}'
        command = command.format(dir = self.workingEnv.exprdir)
        output = subprocess.check_output(command, shell=True)

        results = {}
        for line in output.strip().split('\n'):
            if line.startswith('#'):
                func = line[3:]
                results[func] = []
            else:
                score, feat = line.split(' ', 1)
                results[func].append((float(score), feat))
                self.logger.debug('%s %+1.5f %s.', func, float(score), feat)
        return results

    def _outputResult(self, result, _nearestNeighbors):
        
        sorted_result = sorted(result.items(), key = lambda x : max(x[1])[0], reverse = True)
        for i, (function, data) in enumerate(sorted_result, 1):
            score, feat = max(data)
            for neighbor in _nearestNeighbors:
                if neighbor.node_id == function:
                    print '{:>3} {:< 6.5f}\t{:30}\t{:10}\t{}'.format(i, score, neighbor.name, function, feat)
    
