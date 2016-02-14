#!/usr/env
from rosa_util import *
import re
#find N-glycosylation N{P}[ST]{P} motif from UniProt FASTA

def findpatternpos(pattern):
	db = 'http://www.uniprot.org/uniprot/'
	f = open('data/rosalind_mprt.txt','r')
	
	for line in f.readlines():
		# get FASTA
		pos = []
		url = db+line.strip()+'.fasta'
		fasta = readFASTA(url)
		seqname = fasta[0][0]
		seq = fasta[1][0]
		
		for i in range(len(seq)):
			# find position of pattern
			if seq[i] == 'N':
				if pattern.match(seq[i:i+4]):
					pos.append(i+1)
		
		if len(pos) > 0:
			# write result
			writeResult(line)
			motifpos = ' '.join(str(x) for x in pos)
			writeResult(motifpos+'\n')
					
	f.close()

flushResult()
pattern = re.compile('N[^P][ST][^P]')
findpatternpos(pattern)
