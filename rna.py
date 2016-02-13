#!/usr/env
from rosa_util import *
#transcribe DNA to RNA, ie 'T' to 'U'

def transcribe(s):
	for i in s:
		if i == 'T':
			writeResult("U")
		else:
			writeResult(i)

flushResult()
s=readData('data/rosalind_rna.txt')[0]
transcribe(s)
