#!/usr/env
from rosa_util import *
#find motif from

def gc(s):
	gc = 0.0
	for i in range(len(s)):
		if s[i] == 'G' or s[i] == 'C':
			gc += 1
	gc = gc/len(s)*100 
	return gc

def findhighgc():
	with open('data/rosalind_gc.txt','r') as f:
		seqname = []
		gcvalue = []
		newseq = ''
		highgc = 0
		newgc = 0
		for line in f.readlines():
			if line[0] == '>':
				seqname.append(line.rstrip()[1:])
				if len(newseq) > 0:
					newgc = gc(newseq)
					gcvalue.append(newgc)
				if newgc > highgc:
					highgc = newgc
				newseq = ''
			else:
				newseq = newseq + line.rstrip()
		newgc = gc(newseq)
		gcvalue.append(newgc)
		if newgc > highgc:
			highgc = newgc

	gcname = seqname[gcvalue.index(highgc)]
	writeResult(gcname+'\n')
	writeResult('%.6f' % highgc)
	print gcname
	print '%.6f' % highgc

flushResult()
findhighgc()
