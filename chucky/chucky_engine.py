from settings import Defaults
from ChuckyWorkingEnvironment import ChuckyWorkingEnvironment
from joernInterface.JoernInterface import jutils
from functionAnalyser.FunctionEmbedder import ConditionEmbedder as FunctionEmbedder
from functionAnalyser.FunctionSelector import FunctionSelector
from GlobalAPIEmbedding import GlobalAPIEmbedding
from nearestNeighbor.NearestNeighborSelector import NearestNeighborSelector
from sliceAnalyser.SliceEmbedder import ConditionEmbedder as SliceEmbedder
from sliceAnalyser.SliceSelector import SliceSelector
from sliceAnalyser.SliceFilter import SliceFilter

from job.chucky_ng.Job import ChuckyJob as SlicingJob

import os
import logging
import subprocess

SOURCE = Defaults.SOURCE
SINK = Defaults.SINK

class ChuckyEngine():

    def __init__(self, basedir):
        self.basedir = basedir
        self.logger = logging.getLogger('chucky')

        jutils.connectToDatabase()

    """
    Analyze the given job. This involves three steps:
       1. Select a neighorhood (this depends on the type of the job)
       2. Embed the neighorhood
       3. Find anomalies in the embedding
    """

    def analyze(self, job):

        self.job = job
        self.workingEnv = ChuckyWorkingEnvironment(self.basedir, self.logger)
        
        try:            
            neighborhood = self._get_neighborhood()

            if neighborhood:

                n = len(neighborhood)
                self.logger.info('{} neighbors selected'.format(n))
                for i, neighbor in enumerate(neighborhood, 1):
                    if type(self.job) is SlicingJob:
                        self.logger.debug('{:>2}/{} {} ({})'.format(i, n, neighbor, neighbor[0].function()))
                    else:
                        self.logger.debug('{:>2}/{} {}'.format(i, n, neighbor))

                self._embed_neighborhood(neighborhood)
                result = self._anomaly_rating()
                self._outputResult(result)

            else:
                self.logger.warning('Job skipped, no neighbors found')


        except Exception as e:
            self.logger.error(e)
            self.logger.error('Do not clean up.')
        else:
            self.logger.debug('Cleaning up.')
            self.workingEnv.destroy()

    """
    Select neighbors (i.e functions or statements operating in a similar context)
    """

    def _get_neighborhood(self):

        if type(self.job) is SlicingJob:
            selector = SliceSelector(self.job)
            slices = selector.select_all()
            #return slices
            filter = SliceFilter(self.job)
            return filter.filter(slices)
        else:
            selector = FunctionSelector(self.job)
            functions = selector.select_all()
            #return functions
            GlobalAPIEmbedding(self.workingEnv.cachedir)
            self.knn = NearestNeighborSelector(self.workingEnv.basedir, self.workingEnv.bagdir)
            self.knn.setK(self.job.n_neighbors)
            return self.knn.getNearestNeighbors(self.job.target, functions)

    """
    Embed selected neighors.
    """

    def _embed_neighborhood(self, neighborhood):

        if type(self.job) is SlicingJob:
            embedder = SliceEmbedder(self.workingEnv.exprdir)
            embedder.embed(neighborhood, self.job.category)
        else:
            embedder = FunctionEmbedder(self.workingEnv.exprdir)
            embedder.embed(neighborhood, self.job.symbol_name, self.job.symbol_type)

    """
    Determine anomaly score.
    TODO 
    """

    def _anomaly_rating(self):

        dirname = os.path.dirname(os.path.dirname(__file__))
        command = "echo %d | " % (self.job.target.node_id)
        command += 'python {dirname}/python/anomaly_score.py -d {dir}'
        command = command.format(
                dirname = dirname,
                dir = self.workingEnv.exprdir)
        output = subprocess.check_output(command, shell = True)

        results = []
        for line in output.strip().split('\n'):
            score, feat = line.split(' ', 1)
            results.append((float(score), feat))
            #self.logger.debug('{:< 6.5f}\t{}'.format(float(score), feat))

        return results

    """
    Print results
    """

    def _outputResult(self, result):

        score, feat = max(result)
        self.logger.debug('{:< 6.5f}\t{}\t{}\t{}'.format(score, self.job.function, self.job.function.node_id, feat))
        print '{:< 6.5f}\t{:40s}\t{:10}\t{}'.format(score, self.job.function, self.job.function.node_id, feat)
