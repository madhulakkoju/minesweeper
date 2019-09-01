import numpy as np
import random as rd
n1 = int(input("Rows : "))
n2 = int(input("Columns : "))
global x 
x = np.zeros((n1,n2),dtype=np.int)
m=int(input("mines count : "))
mines1 = m
a=0
b=0
while(m>0):
	a=rd.randint(0,n1-1)
	b=rd.randint(0,n2-1)
	if(x[a][b]==9):
		continue
	else:
		x[a][b]=9
		for i in range(-1,2,1):
			for j in range(-1,2,1):
				if(i==0 and j==0):
					continue
				elif(a-i<0):
					continue
				elif(b-j<0):
					continue
				elif(a-i>(n1-1)):
					continue
				elif(b-j>(n2-1)):
					continue
				else:
					x[a-i][b-j] = x[a-i][b-j] + 1
					if(x[a-i][b-j]>9):
						x[a-i][b-j]=9
		m = m-1
#print(x)
global game
game = np.full((n1,n2),11)
print(game)
def clearxy(x1,y1):
	if(x[x1][y1]==9):
		visit[x1][y1]=1
		print("GAME OVER - BETTER LUCK NEXT TIME")
		sys.exit(0)
		return
	elif(x[x1][y1] != 0 and visit[x1][y1]==0):
		game[x1][y1]=x[x1][y1]
		visit[x1][y1]=1
		return
	elif(x[x1][y1]==0 and visit[x1][y1]==0):
		game[x1][y1]=x[x1][y1]
		visit[x1][y1]=1
		for d in range(-1,2,1):
			for e in range(-1,2,1):
				if(d==0 and e==0):
					continue
				elif(x1-d<0):
					continue
				elif(y1-e<0):
					continue
				elif(x1-d>(n1-1)):
					continue
				elif(y1-e>(n2-1)):
					continue
				else:
					if(visit[x1-d][y1-e]==0):
						clearxy(x1-d,y1-e)
	return
# taking max 30 moves
mines=0
visit = np.zeros((n1,n2),dtype=np.int)
for i in range(30):
	mines = 0
	xc= int(input("X : "))
	yc= int(input("Y : "))
	clearxy(xc,yc)
	print(game)
	for f in range(n1):
		for g in range(n2):
			if(visit[f][g]==0):
				mines= mines +1

	if(mines==mines1):
		print("WINNER WINNER CHICKEN DINNER")
		break
