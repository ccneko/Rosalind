#!/usr/env
from util import *
#fibonacci mortal rabbits, #pairs after n months, each dead after m month

def fibd(n,m):
	p = 1
	repro = 0
	dead = [1]+ [0]*(m-1)
	for i in range(n-1):
		temp = p	
		dead.insert(0,p)
		p = p + repro - dead.pop()
		repro = temp
		print p,repro,dead
	writeResult('fibd',str(p))
#n=int(readData('rosalind_fibd.txt')[0].rsplit()[0])
#m=int(readData('rosalind_fibd.txt')[0].rsplit()[1])
#fibd(n,m)
fibd(7,3)
