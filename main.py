"""
Script which runs the pipeline modules.
"""

from Alignment import Alignment
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

# If reference hasn't been fully indexed, index it
index_filenames = gen_index_filenames(dic_args['reference'])
list_dir = os.listdir(dic_args['output'])
for file in index_filenames:
    if file not in list_dir:
        align = Alignment(dic_args['reference'], dic_args['reads'], dic_args['output'])
        align.index()
        break # eeeeh deve haver maneira melhor de fazer isto

# check if we have BAM files in reads and map non-BAM files (i.e. FASTQ)
# Need way to deal with non FASTQ files -- probably forbid them right away
nb = not_bam(dic_args['reads'])
if sum_not_bam(nb) > 0: # if not all items are .bam
    for nb_elem in nb:
        to_map = Alignment(dic_args['reference'], nb_elem[0], dic_args['output'])
        #to_map.map()
        #dic_args['reads'].replace(non-bam for bam equivalent)

    # after being converted into BAM these reads need to join the rest of the pipeline

# next: fixmate and sort
# We have two instances of Alignment at times... way to only have one instance?



