from joernInterface.JoernInterface import jutils
import os
import os.path

import logging
import subprocess

from nearestNeighbor.NearestNeighborSelector import NearestNeighborSelector
from ChuckyWorkingEnvironment import ChuckyWorkingEnvironment
from nearestNeighbor.FunctionSelector import FunctionSelector
from conditionAnalyser.ConditionEmbedder import ConditionEmbedder

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
            self._outputResult(result)

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
        
        embedder = ConditionEmbedder(self.workingEnv.exprdir)
        symbolName = self.job.getSymbolName()
        symbolType = self.job.getSymbolType()
        embedder.embed(symbolUsers, symbolName, symbolType)


    """
    Determine anomaly score.
    """
    def _anomaly_rating(self):
        dirname = os.path.dirname(os.path.dirname(__file__))
        command = "echo %d | " % (self.job.function.node_id)
        command += 'python {dirname}/python/anomaly_score.py -d {dir}'
        command = command.format(
                dirname = dirname,
                dir = self.workingEnv.exprdir)
        output = subprocess.check_output(command, shell = True)

        results = []
        for line in output.strip().split('\n'):
            score, feat = line.split(' ', 1)
            results.append((float(score), feat))
            self.logger.debug('%+1.5f %s.', float(score), feat)
        return results

    def _outputResult(self, result):
        
        score, feat = max(result)
        print '{:< 6.5f}\t{:40}\t{:10}\t{}'.format(score, self.job.function, self.job.function.node_id, feat)
    
