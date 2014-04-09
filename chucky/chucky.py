#!/usr/bin/env python2

from job.JobGenerator import JobGenerator
from chucky_engine import ChuckyEngine

import logging
import argparse
import os

DESCRIPTION = """Chucky analyzes functions for anomalies. To this end, the
usage of symbols used by a function is analyzed by comparing the checks
used in conjunction with the symbol with those used in similar functions."""
DEFAULT_N = 30
MIN_N = 5
DEFAULT_DIR = ".chucky"

def n_neighbors(value):
    n = int(value)
    if n < MIN_N:
        error_message = "N_NEIGHBORS must be greater than {}".format(MIN_N)
        raise argparse.ArgumentError(error_message)
    else:
        return n

class Chucky():

    def __init__(self):
        self._init_arg_parser()
        self.args = self.arg_parser.parse_args()
        self._config_logger()
        self._create_chucky_dir()
        self.job_generator = JobGenerator(
                identifier = self.args.identifier,
                identifier_type = self.args.identifier_type,
                n_neighbors = self.args.n_neighbors,
                limit = self.args.limit)
        self.engine = ChuckyEngine(self.args.chucky_dir)

    def _init_arg_parser(self):
        self.arg_parser = argparse.ArgumentParser(description=DESCRIPTION)
        self.arg_parser.add_argument(
                'identifier',
                help = """The name of the identifier 
                (function name or source/sink name)""")
        self.arg_parser.add_argument(
                '-i', '--identifier-type',
                action = 'store',
                default = 'function',
                choices = ['function','callee', 'parameter', 'variable'],
                help = """The type of identifier the positional argument
                `identifier` refers to.""")
        self.arg_parser.add_argument(
                '-n', '--n-neighbors',
                action = 'store',
                default = DEFAULT_N,
                type = n_neighbors,
                help = """Number of neighbours to consider for neighborhood
                discovery.""")
        self.arg_parser.add_argument(
                '-c', '--chucky-dir',
                action = 'store',
                default = DEFAULT_DIR,
                help = """The directory holding chucky's data such as cached
                symbol embeddings and possible annotations of sources and
                sinks.""")
        self.arg_parser.add_argument(
                '--interactive',
                action = 'store_true',
                default = False,
                help = """Enable interactive mode.""")
        
        self.arg_parser.add_argument(
                '-l', '--limit',
                action = 'store',
                default = None,
                type = str,
                help = """Limit analysis to functions with given name""")
        
        group = self.arg_parser.add_mutually_exclusive_group()
        group.add_argument(
                '-d', '--debug',
                action = 'store_const',
                const = logging.DEBUG,
                dest = 'logging_level',
                default = logging.WARNING,
                help = """Enable debug output.""")
        group.add_argument(
                '-v', '--verbose',
                action = 'store_const',
                const = logging.INFO,
                dest = 'logging_level',
                default = logging.WARNING,
                help = """Increase verbosity.""")
        group.add_argument(
                '-q', '--quiet',
                action = 'store_const',
                const = logging.ERROR,
                dest = 'logging_level',
                default = logging.WARNING,
                help = """Be quiet during processing.""")

    def _create_chucky_dir(self):
        basedir = self.args.chucky_dir
        if not os.path.isdir(basedir):
            self.logger.debug('Creating directory %s.', os.path.abspath(basedir))
            os.makedirs(basedir)
        self.logger.info('Base directory is %s.', os.path.abspath(basedir))

    
    def _config_logger(self):
        self.logger = logging.getLogger('chucky')
        self.logger.setLevel('DEBUG')
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.args.logging_level)
        file_handler = logging.FileHandler('chucky.log', 'w+')
        file_handler.setLevel('DEBUG')
        #console_formatter = logging.Formatter('%(message)s')
        console_formatter = logging.Formatter('[%(levelname)s] %(message)s')
        file_formatter = logging.Formatter('[%(levelname)s] %(message)s')
        console_handler.setFormatter(console_formatter)
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    """
    Generates Jobs (list of ChuckyJobs) and asks
    the engine to perform an analysis for each job.
    """

    def execute(self):
        jobs = self.job_generator.generate()
        numberOfJobs = len(jobs)
        
        for i, job in enumerate(jobs, 1):
            print 'Job ({}/{}): {}'.format(
                    i,
                    numberOfJobs,
                    job)
            if self.args.interactive:
                choice = raw_input('Run job ([yes]/no/quit)? ').lower()
                if choice in ['n', 'no']:
                    continue
                elif choice in ['q', 'quit']:
                    return
            self.engine.analyze(job)

if __name__ == '__main__':
    Chucky().execute()
