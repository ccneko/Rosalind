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
n = int(readData()[0].strip())
list = range(1,n+1)
perm(list)
writeResult(str(len(permlist))+'\n')
writeResult('\n'.join(permlist))