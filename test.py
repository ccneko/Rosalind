from rosa_util import *
s=readData('data/rosalind_prot.txt')[0].rstrip()
print translate(s,'rna_codon.txt')
