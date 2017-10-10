import argparse
from Alignment import Alignment

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

# check if we have BAM files in reads and map non-BAM files (i.e. FASTQ)
not_bam = [(x, True) if x[len(x)-3:len(x)] != "bam" else (0, False) for x in dic_args['reads']]
if sum([nb[1] for nb in not_bam]) > 0: # if not all items are .bam
    align = Alignment(dic_args['reference'], dic_args['reads'], dic_args['output'])
    #align.map()



