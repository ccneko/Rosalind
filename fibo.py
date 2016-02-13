#!/usr/env
from rosa_util import *
#fibonacci

def fibo(n):
	a1 = 1
	a2 = 1
	for i in range(n-2):
		temp = a2
		a2 = a1 + a2
		a1 = temp
	print a2
	writeResult('fibo',str(a2))
  n=int(readData('rosalind_fibo.txt')[0].rsplit()[0])
fibo(n)
