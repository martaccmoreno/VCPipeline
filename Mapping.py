""""
Module which performs operations based on the mapping steps of the pipeline
Prerequisites:
* bwa version 0.7.12-r1039
* samtools version 1.6
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
        self.created_files = {}

    def print_args(self):  # for testing purposes
        print(self.ref, self.reads)

    def index(self):
        print('Starting indexing...')
        os.system('bwa index ' + self.ref)
        print('Done')

    def map(self):
        if len(self.reads) == 1:
            print('Starting mapping...')
            os.system('bwa mem -R "@RG\tID:foo\tSM:bar\tLB:library1" {} {} > {}/lane.sam'
                      .format(self.ref, self.reads[0], self.out))
            self.created_files['lane'] = 'lane.sam'
            print('Done')

        else:
            print('Starting mapping...')
            os.system('bwa mem -R "@RG\tID:foo\tSM:bar\tLB:library1" {} {} > {}/lane.sam'
                      .format(self.ref, ' '.join(self.reads), self.out))
            self.created_files['lane'] = 'lane.sam'
            print('Done')

    def fixmate(self):
        print('Cleaning up read pairing information and flags...')
        os.system('samtools fixmate -O bam {0}/lane.sam {0}/lane_fixmate.bam'.format(self.out))
        self.created_files['fixmate'] = 'lane_fixmate.sam'
        print('Done')

    def sort(self):
        print('Sorting using coordinate order...')
        os.system('samtools sort -O bam -o {0}/lane_sorted.bam -T {0}/tmp/lane_temp {0}/lane_fixmate.sam'.format(self.out))
        self.created_files['sorted'] = 'lane_sorted.sam'
        print('Done')

    def return_created_files(self):
        """Returns the names of the files (as a dictionary) thus far created by the class."""
        return self.created_files