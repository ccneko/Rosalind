#!/usr/env
from util import *
import urllib2
#get GO from UniProt given UniProt ID

def protGO():
	db = 'http://www.uniprot.org/uniprot/'
	f = open('rosalind_dbpr.txt','r')
	arrive = 0
	for line in f:
		pos = []
		txt = urllib2.urlopen(db+line.rstrip()+'.txt')
		for ln in txt.readlines():
			if ln[:2]!='DR':
				continue
			if ln[5:8]!='GO;':
				if arrive == 1:
					return
				continue

			GO =  ln[5:].rsplit(';')[2].rsplit(':')

			if GO[0] == ' P':
				arrive = 1
				print GO[1]
				writeResult('dbpr',GO[1]+'\n')
			
					
	f.close()
	

protGO()
