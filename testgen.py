def gen1():
	for i in range(10):
		yield i
	
for i in gen1():
	print i