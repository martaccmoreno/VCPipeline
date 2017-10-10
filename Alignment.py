import os

class Alignment:
    def __init__(self, ref, reads):
        """
        :param ref: the path to the reference genome
        :param reads: list of paths to the reads to map to the genome ref
        """
        self.ref = ref
        self.reads = reads

    def print_args(self):
        print(self.ref, self.reads)
