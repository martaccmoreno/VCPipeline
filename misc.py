"""
Module with miscellaneous functions to aid main.py
"""

def not_bam(reads):
    return [(x, True) if x[len(x)-3:len(x)] != "bam" else (0, False) for x in reads]

def sum_not_bam(not_bam):
    return sum([nb[1] for nb in not_bam])

def gen_index_filenames(fn):
    filename_prefix = fn[:len(fn)-3]
    filenames =  [filename_prefix+suffix for suffix in ['amb', 'ann', 'bwt', 'pac', 'sa']]
    return filenames