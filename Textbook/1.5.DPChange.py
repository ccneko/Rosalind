#!/usr/env

def readData():
	data = open('change_problem.txt','r')
	money = int(data.readline())
	Coins = [int(x) for x in data.readline().rstrip().split(',')]
	data.close()
	return money,Coins
	
def DPChange(money,Coins):
	MinNumCoins = [0]*(money+1)
	for m in range(1,money + 1):
		MinNumCoins[m] = float('inf')
		for i in range(len(Coins)):
			if m >= Coins[i]:
				if MinNumCoins[m - Coins[i]] + 1 < MinNumCoins[m]:
					MinNumCoins[m] = MinNumCoins[m - Coins[i]] + 1
	return MinNumCoins[money]

Data = readData()
print DPChange(Data[0],Data[1])
