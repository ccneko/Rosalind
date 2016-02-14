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
	writeResult(str(a2))
  n=int(readData()[0].rsplit()[0])
fibo(n)
