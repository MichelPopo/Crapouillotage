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
    tabposition = 4*[0]
    for i in range (4) :
        tabposition[i] = 4*[0]
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
            tabposition[x-2][0] = i
            tabposition[x-2][1] = j
            tabposition[x-2][2] = hv
            tabposition[x-2][3] = x
        print("test =  ",  test)
        print("i =  ", i ,"j =   ",   j)
        print("x = ",  x)
    


placer(2)
placer(3)
placer(3)
placer(4)
placer(5)

for i in range (b) :
    print(tableau[0][i],  tableau[1][i],  tableau[2][i],  tableau[3][i],   tableau[4][i],  tableau[5][i],  tableau[6][i],  tableau[7][i],  tableau[8][i],  tableau[9][i], sep=" ")
    
#for i in range (4) :
    #print(tabposition[0][i], tabposition[1][i], tabposition[2][i], tabposition[3][i],  sep=" ")


    
    
