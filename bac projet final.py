import os    #efface la console
os.system("cls") 
import random
from copy import deepcopy

a = 10
b = 10
tableau = a*[0]
for i in range (a) :
    tableau[i] = b*[0]


def placer (x):
    hv=random.randit(0,  1)
    if hv == 0:
        i=random.randit(0, a-1)
        j=random.randit(0, b-1-x)
        
        for i in range (i, i+x):
            tableau[i][j]=1
        
    for i in range (b) :
        print(tableau[0][i],  tableau[1][i],  tableau[2][i],  tableau[3][i],   tableau[4][i],  tableau[5][i],  tableau[6][i],  tableau[7][i],  tableau[8][i],  tableau[9][i], sep="  ")
    
    
    else:
        i=random.randit(0, a-1-x)
        j=random.randit(0, b-1)
        
        for j in range (j, j+x):
            tableau[i][j]=1
        
    for j in range (a) :
        print(tableau[j][0],  tableau[j][1],  tableau[j][2],  tableau[j][3],   tableau[j][4],  tableau[j][5],  tableau[j][6],  tableau[j][7],  tableau[j][8],  tableau[j][9], sep="  ")
    
