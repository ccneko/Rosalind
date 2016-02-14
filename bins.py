#!/usr/env
from rosa_util import *
#binary search

def bins():
	l = []
	f = open('rosalind_bins.txt','r')
	f.readline()
	f.readline()
	for i in f.readline().rsplit():
		l.append(int(i))

	m = l[len(l)/2]
	for i in f.readline().rsplit():
		n = int(i)
		if n < m:
			if n in l[:len(l)/2]:
				ans = str(l.index(n)+1)
				#print ans
				writeResult(ans+' ')
			else:
				notfound()
		elif n >= m:
			if n in l[len(l)/2:]:	
				ans = str(l.index(n)+1)
				#print ans
				writeResult(ans+' ')
                                        
			else:
				notfound()
	f.close

def notfound():
	#print '-1'
	writeResult('bins','-1 ')

flushResult()
bins()
