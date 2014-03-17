from demux_tool import DemuxTool
from joern_nodes import *
from expression_normalizer import ExpressionNormalizer
from symbol_tainter import SymbolTainter

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

    def _cache_api_symbols(self, function):
        for api_symbol in function.api_symbols():
            self.logger.debug('Caching %s %s.', function, api_symbol)
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

    def _relevant_conditions(self, symbol):
        taintset = SymbolTainter().taint(symbol)
        conditions = map(lambda x : x.traverse_to_using_conditions(), taintset)
        conditions = set([c for sublist in conditions for c in sublist])
        return conditions

    def _arguments(self, symbol):
        argset = symbol.arguments()
        return argset

    def _return_value(self, symbol):
        retset = []
        if symbol.is_callee():
            retset = symbol.assigns()
        return retset

    def _create_api_symbol_embedding(self):
        config = 'sally -q -c sally.cfg'
        config = config + ' --hash_file {}/feats.gz --vect_embed tfidf --tfidf_file {}/tfidf.fv'
        config = config.format(self.bagdir, self.bagdir)
        inputdir = '{}/data'
        inputdir = inputdir.format(self.bagdir)
        outfile = '{}/embedding.libsvm'
        outfile = outfile.format(self.bagdir)
        command = ' '.join([config, inputdir, outfile])
        subprocess.check_call(shlex.split(command))

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

    def _neighborhood(self):
        command = 'knn.py -k {n_neighbors} --dirname {bagdir}'
        command = command.format(n_neighbors=self.config.n, bagdir=self.bagdir)
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

    def _anomaly_rating(self):
        command = 'python ../python/anomaly_score.py -e -d {dir} -f {dir}/TOC'
        command = command.format(dir = self.exprdir)
        args = shlex.split(command)
        output = subprocess.check_output(args)

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

    def analyze(self, config):

        self.config = config

        # create working environment
        self.workingdir = tempfile.mkdtemp(dir=self.basedir)
        self.bagdir = os.path.join(self.workingdir, 'bag')
        self.exprdir = os.path.join(self.workingdir, 'exp')
        os.makedirs(os.path.join(self.bagdir, 'data'))
        expr_saver = DemuxTool(self.exprdir)

        self.logger.debug('Working directory is %s.', self.workingdir)

        # get all relatives (functions using the given symbol) 
        relatives = self.config.function.relatives(self.config.symbol)
        self.logger.debug(
                '%s functions using the symbol %s.',
                len(relatives), self.config.symbol)

        if len(relatives) < self.config.n:
            self.logger.warning('Configuration skipped.')
            shutil.rmtree(self.workingdir) # clean up
            return

        # extract and embedd api symbols for each relative
        for i, relative in enumerate(relatives, 1):
            self.logger.info('Processing %s (%s/%s).', relative, i, len(relatives))
            if relative.node_id not in self.api_symbol_cache.toc:
                self._cache_api_symbols(relative)
            self._load_from_api_symbol_cache(relative.node_id)
        self._load_toc()
        self._create_api_symbol_embedding()

        # process neighbors
        try:
            neighborhood = self._neighborhood()
            for i, neighbor in enumerate(neighborhood, 1):
                self.logger.info('Processing %s (%s/%s).', neighbor, i, len(neighborhood))
                symbol = neighbor.find_symbol_by_name(self.config.symbol.code)
                conditions = self._relevant_conditions(symbol)
                argset = self._arguments(symbol)
                retset = self._return_value(symbol)
                expr_normalizer = ExpressionNormalizer(argset, retset)
                for condition in conditions:
                    root = condition.childs()[0]
                    for expr in expr_normalizer.generate(root):
                        expr_saver.demux(neighbor.node_id, expr)
                if not conditions:
                    expr_saver.demux(neighbor.node_id, None)
            self._create_function_embedding()
            result = self._anomaly_rating()
            sorted_result = sorted(result.items(), key=lambda x: max(x[1])[0], reverse = True)
            for function, data in sorted_result:
                score, feat = max(data)
                for neighbor in neighborhood:
                    if neighbor.node_id == function:
                        print '{: 6.5f}\t{}\t{} ({})'.format(score, feat, neighbor, function)
        except subprocess.CalledProcessError as e:
            self.logger.error(e)
            self.logger.error('Do not clean up.')
        else:
            self.logger.debug('Cleaning up.')
            shutil.rmtree(self.workingdir) # clean up
