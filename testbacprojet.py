import os    #efface la console
os.system("cls") 
import random
from copy import deepcopy




def placer (x):
    global numero_bato
    test = 0
    while test == 0 :
        hv = random.randint(0,  1) # 1 vertical ou 0 horizontal
        print(hv)
        if hv == 1 :
            i = random.randint(0,  (a-1)-x)
            j = random.randint(0,  b-1)
            compteur = i
            test = 0
            while tableau[compteur][j] == 0 and compteur < i+x :
                compteur = compteur + 1
            if compteur == i+x :
                test = 1
                for t in range (i, i+x):
                    tableau[t][j] = numero_bato
                    
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
                    tableau[i][t]= numero_bato
                    
    tabposition[numero_bato][0] = i
    tabposition[numero_bato][1] = j
    tabposition[numero_bato][2] = hv
    tabposition[numero_bato][3] = x
    tabposition[numero_bato][4] = x
    
    print("test =  ",  test)
    print("i =  ", i ,"j =   ",   j)
    print("x = ",  x)
    print(numero_bato)
    numero_bato = numero_bato + 1

def affiche_grille(t) :
    for i in range (b) :
        for j in range (a) :
            print(repr(t[i][j]).rjust(2) , end=' ')
        print(sep=" ")
        
def test_sylvain(i, j) :
    num = tableau[i][j]

    if num == 0 :
        tableau[i][j] = -1
    elif num > 0 :
        if tabposition[num][3] == 1 : # le bateau est coulé
            tabposition[num][3] = 0
            if tabposition[num][2] == 0 : # bateau horizontal
                for s in range(tabposition[num][1], tabposition[num][1]+ tabposition[num][4]):
                    tableau[i][s] = -3
            else :               #bateau vertical
                for s in range(tabposition[num][0], tabposition[num][0]+ tabposition[num][4]):
                    tableau[s][j] = -3
        else :
            tabposition[num][3] = tabposition[num][3]-1
            tableau[i][j] = -2

# DEBUT

            
a = 10
b = 10

tableau = a*[0]
for i in range (a) :
    tableau[i] = b*[0]
    
tabposition = 10*[0]
for i in range (10) :
    tabposition[i] = 5*[0]

numero_bato = 1

placer(4)
placer(5)
placer(3)
placer(2)
placer(2)
placer(8)
placer(4)


affiche_grille(tableau)

for i in range (numero_bato) :
    for j in range (5) :
        print(tabposition[i][j], end=' ')
    print(sep=" ")


for s in range (1) :
    v = random.randint(0, 9)
    r = random.randint(0, 9)
    test_sylvain(v, r)
    
#for i in range (b) :
#    for j in range (a) :
#        test_sylvain(i, j)

affiche_grille(tableau)

for i in range (numero_bato) :
    for j in range (5) :
        print(tabposition[i][j], end=' ')
    print(sep=" ")
