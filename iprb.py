#!/usr/env
from rosa_util import *
#mendelian inheritance

def Pdom(k,m,n):
	prob = 1.0
	total = k + m + n
	k1 = k/total
	m1 = m/total
	n1 = n/total
	#prob = 1 - n1*(n1+m1/2) - m1*m1/4
	#prob = 1 - 2 * n/total * (n-1)/(total-1) - 2* n/total * (m/2)/total - 2* (m/2)/total * ((m-1)/2)/(total - 1)
	print '%.5f' % prob
	writeResult('%.5f' % prob)
	return prob

f = readData()[0].rsplit()
k = float(f[0])
m = float(f[1])
n = float(f[2])

Pdom(k,m,n)
