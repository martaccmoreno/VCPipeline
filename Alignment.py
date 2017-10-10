import os

"""
Module which performs operations based on the mapping steps of the pipeline
Prerequisites:
* bwa version 0.7.12-r1039
"""

class Alignment:
    def __init__(self, ref, reads, output):
        """
        :param ref: the path to the reference genome
        :param reads: list of paths to the reads to map to the genome ref
        """
        self.ref = ref
        self.reads = reads
        self.out = output

    def print_args(self):
        print(self.ref, self.reads)

    def align(self):
        # executa na mesma quer exista index ou nao - fazer algo acerca disto
        print("Starting...")
        os.system('bwa index '+self.ref)
        print("Done")

    def map(self):
        for read in self.reads:
            print(read)
            os.system('ls '+self.out)
