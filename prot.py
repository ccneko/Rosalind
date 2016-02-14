#!/usr/env
from rosa_util import *
#translate

flushResult()
s=readData()[0].strip()
writeResult(translate(s,'codon.txt'))
