#!/usr/bin/env python
from rosa_util import *
from itertools import permutations

permlist = []
def perm(a,k=0):
	if(k==len(a)):
		permlist.append(' '.join(str(x) for x in a))
	else:
		for i in xrange(k,len(a)):
			a[k],a[i] = a[i],a[k]
			perm(a, k+1)
			a[k],a[i] = a[i],a[k]

flushResult()
data = readData()
alphalist = data[0].strip().split()
n = int(data[1].strip())
print list(permutations(alphalist,n))
#perm(list)
#writeResult(str(len(permlist))+'\n')
#writeResult('\n'.join(permlist))