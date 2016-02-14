#!/usr/env
#write results to file
import sys, os
from time import strftime
import urllib2

callername = sys._getframe(0).f_back.f_globals['__file__'].split('\\')[-1].rsplit('.',1)[0]
resultname = 'result/' + callername + '-result.txt'

def readData():
	dir = 'data/'
	filename = dir + 'rosalind_' + callername + '.txt'
	return readFile(filename)

def readFile(filename):
	with open(filename,'r') as f:
		return f.readlines()
		
def prepResultDir():
	try:
		os.makedirs('result')
	except OSError:
		pass
	
def flushResult():
	prepResultDir()
	r = open(resultname,'w')
	r.close()
		
def writeResult(s):
	with open(resultname,'a') as r:
		r.write(s)

def readCodon(file):
	try:
		f = open(file,'r')
		f.close()
	except IOError, err:
		if err.errno == 2:
			aa = stdCodon()
		else:
			raise
		return aa
	aa= []
	tmp = []
	with open(file,'r') as f:
		for line in f.readlines():
			tmp = tmp + line.strip().split('\t')
	tmp = sorted(tmp)
	for code in tmp:	
		aa.append(code.split()[1])
	return aa

def stdCodon():
	aa = ['K', 'N', 'K', 'N', 'T', 'T', 'T', 'T', \
		 'R', 'S', 'R', 'S', 'I', 'I', 'M', 'I', 'Q',\
		 'H', 'Q', 'H', 'P', 'P', 'P', 'P', 'R', 'R', \
		 'R', 'R', 'L', 'L', 'L', 'L', 'E', 'D', 'E', \
		 'D', 'A', 'A', 'A', 'A', 'G', 'G', 'G', 'G', \
		 'V', 'V', 'V', 'V', '*', 'Y', '*', 'Y', \
		 'S', 'S', 'S', 'S', '*', 'C', 'W', 'C', 'L', 'F', 'L', 'F']
	return aa

def readaamass():
	water = 18.01056
	aa = []
	aamass = []
	with open('aamass.txt','r') as f:
		for line in f.readlines():
			splitline = line.rstrip().rsplit()
			aa.append(splitline[0])
			aamass.append(float(splitline[1]))
	return water,aa,aamass

def readFASTA(FASTA):
	seqnamelist = []
	seqlist = []
	tmp = ''
	try: 
		f = open(FASTA,'r')
	except IOError, err:
		if err.errno == 22:
			f = urllib2.urlopen(FASTA)
		else:
			raise
	for line in f.readlines():
		if line[0] == '>':
			seqnamelist.append(line.strip()[1:])
			if len(seqnamelist) > 1:
				seqlist.append(tmp)
			tmp = ''
		else:
			tmp = tmp + line.strip()
	seqlist.append(tmp)
	f.close()
	return seqnamelist,seqlist

def revc(s):
	s1 = ''
	dict = {'A':'T','C':'G','G':'C','T':'A'}
	for i in s[::-1]:
		s1 = s1 + dict[i]
	return s1

						
def translate(s,codonfile):
	prot = ''
	aa = readCodon(codonfile)
	index = {'A':0,'C':1,'G':2,'T':3,'U':3}
	a = -1
	for i in range(0,len(s)-1,3):
		a = index[s[i]]*4*4 + index[s[i+1]]*4 + index[s[i+2]]
		if aa[a] == '*' or aa[a] == 'Stop':
			break
		prot += aa[a]
	return prot
	
