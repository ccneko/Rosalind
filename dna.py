#!/usr/env
from rosa_util import *
#count number of each base

def  countbase(s):
	a = 0
	c = 0
	g = 0
	t = 0

	for i in s:
		if i == 'A':
			a += 1
		elif i == 'C':
			c += 1
		elif i == 'G':
			g += 1
		elif i == 'T':
			t += 1
		result = '\t'.join([str(a),str(c),str(g),str(t)])
	print result
	writeResult(result)

if __name__ == '__main__':
	flushResult()
	s=readData()[0]
	countbase(s)
