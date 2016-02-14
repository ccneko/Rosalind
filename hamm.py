#!/usr/env
from rosa_util import *
#hamming distance

def hamm(s1,s2):
	h = 0
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			h += 1
	print h
	writeResult(str(h))

flushResult()
f = readData()
s1 = f[0].rstrip()
s2 = f[1].rstrip()
hamm(s1,s2)
