#!/usr/env
from util import *
#reverse complement

def revc1(s):
	for i in s[::-1]:
		if i == 'A':
			writeResult('revc','T')
		elif i == 'C':
			writeResult('revc','G')
		elif i == 'G':
			writeResult('revc','C')
		elif i == 'T':
			writeResult('revc','A')
				
s=readData('rosalind_revc.txt')[0]
revc1(s)
