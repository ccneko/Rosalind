#!/usr/env
from rosa_util import *
#fibonacci rabbits, #pairs after n months, k pairs per month

def fib(n,k):
	p = 1
	repro = 0

	for i in range(n-1):
		temp = p
		p = p + repro*k
		repro = temp
	print p
	writeResult(str(p))

flushResult()
data = readData('data/rosalind_fib.txt')[0]
n=int(data.rsplit()[0])
k=int(data.rsplit()[1])
fib(n,k)
