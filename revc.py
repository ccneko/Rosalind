#!/usr/env
from rosa_util import *
#reverse complement

def revc1(s):
	for i in s[::-1]:
		if i == 'A':
			writeResult('T')
		elif i == 'C':
			writeResult('G')
		elif i == 'G':
			writeResult('C')
		elif i == 'T':
			writeResult('A')

flushResult()
s=readData('data/rosalind_revc.txt')[0]
revc1(s)
