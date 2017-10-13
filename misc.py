"""
Module with miscellaneous functions to aid main.py
"""
import argparse

### CHECK FILE TYPES

def is_fasta(string):
    'Check if the reference has a legal file ending for FASTA format files.'
    for file_type in ['.fna', '.fast', '.fa']:
        if file_type == string[len(string)-len(file_type):len(string)]:
            return string
        msg = 'Reference is not a FASTA file'
        raise argparse.ArgumentTypeError(msg)

def is_read(string):
    'Check if reads have an eligible file ending.'
    for file_type in ['.bam', '.fastq', '.fastq.gz']:
        if file_type == string[len(string)-len(file_type):len(string)]:
            return string
        msg = 'One or more reads cannot be used as input. They must be FASTQ or BAM files.'
        raise argparse.ArgumentTypeError(msg)

### OTHER CHECKS

def check_index_files(list_dir, index_filenames):
    'Check if all index-related files are available (True), if not runs the index command (False).'
    for file in index_filenames:
        if file not in list_dir:
            return False
    return True


### OTHERS

def gen_index_filenames(fn):
    filename_prefix = fn[:len(fn)-3]
    filenames =  [filename_prefix+suffix for suffix in ['amb', 'ann', 'bwt', 'pac', 'sa']]
    return filenames

def not_bam(reads):
    return [(x, True) if x[len(x)-3:len(x)] != "bam" else (0, False) for x in reads]

def sum_not_bam(not_bam):
    return sum([nb[1] for nb in not_bam])