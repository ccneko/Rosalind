#!/usr/bin/env python
from rosa_util import *
from itertools import product

flushResult()
f = open('data/rosalind_lexv.txt','r')
data = f.readlines()
f.close()
alphalist = data[0].strip().split()
n = int(data[1].strip())

permlist = []

for i in range(1,n+1):
	tmplist = list(product(alphalist,repeat=i))
	for item in tmplist:
		permlist.append(''.join(item))
	
tmplist = []
for i,j in enumerate(permlist):
	tmp = j[0]
	tmplist.append(j)
	permlist.remove(j)
	if permlist[i][0]!=tmp:
		for p,q in enumerate(permlist):
			if q[0] == tmp:
				tmplist.append(q)
				permlist.remove(q)
print tmplist
	#writeResult(''.join(perm)+'\n')