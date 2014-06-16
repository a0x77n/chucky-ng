from settings import Defaults
from job.Job import ChuckyJob as _ChuckyJob

DEFAULT_N = Defaults.N_NEIGHBORS
SINK = Defaults.SINK
SOURCE = Defaults.SOURCE

class ChuckyJob(_ChuckyJob):
    
    def __init__(self, target, symbol):
        _ChuckyJob.__init__(self, target, symbol)
        self.category = SOURCE
        self.suffix = None

    def __setattr__(self, name, value):
        try:
            if name == 'category':
                if value in [SOURCE, SINK]:
                    _ChuckyJob.__setattr__(self, name, value)
                else:
                    raise AttributeError()
            else:
                _ChuckyJob.__setattr__(self, name, value)
        except Exception, e:
            print e
            raise AttributeError(e)

        @property
        def function(self):
            return self.target.function()
