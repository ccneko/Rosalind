#!/usr/env
from rosa_util import *
#mer

def mer():
	l1 = []
	l2 = []
	l = []
	f = open('rosalind_mer.txt','r')
	n = int(f.readline().strip())

	for i in f.readline().split():
		l1.append(int(i))

	m = int(f.readline().strip())
	for i in f.readline().split():
		l2.append(int(i))

	for i in range(n+m):
		if len(l1) == 0:
			writeResult('mer',' '.join(str(x) for x in l2))
			return
			#for x in l2:
			#	l.append(x)
			#	return l
		elif len(l2) == 0:
			writeResult('mer',' '.join(str(x) for x in l1))
			return
			#for x in l1:
			#	l.append(x)
			#	return l
		if l1[0] == min(l1[0],l2[0]):
			writeResult('mer',str(l1.pop(0))+' ')
			#l.append(l1.pop(0))
		if l2[0] == min(l1[0],l2[0]):
			writeResult('mer',str(l1.pop(0))+' ')
			#l.append(l2.pop(0))

	#return l
mer()
