#!/usr/env
from rosa_util import *
#get O3 from FASTA, note that a "directed graph" is required

def edge(seqnamelist,seqlist,k):
	edges = []
	tmppair = []
	for i in range(len(seqnamelist)):
		for j in range(len(seqnamelist)):
			# check if the suffix k-mer of the i-th sequence = the prefix of the j-th
			if seqlist[i][-k:] == seqlist[j][:k]:
				# ensure the two sequences are not the same
				tmppair = [seqnamelist[i],seqnamelist[j]]
				if len(seqlist[i]) != len(seqlist[j]):
					# check not duplicated
					if tmppair not in edges:
						#print seqnamelist[i]+' '+seqnamelist[j]
						writeResult(' '.join(tmppair)+'\n')
						edges.append(tmppair)
				else:
					for p in range(len(seqlist[i])):
						if seqlist[i][p] != seqlist[j][p]:
							if tmppair not in edges:
								#print seqnamelist[i]+' '+seqnamelist[j]
								writeResult(' '.join(tmppair)+'\n')
								edges.append(tmppair)
							break
	return edges

flushResult()
f = readFASTA('data/rosalind_grph.txt')
edge(f[0],f[1],3)
