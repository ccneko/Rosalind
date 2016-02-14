#!/usr/env
from rosa_util import *
#translate

flushResult()
s=readData('data/rosalind_prot.txt')[0].strip()
writeResult(translate(s,'rna_codon.txt'))
