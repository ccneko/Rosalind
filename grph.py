#!/usr/env
from util import *
#get O3 from FASTA

def getFASTAnode(FASTAname,n):
	seqname = []
	seqpre = []
	seqsuf = []

	with open(FASTAname,'r') as f:
		while True:
			line = f.readline()
			if len(line) == 0:
				break
			elif line[0] == '>':
				seqname.append(line.rstrip()[1:])
				seqline = f.readline().rstrip()
				seqpre.append(seqline[:n])
				seqsuf.append(seqline.rstrip()[-n:])
			else:
				seqsuf[-1] = line.rstrip()[-n:]
	return seqname,seqpre,seqsuf

def edge1(seqname,seqpre,seqsuf):
	for i,j in enumerate(seqsuf):
		for p,q in enumerate(seqpre):
			if j == q and i != p:
				print seqname[i]+'\t'+seqname[p]
				writeResult('grph',seqname[i]+'\t'+seqname[p]+'\n')

def edge(seqname,seq,n):
	for i in range(len(seqname)):
		for j in range(len(seqname)):
			if seq[i][-n:] == seq[j][:n]:
				if len(seq[i]) != len(seq[j]):
					print seqname[i]+' '+seqname[j]
					writeResult('grph',seqname[i]+' '+seqname[j]+'\n')
				else:
					for p in range(len(seq[i])):
						if seq[i][p] != seq[j][p]:
							print seqname[i]+' '+seqname[j]
		                                        writeResult('grph',seqname[i]+' '+seqname[j]+'\n')
							break


f = readFASTA('rosalind_grph.txt')
edge(f[0],f[1],3)
