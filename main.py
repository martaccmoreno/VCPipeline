import argparse
from Alignment import Alignment
from misc import *
import os

"""
Script which runs the pipeline modules.
"""

parser = argparse.ArgumentParser(description='A basic WES pipeline.')
parser.add_argument('reference', help="The genome to use as a reference.")
parser.add_argument('reads', nargs='+', help="The reads to use as input.")
parser.add_argument('-o', dest='output', default=".", help='Output directory (default is the current directory)')
# MAYBE adicionar opção para correr no fundo
args = parser.parse_args() # get args into a Namespace object
dic_args = vars(args) # transform the Namespace object into a dictionary where argument names are keys

# If reference hasn't been fully indexed, index it
index_filenames = gen_index_filenames(dic_args['reference'])
list_dir = os.listdir(dic_args['output'])
for file in index_filenames:
    if file not in list_dir:
        align = Alignment(dic_args['reference'], dic_args['reads'], dic_args['output'])
        break # eeeeh deve haver maneira melhor de fazer isto

# check if we have BAM files in reads and map non-BAM files (i.e. FASTQ)
# Need way to deal with non FASTQ files
nb = not_bam(dic_args['reads'])
if sum_not_bam(nb) > 0: # if not all items are .bam
    for nb_elem in nb:
        to_map = Alignment(dic_args['reference'], nb_elem[0], dic_args['output'])
    #to_map.map()



