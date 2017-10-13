"""
Module which performs operations based on the mapping steps of the pipeline
Prerequisites:
* bwa version 0.7.12-r1039
"""

import os


class Mapping:
    def __init__(self, ref, reads, output):
        """
        :param ref: the path to the reference genome
        :param reads: list of paths to the reads to map to the genome ref
        """
        self.ref = ref
        self.reads = reads
        self.out = output

    def print_args(self):  # for testing purposes
        print(self.ref, self.reads)

    def index(self):
        print("Starting indexing...")
        os.system('bwa index ' + self.ref)
        print("Done")

    def map(self):
        if len(self.reads) == 1:
            print("Starting mapping...")
            os.system('bwa mem -R "@RG\tID:foo\tSM:bar\tLB:library1" {} {} > {}/lane.sam'
                      .format(self.ref, self.reads[0], self.out))
            print("Done")

        else:
            print("Starting mapping...")
            os.system('bwa mem -R "@RG\tID:foo\tSM:bar\tLB:library1" {} {} > {}/lane.sam'
                      .format(self.ref, ' '.join(self.reads), self.out))
            print("Done")
