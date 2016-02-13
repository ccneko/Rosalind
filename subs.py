#!/usr/env
from rosa_util import *
#find motif, findmotif_l incomplete

def findmotif(s1,s2):
	if len(s2)>1000:
		findmotif_l(s1,s2)
	else:
		findmotif_s(s1,s2)

def findmotif_s(s1,s2):
	for i in range(len(s1)):
		if s1[i:i+len(s2)] == s2:
			writeResult(str(i+1)+'\t')

def findmotif_l(s1,s2):
	index = {'T':0,'C':1,'A':2,'G':3}
	n = 0
	temp = 0
	i1 = 0
	j1 = 0
	seed = s2[:5]

	for i in s2:
		n = n + index[i] 

	for i in range(len(s1)-len(s2)):
		if s1[i:i+5] == seed:
			for j in range(len(s2)-1):
				j1 = j
				if s1[i+j] != s2[j]:
					break
				temp = temp + index[s1[i+j]]
		if j1 == len(s2)-1 and s1[i+j] == s2[j]:
			i1 = i + 1
			writeResult(str(i+1)+'\t')
			break

	for i in range(i1,len(s1)-len(s2)):
		temp = temp + index[s1[i+len(s2)]] - index[s1[i]]
		if s1[i:i+5] == seed and temp == n:
			for j in range(len(s2)-1):
				j1 = j
				if s1[i+j]!=s2[j]:
					break
		if j == len(s2)-1 and s1[i+j] == s2[j]:
			writeResult(str(i+1)+'\t')

flushResult()
f = readData('data/rosalind_subs.txt')
s1 = f[0].rstrip()
s2 = f[1].rstrip()
findmotif(s1,s2)
