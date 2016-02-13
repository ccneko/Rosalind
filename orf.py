#!/usr/env
from rosa_util import *
#translate DNA to protein from ORF

def translateORF(s):
	protlist = translateORF_f(revc(s),translateORF_f(s,[]))
	for prot in protlist:
		print prot
		writeResult('orf',prot+'\n')

	return protlist

def translateORF_f(s,protlist):
        for i in range(len(s)):
                if s[i:i+3] == 'ATG':
			prot =  translateDNA(s[i:])
			if protlist is not None:
				if prot is not None and prot not in protlist:
					protlist.append(prot)
	return protlist			

s=readFASTA('rosalind_orf.txt')[1][0].rstrip()
translateORF(s)
