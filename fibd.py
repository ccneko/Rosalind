from rosa_util import *
#fibonacci mortal rabbits, #pairs after n months, each dead after m month

class fibd(n,m):
	def __init__(self):	
		self.time = 0
		self.maturity = 1
		self.start = n
		self.lifespan = m
		self.total = 1
		self.born = [1]
		self.mature = 0
		self.dead = 0
		
		if self.start == 1:
			return self.total
	
	def __iter__(self):
		return self
		
	def __next__(self):
		if self.start  1:
			raise StopIteration
		else:
			self.time += 1
			self.death()
			self.birth()
		return self
		
	def birth(self):
		
		self.born.append(self.p + self.mature*2)
		return
	
	def mature(self):
		newlymatured = self.born[max(0,self.time-self.maturity)]
		self.matured.append(self.born
		return
		
	def death(self):
		return
		
	for i in range(1,n):
		temp = p
		dead.append() = p
		dead.insert(0,p)
		p = p + repro - dead.pop()
		repro = temp
	return p
	
flushResult()
data = readData()
line = data[0]
n = int(line.split()[0])
m = int(line.split()[1])

p = fibd(n,m)
print p
writeResult(str(p))
