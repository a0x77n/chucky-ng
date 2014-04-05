from demux_tool import DemuxTool
from joern_nodes import *
from expression_normalizer import ExpressionNormalizer
from symbol_tainter import SymbolTainter
from jutils import jutils

import logging
import tempfile
import sys
import os
import shutil
import shlex
import subprocess

class ChuckyEngine():

    def __init__(self, basedir):
        self.basedir = basedir
        self.cachedir = os.path.join(self.basedir, 'cache')
        self.api_symbol_cache = DemuxTool(self.cachedir)
        self.logger = logging.getLogger('chucky')

        jutils.connectToDatabase()

    def analyze(self, config):

        self.config = config
        self._createWorkingEnvironment()
        
        try:            
            neighborhood = self._getKNearestNeighbors()
            
            if neighborhood == []:
                self.logger.warning('Configuration skipped.')
                shutil.rmtree(self.workingdir) # clean up
                return

            self._calculateCheckModels(neighborhood)
            result = self._anomaly_rating()
            self._outputResult(result, neighborhood)

        except subprocess.CalledProcessError as e:
            self.logger.error(e)
            self.logger.error('Do not clean up.')
        else:
            self.logger.debug('Cleaning up.')
            shutil.rmtree(self.workingdir)


    """
    Create a temporary directory to store embeddings.
    """
    def _createWorkingEnvironment(self):
        
        self.workingdir = tempfile.mkdtemp(dir=self.basedir)
        self.bagdir = os.path.join(self.workingdir, 'bag')
        self.exprdir = os.path.join(self.workingdir, 'exp')
        os.makedirs(os.path.join(self.bagdir, 'data'))
        self.logger.debug('Working directory is %s.', self.workingdir)

    """
    Determine the k nearest neighbors for the
    current (function, symbol)-pair.
    """

    def _getKNearestNeighbors(self):
        
        # get all relatives (functions using the given target) 
        relatives = self._relative_functions()
        
        self.logger.debug(
                '%s functions using the symbol %s.',
                len(relatives), self.config.target_name)

        if len(relatives) < self.config.n_neighbors:
            return []

        # write API symbols to data directory
        for i, relative in enumerate(relatives, 1):
            self.logger.info('Processing %s (%s/%s).', relative, i, len(relatives))
            if relative.node_id not in self.api_symbol_cache.toc:
                self._cache_api_symbols(relative)
            self._load_from_api_symbol_cache(relative.node_id)
        self._load_toc()

        # create embedding from data directory
        self._create_api_symbol_embedding()

        return self._neighborhood()

    """
    Determine functions using the same symbol as the
    function of interest
    """
    def _relative_functions(self):
        if self.config.target_type == 'Parameter':
            relatives = Function.lookup_functions_by_parameter(
                    self.config.target_name,
                    self.config.target_decl_type)
        elif self.config.target_type == 'Variable':
            relatives = Function.lookup_functions_by_variable(
                    self.config.target_name,
                    self.config.target_decl_type)
        elif self.config.target_type == 'Callee':
            relatives = Function.lookup_functions_by_callee(
                    self.config.target_name)
        
        return relatives

    def _cache_api_symbols(self, function):
        for api_symbol in function.api_symbol_nodes():
            self.logger.debug('Caching %s %s.', function, api_symbol.code)
            self.api_symbol_cache.demux(function.node_id,  api_symbol.code)

    def _load_from_api_symbol_cache(self, function):
        number = self.api_symbol_cache.toc[function]
        source = os.path.join(self.cachedir, 'data', str(number))
        target = os.path.join(self.bagdir, 'data', str(number))
        os.symlink(os.path.abspath(source),os.path.abspath(target))

    def _load_toc(self):
        source = os.path.join(self.cachedir, 'TOC')
        target = os.path.join(self.bagdir, 'TOC')
        os.symlink(os.path.abspath(source),os.path.abspath(target))
    
    def _create_api_symbol_embedding(self):
        config = 'sally -q -c sally.cfg '
        config = config + ' --hash_file {}/feats.gz --vect_embed=cnt'
        config = config.format(self.bagdir, self.bagdir)
        inputdir = '{}/data/'
        inputdir = inputdir.format(self.bagdir)
        outfile = '{}/embedding.libsvm'
        outfile = outfile.format(self.bagdir)
        command = ' '.join([config, inputdir, outfile])
        subprocess.check_call(shlex.split(command))

    """
    Determine k nearest neighbors for self.config.function.node_id
    by calling knn.py
    """
    def _neighborhood(self):
        command = 'knn.py -k {n_neighbors} --dirname {bagdir}'
        command = command.format(n_neighbors=self.config.n_neighbors, bagdir=self.bagdir)
        args = shlex.split(command)
        knn = subprocess.Popen(
                args,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        neighbors = []
        (stdout, stderr) = knn.communicate(str(self.config.function.node_id))
        returncode = knn.poll()
        if returncode:
            raise subprocess.CalledProcessError(returncode, command, stderr)
        for neighbor in stdout.strip().split('\n'):
            neighbors.append(Function(neighbor))
        return neighbors
    
    def _calculateCheckModels(self, neighborhood):
        
        expr_saver = DemuxTool(self.exprdir)

        for i, neighbor in enumerate(neighborhood, 1):
            self.logger.info('Processing %s (%s/%s).', neighbor, i, len(neighborhood))
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
        if self.config.target_type == 'Callee':
            taintset = set()
            callees = function.lookup_callees_by_name(self.config.target_name)
            for callee in callees:
                for argument in callee.arguments():
                    taintset = taintset | symbol_tainter.taint_upwards(argument)
                for return_value in callee.return_value():
                    taintset = taintset | symbol_tainter.taint_upwards(return_value)
        else:
            symbol = function.lookup_symbol_by_name(self.config.target_name)
            taintset = symbol_tainter.taint(symbol)
        conditions = map(lambda x : x.traverse_to_using_conditions(), taintset)
        conditions = set([c for sublist in conditions for c in sublist])
        return conditions

    def _arguments(self, function):
        if self.config.target_type == 'Callee':
            callees = function.lookup_callees_by_name(self.config.target_name)
            arguments = map(lambda x : x.arguments(), callees)
            arguments = [arg for sublist in arguments for arg in sublist]
            return set(arguments)
        else:
            return set()

    def _return_value(self, function):
        if self.config.target_type == 'Callee':
            callees = function.lookup_callees_by_name(self.config.target_name)
            arguments = map(lambda x : x.return_value(), callees)
            arguments = [arg for sublist in arguments for arg in sublist]
            return set(arguments)
        else:
            return set()

    def _create_function_embedding(self):
        config = 'sally -q -c sally.cfg'
        config = config + ' --hash_file {}/feats.gz --vect_embed bin'
        config = config.format(self.exprdir)
        inputdir = '{}/data'
        inputdir = inputdir.format(self.exprdir)
        outfile = '{}/embedding.libsvm'
        outfile = outfile.format(self.exprdir)
        command = ' '.join([config, inputdir, outfile])
        subprocess.check_call(shlex.split(command))


    """
    Determine anomaly score.
    """
    def _anomaly_rating(self):
        command = "echo %d |" % (self.config.function.node_id)
        command += 'python ../python/anomaly_score.py -e -d {dir}'
        command = command.format(dir = self.exprdir)
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

    def _outputResult(self, result, neighborhood):
        
        sorted_result = sorted(result.items(), key = lambda x : max(x[1])[0], reverse = True)
        for i, (function, data) in enumerate(sorted_result, 1):
            score, feat = max(data)
            for neighbor in neighborhood:
                if neighbor.node_id == function:
                    print '{:>3} {:< 6.5f}\t{:30}\t{:10}\t{}'.format(i, score, neighbor.name, function, feat)
    
