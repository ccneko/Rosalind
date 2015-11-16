#!/usr/env
from util import *
#superstring from FASTA

def cons(seq):
	nucl = ['A','C','G','T']
	cons = ''
	A = []
	C = []
	G = []
	T = []
	for i in range(len(seq[0])):
		a = 0
		c = 0
		g = 0
		t = 0
		for s in seq:
			if s[i] == 'A':
				a += 1
			elif s[i] == 'C':
				c += 1
			elif s[i] == 'G':
				g += 1
			elif s[i] == 'T':
				t += 1

		mode = max(a,c,g,t)
		if a == mode:
			cons += 'A'
		elif c == mode:
			cons += 'C'
		elif g == mode:
			cons += 'G'
		elif t == mode:
			cons += 'T'
		A.append(a)
		C.append(c)
		G.append(g)
		T.append(t)

	print cons
	writeResult('cons',cons+'\n')
	aa = 'A: '+' '.join(str(x) for x in A)+'\n'
	cc = 'C: '+' '.join(str(x) for x in C)+'\n'
	gg = 'G: '+' '.join(str(x) for x in G)+'\n'
	tt = 'T: '+' '.join(str(x) for x in T)+'\n'
	print aa,cc,gg,tt
	writeResult('cons',aa+cc+gg+tt)

f = readFASTA('rosalind_cons.txt')
cons(f[1])
