#!/usr/env

def readData():
	data = open('longest_path.txt','r')
	splitline = data.readline().split()
	n = int(splitline[0])
	m = int(splitline[1])

	Down = []
	Right = []

	for i in range(n):
		splitline = data.readline().split()
		Down.append([])
		for j in range(m+1):
			Down[i].append(int(splitline[j]))
	
	data.readline()

	for i in range(n+1):
		splitline = data.readline().split()
		Right.append([])
		for j in range(m):
			Right[i].append(int(splitline[j]))
	data.close()
	return n,m,Down,Right
	
def ManhattanTourist(n,m,Down,Right):
	s = [[0]*(m+1) for i in range(n+1)]
	for i in range(1,n+1):
		s[i][0] = s[i-1][0] + Down[i-1][0]
	for j in range(1,m+1):
		s[0][j] = s[0][j-1] + Right[0][j-1]
	for i in range(1,n+1):
		for j in range(1,m+1):
			s[i][j] = max(s[i-1][j] + Down[i-1][j],s[i][j-1] + Right[i][j-1])
	print s[n][m]
	return s

def Trackback(s):
	pass

Data = readData()
ManhattanTourist(Data[0],Data[1],Data[2],Data[3])
