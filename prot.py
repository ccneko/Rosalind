#!/usr/env
from util import *
#translate

def translate(s):
	aa = readRNAcodon()
	index = {'U':0,'C':1,'A':2,'G':3}
	a = -1
	for i in range(0,len(s)-1,3):
		a = index[s[i]]*4*4 + index[s[i+1]]*4 + index[s[i+2]]
		if aa[a] == '*':
			break
		writeResult('prot',aa[a])

s=readData('rosalind_prot.txt')[0].rstrip()
translate(s)
