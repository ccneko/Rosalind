#!/usr/env
from util import *
#majority element

def maj():
	f = open('rosalind_maj.txt','r')
	ln1 = f.readline().rsplit()
	k = int(ln1[0])
	half = int(ln1[1])/2

	for i in range(k):
		D = {}
		maj = 0
		A = f.readline().rsplit()
		for j in range(len(A)):
			num = int(A[j])

			if num not in D:
				D[num] = 1
				maj = 1
			else:
				D[num] += 1
				if D[num] > maj:
					maj = D[num]
			if D[num] > half:
				#print num
				writeResult('maj',str(num)+' ')
				break	
		if maj <= half:
				#print '-1'
				writeResult('maj','-1 ')
	f.close


maj()
