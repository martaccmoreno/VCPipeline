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
# verificar se o ficheiro é BAM ou se é preciso mapear contra o genome de referencia
args = parser.parse_args() # get args into a Namespace object
dic_args = vars(args) # transform the Namespace object into a dictionary where argument names are keys
#print(dic_args)

align = Alignment(dic_args["reference"], dic_args["reads"], dic_args["output"])
align.print_args()
#align.align()
align.map()