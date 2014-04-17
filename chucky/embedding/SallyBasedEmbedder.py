
import subprocess
import shlex

class SallyBasedEmbedder:
    
    def embed(self, directory, embType = 'cnt'):

        cmd = (
                'sally '
                '--quiet '
                '--input_format dir '
                '--output_format libsvm '
                '--ngram_len 1 '
                '--ngram_delim %0a '
                '--vect_embed {vect_embed} '
                '--hash_file {directory}/feats.gz '
                '{directory}/data '
                '{directory}/embedding.libsvm '
        ).format(
                vect_embed = embType,
                directory = directory
        )

        #config = 'sally -q -c sally.cfg '
        #config = config + ' --hash_file {}/feats.gz --vect_embed=' + embType
        #config = config.format(directory)
        #inputdir = '{}/data/'
        #inputdir = inputdir.format(directory)
        #outfile = '{}/embedding.libsvm'
        #outfile = outfile.format(directory)
        #command = ' '.join([config, inputdir, outfile])
        #print cmd
        #print command
        subprocess.check_call(shlex.split(cmd))
