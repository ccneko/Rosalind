#!/usr/bin/env python
from rosa_util import *
from itertools import product

flushResult()
data = readData()
alphalist = data[0].strip().split()
n = int(data[1].strip())

permlist = []
for i in range(1,n+1):
	tmplist = []
	newlist = []
	newtuplelist = list(product(alphalist,repeat=i))
	
	for perm in newtuplelist:
		newlist.append(''.join(list(perm)))
	
	if len(permlist)>0:
		for i,j in enumerate(permlist):
			#print j
			tmplist.append(j)
			if permlist[i][0]!=permlist[i-1][0]:
				for k in newlist:
					print k
					if j[0]==k[0]:
						tmplist.append(k)
						newlist.pop(0)
		
		for perm in tmplist:
			permlist += list(perm)
	else:
		permlist = newlist
	#print permlist
	
for perm in permlist:
	writeResult(''.join(perm)+'\n')