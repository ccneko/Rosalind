#!/usr/env
#write results to file
import sys, os
from time import strftime
import urllib2

def readData(datafilename):
	with open(datafilename,'r') as f:
		return f.readlines()

def prepResultDir():
	try:
		os.makedirs('result')
	#except OSError as exception:
		#if exception.errno != errno.EEXIST:
			#raise
		#else:
			#pass
	except OSError:
		pass

def flushResult():
	callername = sys._getframe(0).f_back.f_globals['__file__'].split('\\')[-1].rsplit('.',1)[0]
	prepResultDir()
	resultname = 'result/' + callername + '-result.txt'
	r = open(resultname,'w')
	r.close()
		
def writeResult(s):
	callername = sys._getframe(0).f_back.f_globals['__file__'].split('\\')[-1].rsplit('.',1)[0]
	resultname = 'result/' + callername + '-result.txt'
	with open(resultname,'a') as r:
		r.write(s)

def test():
	funcname=sys._getframe().f_code.co_name
	print 'hi'
	print test.__name__
	print funcname

def readCodon(file):
	try:
		f = open(file,'r')
		f.close()
	except OSError:
		aa = stdCodon()
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
		 'V', 'V', 'V', 'V', 'Stop', 'Y', 'Stop', 'Y', \
		 'S', 'S', 'S', 'S', 'Stop', 'C', 'W', 'C', 'L', 'F', 'L', 'F']
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