import argparse
from Alignment import Alignment

"""
Script which runs the pipeline modules.
"""

parser = argparse.ArgumentParser(description='A basic WES pipeline.')
parser.add_argument('reference', help="The genome to use as a reference.")
parser.add_argument('reads', nargs='+', help="The reads to use as input.")
args = parser.parse_args() # get args into a Namespace object
dic_args = vars(args) # transform the Namespace object into a dictionary where argument names are keys

align = Alignment(dic_args["reference"], dic_args["reads"])
align.print_args()