from demux_tool import DemuxTool
from expression_normalizer import ExpressionNormalizer
from symbol_tainter import SymbolTainter
from joernInterface.JoernInterface import jutils


import logging
import shlex
import subprocess

from nearestNeighbor.NearestNeighborSelector import NearestNeighborSelector
from ChuckyWorkingEnvironment import ChuckyWorkingEnvironment

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
        return self.knn.getNearestNeighbors(self.job.function.node_id, symbol)
    
    def _calculateCheckModels(self, nearestNeighbors):
        
        expr_saver = DemuxTool(self.workingEnv.exprdir)

        for i, neighbor in enumerate(nearestNeighbors, 1):
            self.logger.info('Processing %s (%s/%s).', neighbor, i, len(nearestNeighbors))
            conditions = self._relevant_conditions(neighbor)
            argset = self._arguments(neighbor)
            retset = self._return_value(neighbor)
            expr_normalizer = ExpressionNormalizer(argset, retset)
            
            
            for condition in conditions:
                root_expr = condition.children()[0]
                self.logger.debug('Normalizing condition ( {} ) ({})'.format(root_expr, root_expr.node_id))
                for expr in expr_normalizer.normalize_expression(root_expr):
                    expr_saver.demux(neighbor.node_id, expr)
            if not conditions:
                # empty feature hack
                expr_saver.demux(neighbor.node_id, None)

        self._create_function_embedding()

    def _relevant_conditions(self, function):
        symbol_tainter = SymbolTainter()
        if self.job.getSymbolType() == 'Callee':
            taintset = set()
            callees = function.lookup_callees_by_name(self.job.getSymbolName())
            for callee in callees:
                for argument in callee.arguments():
                    taintset = taintset | symbol_tainter.taint_upwards(argument)
                for return_value in callee.return_value():
                    taintset = taintset | symbol_tainter.taint_upwards(return_value)
        else:
            symbol = function.lookup_symbol_by_name(self.job.getSymbolName())
            taintset = symbol_tainter.taint(symbol)
        conditions = map(lambda x : x.traverse_to_using_conditions(), taintset)
        conditions = set([c for sublist in conditions for c in sublist])
        return conditions

    """
    Get arguments of function
    """
    def _arguments(self, function):
        if self.job.getSymbolType() == 'Callee':
            callees = function.lookup_callees_by_name(self.job.getSymbolName())
            arguments = map(lambda x : x.arguments(), callees)
            arguments = [arg for sublist in arguments for arg in sublist]
            return set(arguments)
        else:
            return set()

    def _return_value(self, function):
        if self.job.getSymbolType() == 'Callee':
            callees = function.lookup_callees_by_name(self.job.getSymbolName())
            arguments = map(lambda x : x.return_value(), callees)
            arguments = [arg for sublist in arguments for arg in sublist]
            return set(arguments)
        else:
            return set()

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
    
