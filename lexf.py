#!/usr/bin/env python
from rosa_util import *
from itertools import product

flushResult()
data = readData()
alphalist = data[0].strip().split()
n = int(data[1].strip())

permlist = list(product(alphalist,repeat=n))
for perm in permlist:
	writeResult(''.join(perm)+'\n')