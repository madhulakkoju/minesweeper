# PLAY FIELD IN MINESWEEPER GAME WHEN ROWS, COLUMNS AND NUMBER OF MINES ARE GIVEN.

import numpy as np
import random as rd
n1 = int(input("Rows : "))
n2 = int(input("Columns : "))
x=np.zeros((n1,n2),dtype=np.int)
m=int(input("mines count : "))
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

print(x)
