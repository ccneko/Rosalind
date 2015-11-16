#!/usr/env
#write results to file
import sys
from time import strftime
import urllib2

def readData(datafilename):
	with open(datafilename,'r') as f:
		return f.readlines()

def writeResult(funcname,s):
	resulttime = strftime("-%Y%m%d_%H%M")
	resultname = funcname + resulttime + '-result.txt'
	with open(resultname,'a') as r:
		r.write(s)

def test():
	funcname=sys._getframe().f_code.co_name
	print 'hi'
	print test.__name__
	print funcname

def readRNAcodon():
	#UCAG
	aa= []
	with open('rna_codon.tsv','r') as f:
		for line in f.readlines():
			aa.append(line.rstrip().rsplit()[1])
	return aa

def readDNAcodon():
        #TCAG
        aa= []
        with open('dna_codon.tsv','r') as f:
                for line in f.readlines():
                        aa.append(line.rstrip().rsplit()[1])
        return aa

def readaamass():
	water = 18.01056
	aa = []
	aamass = []
	with open('aamass.tsv','r') as f:
		for line in f.readlines():
			splitline = line.rstrip().rsplit()
			aa.append(splitline[0])
			aamass.append(float(splitline[1]))
	return water,aa,aamass

def readFASTA(FASTAname):
	seqname = []
	seq = []
	temp = ''
	with open(FASTAname,'r') as f:
		for line in f.readlines():
			if line[0] == '>':
				seqname.append(line.rstrip()[1:])
				if len(seqname) > 1:
					seq.append(temp)
				temp = ''
			else:
				temp = temp + line.rstrip()
		seq.append(temp)
	return seqname,seq

def getDNAcodon():
	with open('rna_codon.tsv','r') as old:
		with open('dna_codon.tsv','w') as new:
			for line in old.readlines():
				for i,j in enumerate(line):
					if j == 'U':
						new.write('T')
					else:
						new.write(j)

def revc(s):
	s1 = ''
        for i in s[::-1]:
                if i == 'A':
                        s1 = s1 + 'T'
                elif i == 'C':
                        s1 = s1 + 'G'
                elif i == 'G':
                        s1 = s1 + 'C'
                elif i == 'T':
                        s1 = s1 + 'A'
	return s1

						
def translateDNA(s):
        prot = ''
        aa = readDNAcodon()
        index = {'T':0,'C':1,'A':2,'G':3}
        a = -1
        for i in range(0,len(s)-1,3):
                a = index[s[i]]*4*4 + index[s[i+1]]*4 + index[s[i+2]]
		prot += aa[a]
                if aa[a] == '*':
                        prot = prot[:-1]
			return prot

def readFASTAfromDB(db,s):
	f = urllib2.urlopen(db+s)
	temp = ''
	seqname = ''
	seq = ''
	for line in f.readlines():
		if len(line.rstrip()) == 0:
			pass
		if line[0] == '>':
			seqname = line.rstrip()[1:]
		else:
				seq  = seq + line.rstrip()
	
	return seqname,seq
