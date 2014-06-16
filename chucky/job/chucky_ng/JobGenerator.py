from settings import Defaults

from job.chucky_ng.Job import ChuckyJob
from job.JobGenerator import JobGenerator as _JobGenerator

SOURCE = Defaults.SOURCE
SINK = Defaults.SINK

"""
Creates a list of jobs for Chucky Engine based
on user queries.
"""

class JobGenerator(_JobGenerator):

    def __init__(self, identifier, identifier_type):
        split = self.suffix = identifier.split(':', 1)
        identifier_prefix = split[0]
        _JobGenerator.__init__(self, identifier_prefix, identifier_type)
        self.category = SOURCE
        self.suffix = split[1] if len(split) > 1 else None
        
    def _jobs_from_symbols(self, symbols):
        def f(x):
            job = ChuckyJob(x.statement(), x)
            job.n_neighbors = self.n_neighbors
            job.category = self.category
            job.suffix = self.suffix
            return job
        return map(f, symbols)
