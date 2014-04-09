
import subprocess
import shlex

class SallyBasedEmbedder:
    
    def embed(self, directory, embType = 'cnt'):
        
        config = 'sally -q -c sally.cfg '
        config = config + ' --hash_file {}/feats.gz --vect_embed=' + embType
        config = config.format(directory)
        inputdir = '{}/data/'
        inputdir = inputdir.format(directory)
        outfile = '{}/embedding.libsvm'
        outfile = outfile.format(directory)
        command = ' '.join([config, inputdir, outfile])
        subprocess.check_call(shlex.split(command))
        