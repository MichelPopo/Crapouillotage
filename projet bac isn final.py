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
    test = 0
    while test == 0 :
        hv = random.randint(0,  1)
        print(hv)
        if hv == 0 :
            i = random.randint(0,  (a-1)-x)
            j = random.randint(0,  b-1)
            compteur = i
            test = 0
            while tableau[compteur][j] == 0 and compteur < i+x :
                compteur = compteur + 1
            if compteur == i+x :
                test = 1
                for t in range (i, i+x):
                    tableau[t][j]=x
            
        else : 
            i = random.randint(0,  (a-1))
            j = random.randint(0,  (b-1)-x)
            compteur = j
            test = 0
            while tableau[i][compteur] == 0 and compteur < j+x :
                compteur = compteur + 1
            if compteur == j+x :
                test = 1
                for t in range (j, j+x):
                    tableau[i][t]=x
        
        print("test =  ",  test)  
    print("x = ",  x)

    


placer(2)
placer(3)
placer(4)
placer(5)

for i in range (b) :
    print(tableau[0][i],  tableau[1][i],  tableau[2][i],  tableau[3][i],   tableau[4][i],  tableau[5][i],  tableau[6][i],  tableau[7][i],  tableau[8][i],  tableau[9][i], sep="  ")






