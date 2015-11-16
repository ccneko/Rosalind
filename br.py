from sys import argv
from util import *
with open(argv[1],'r') as f:
	for x in f.readline().split():
		writeResult('resu-test.txt',x+'\n')
