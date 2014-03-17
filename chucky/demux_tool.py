import os

class DemuxTool():

    def __init__(self, directory):
        self._directory = directory
        self._init_output_dir()

    def _init_output_dir(self):
        if not os.path.isdir(self._directory):
            path = os.path.join(self._directory, 'data')
            os.makedirs(path)
            open(os.path.join(self._directory, 'TOC'), 'w').close()
            self.toc = dict()
            self._next_file_number = 0
        else:
            self._recover_toc()

    def _recover_toc(self):
        self.toc = dict()
        number = 0
        with open(os.path.join(self._directory, 'TOC')) as f:
            for number, key in enumerate(f):
                self.toc[int(key)] = number
        #self._next_file_number = number + 1
        self._next_file_number = len(self.toc)

    def _add_to_toc(self, key, value):
        toc = open(self._directory + '/TOC', 'a+')
        toc.write(str(key) + '\n')
        toc.close()

    def _output_file(self, key):
        if key not in self.toc:
            self.toc[key] = self._next_file_number
            self._next_file_number += 1
            self._add_to_toc(key, self._next_file_number)

        filename = os.path.join(
                self._directory,
                'data',
                str(self.toc[key]))
        return filename

    def demux(self, key, data):
        with open(self._output_file(key),'a+') as f:
            if data:
                f.write(str(data) + '\n')
