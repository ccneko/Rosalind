#!/usr/env
from util import *
#transcribe DNA to RNA, ie 'T' to 'U'

def transcribe(s):
	for i in s:
		if i == 'T':
			writeResult('rna',"U")
		else:
			writeResult('rna',i)

s=readData('rosalind_rna.txt')[0]
transcribe(s)
