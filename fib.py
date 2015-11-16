#!/usr/env
from util import *
#fibonacci rabbits, #pairs after n months, k pairs per month

def fib(n,k):
	p = 1
	repro = 0

	for i in range(n-1):
		temp = p
		p = p + repro*k
		repro = temp
	print p
	writeResult('fib',str(p))
n=int(readData('rosalind_fib.txt')[0].rsplit()[0])
k=int(readData('rosalind_fib.txt')[0].rsplit()[1])
fib(n,k)
