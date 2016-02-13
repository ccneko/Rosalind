#!/usr/env
from rosa_util import *
#calculate protein mass

def protmass(s):
	table = readaamass()
	water = table[0]
	aa = table[1]
	aamass = table[2]

	mass = 0
	for i in s:
		mass = mass + aamass[aa.index(i)]
	print '%.3f' % mass
	writeResult('prtm',str('%.3f' % mass))

s=readData('rosalind_prtm.txt')[0].rstrip()
protmass(s)
