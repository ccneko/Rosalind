#!/usr/env
from rosa_util import *
#translate

def translate(s):
	aa = readCodon('rna_codon.txt')
	index = {'A':0,'C':1,'G':2,'U':3}
	a = -1
	for i in range(0,len(s)-1,3):
		a = index[s[i]]*4*4 + index[s[i+1]]*4 + index[s[i+2]]
		if aa[a] == '*' or aa[a] == 'Stop':
			break
		writeResult(aa[a])

flushResult()
s=readData('data/rosalind_prot.txt')[0].rstrip()
translate(s)
