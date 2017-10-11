"""
Module which performs operations based on the mapping steps of the pipeline
Prerequisites:
* bwa version 0.7.12-r1039
"""

import os

class Alignment:
    def __init__(self, ref, reads, output):
        """
        :param ref: the path to the reference genome
        :param reads: list of paths to the reads to map to the genome ref
        """
        self.ref = ref
        self.reads = reads
        self.out = output

    def print_args(self): # for testing purposes
        print(self.ref, self.reads)

    def index(self):
        print("Starting indexing...")
        os.system('bwa index '+self.ref)
        print("Done")

    def map(self):
        if len(self.reads) == 1:
            print("Starting mapping...")
            os.sytem('bwa mem -R "@RG\tID:foo\tSM:bar\tLB:library1" ' + self.reads[0] + ' > lane.sam')
            print("Done")

        else:
            #### REWRITE #####
            for read in self.reads:
                print("Starting mapping...")
                os.sytem('bwa mem -R "@RG\tID:foo\tSM:bar\tLB:library1" ' + read + ' > lane.sam')
                # rather than doing read by read this should truly group reads by lane
                print("Done")

