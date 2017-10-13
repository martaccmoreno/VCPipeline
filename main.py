"""
Script which runs the pipeline modules.
"""

from Mapping import Mapping
from misc import *
import os

### PARSE ARGUMENTS

parser = argparse.ArgumentParser(description='A basic WES pipeline.')
parser.add_argument('reference', help='The genome to use as a reference.', type=is_fasta)
parser.add_argument('reads', nargs='+', help='The reads to use as input.', type=is_read)
parser.add_argument('-o', dest='output', default=".", help='Output directory (default is the current directory)')
# MAYBE adicionar opção para correr no fundo
args = parser.parse_args()
# transform the Namespace object into a dictionary where argument names are keys
dic_args = vars(args)

### PIPELINE

map = Mapping(dic_args['reference'], dic_args['reads'], dic_args['output'])

# If reference hasn't been fully indexed, index it
index_filenames = gen_index_filenames(dic_args['reference'])
list_dir = os.listdir(dic_args['output'])
if check_index_files(list_dir, index_filenames) == False:
    map.index()


# Check if we have BAM files in reads and map non-BAM files (i.e. FASTQ)
# Need way to deal with non FASTQ files -- probably forbid them right away
nb = not_bam(dic_args['reads'])
if sum_not_bam(nb) > 0: # if not all items are .bam
    for nb_elem in nb:
        map.map()
        dic_args['reads'] = [read.replace('.sam','.bam') for read in dic_args['reads']]
        map = Mapping(dic_args['reference'], dic_args['reads'], dic_args['output'])

# Fixmate
map.fixmate()

# Sorting
map.sort()




