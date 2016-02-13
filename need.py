#!/usr/env
from rosa_util import *
from Bio.Emboss.Applications import NeedleCommandline
import re

fetch

def needle():
	needle_cline = NeedleCommandline(asequence = 

def nglyc():
	db = 'http://www.uniprot.org/uniprot/'
	pattern = re.compile('N[^P][ST][^P]')
	f = open('rosalind_mprt.txt','r')
	for line in f.readlines():
		pos = []
		entry = readFASTAfromDB(db,line.rstrip()+'.fasta')
		seqname = entry[0]
		seq = entry[1]
		
		for i in range(len(seq)):
			if seq[i] == 'N':
				if pattern.match(seq[i:i+4]):
					pos.append(i+1)
					#print seq[i:i+4]
		
		if len(pos) > 0:
			print line.rstrip()
			writeResult('mprt',line)
			motifpos = ' '.join(str(x) for x in pos)
			print motifpos
			writeResult('mprt',motifpos+'\n')
			
					
	f.close()
