#!/usr/env
from rosa_util import *
#translate DNA to protein from ORF

def translateORF(s):
	protlist = translateORF_f(revc(s),translateORF_f(s,[]))
	for prot in protlist:
		writeResult(prot+'\n')

	return protlist

def translateORF_f(s,protlist):
	for i in range(len(s)):
		if s[i:i+3] == 'ATG':
			prot = translate(s[i:],'codon.txt')
			if protlist is not None:
				if prot is not None and prot not in protlist:
					protlist.append(prot)
	return protlist			

flushResult()
s=readFASTA('data/rosalind_orf.txt')[1][0].rstrip()
translateORF(s)
