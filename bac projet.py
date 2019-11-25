import os    #efface la console
os.system("cls") 
import random
from copy import deepcopy


a = 10
b = 10
tableau = a*[0]
for i in range (a) :
    tableau[i] = b*[0]

i = random.randint(0,  a-1)
j = random.randint(0,  b-1) 
x = random.randint(1,  5)

while i+x > 10:
    i = random.randint(0,  a-1)
    j = random.randint(0,  b-1) 
    x = random.randint(1,  5)
for i in range (i, i+x):
        tableau[i][j]=1


print(i,  j)
print(x)




for i in range (b) :
    print(tableau[0][i],  tableau[1][i],  tableau[2][i],  tableau[3][i],   tableau[4][i],  tableau[5][i],  tableau[6][i],  tableau[7][i],  tableau[8][i],  tableau[9][i], sep="  ")
