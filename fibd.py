from rosa_util import *
#fibonacci mortal rabbits, #pairs after n months, each dead after m month

def fibd(n,m):
	p = 1
	repro = 0
	dead = [1]+ [0]*(m-1)
	for i in range(n-1):
		temp = p	
		dead.insert(0,p)
		p = p + repro - dead.pop()
		repro = temp
		print p,repro,dead
	writeResult(str(p))

data = open('rosalind_fibd.txt','r')
line = data.readline()
n = int(line.split()[0])
m = int(line.split()[1])
data.close()

fibd(n,m)
