import os    #efface la console
os.system("cls") 
import random
from copy import deepcopy
from tkinter import * 
import tkinter as Tk 
from PIL import Image
import tkinter.font as tkFont
import time
from wave import *
from winsound import *


##############################################################################  
##############################################################################  



    
def alert():
    showinfo("alerte", "Bravo!")





    
##############################################################################   
##############################################################################  
    



     #SON  

     
def son_boutons_next(): 
    PlaySound('audio/audio_bouton_next.wav', SND_ASYNC | SND_FILENAME)       

def son_boutons_retour():
    PlaySound('audio/audio_bouton_retour.wav', SND_ASYNC | SND_FILENAME)





##############################################################################  
##############################################################################  
    
          #DEF CONSOLE
        #Placement des bateaux dans la console
    
    
def placer (x):
    global numero_bato
    test = 0
    while test == 0 :                               #test pour savoir si le bateau n'en chevauche pas un autre ou ne sort pas du tableau (tant que la condition n'est pas validée)
        hv = random.randint(0,  1)                  # aléatoire entre 1 vertical ou 0 horizontal
        print(hv)
        if hv == 1 :                                #si c'est vertical
            i = random.randint(0,  (a-1)-x)         #aléatoire entre 0 et hauteur du tableau - celle du bateau
            j = random.randint(0,  b-1)             #aléatoire entre 0 et largeur du tableau - celle du bateau
            compteur = i                            #on crée un compteur pour nos tests ci dessous
            test = 0
            while tableau[compteur][j] == 0 and compteur < i+x :  #tant qu'il n'y a pas de bateau dans la case et que l'on est pas sorti du tableau
                compteur = compteur + 1             #le compteur est augmenté et on passe à la case à coté
            if compteur == i+x :                    #si on arrive enfin à la fin de la taille du bateau et qu'il n'y a pas eu de problèmes
                test = 1                            #le test est bon
                for t in range (i, i+x):            #une boucle pour créer le bateau
                    tableau[t][j] = numero_bato     #et le placer dans le tabposition en fonction de son rang
                    
        else :                                      #pareil mais pour un bateau horizontal
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
                                                
    tabposition[numero_bato][0] = i                 #création du tabposition avec nos infos sur les bateaux à l'interieur
    tabposition[numero_bato][1] = j
    tabposition[numero_bato][2] = hv
    tabposition[numero_bato][3] = x
    tabposition[numero_bato][4] = x
    
    print("test =  ",  test)
    print("i =  ", i ,"j =   ",   j)
    print("x = ",  x)
    print(numero_bato)
    numero_bato = numero_bato + 1                   #l'indice indiquant la place du tableau dans le bateau ainsi que la valeur de ses cases est augmenté
      


def affiche_grille(t) :                             #fonction qui affiche le tableau
    for i in range (b) :                            #double boucle pour parcourir tout le tableau
        for j in range (a) :
            print(repr(t[i][j]).rjust(2) , end=' ') #affichage avec alignement
        print(sep=" ")
 
       
        
def test_touchecoule(i, j) :                        #fonction pour jouer
    global nb_coule2
    num = tableau[i][j]

    if num == 0 :                                   #la case ne contient pas de bateaux
        tableau[i][j] = -1                          #tir dans l'eau = -1 (pour l'affichage)
    elif num > 0 :                                  #sinon il y a un bateau
        if tabposition[num][3] == 1 :               #le bateau est coulé (indice de cases restantes du bateau)
            tabposition[num][3] = 0
            if tabposition[num][2] == 0 :           #si bateau horizontal
                for s in range(tabposition[num][1], tabposition[num][1]+ tabposition[num][4]): #du début du bateau jusqu'à cette première case + la longueur du bateau
                    tableau[i][s] = -3              #on donne la valeur -3 à tout le bateau
            else :                                  #si bateau vertical, pareil que pour horizontal
                for s in range(tabposition[num][0], tabposition[num][0]+ tabposition[num][4]):
                    tableau[s][j] = -3
            nb_coule2=nb_coule2 + 1                 #variable indiquant les bateaux coulés augmente
        else :                                      #sinon bateau touché
            tabposition[num][3] = tabposition[num][3]-1 #décrémentation dans le tabposition
            tableau[i][j] = -2                      #on donne une case bateau touché = -2
     
     
    

################################################################################################################################################################  
################################################################################################################################################################

            #DEF AFFICHAGE
            


def affichage(tableau, tableau_bouton):
    global nombre_tours, nombre_coups,coups_restants,Compteur, nb_gagne, nb_coule2, nb_coule
    
    
    if nb_gagne==nb_coule :                 #Si le nombre bateaux coulés est egal au nombre de bateaux alors la partie est gagnée 
        
        partie_gagnee()
        
        
    elif nombre_tours==nombre_coups :       #Si le nombre de coups déja fait est egal aux nombres de coups max alors la partie est perdue
        
        partie_perdue()
        
    else:                                   #si ni l'une ni l'autre des deux fonctions precedentes alors la grlle se réaffiche avec le coup précedement fait
        for i in range (a):                 
            for j in range (b):
                if tableau[i][j]==-1:   #raté
                    tableau_bouton[i][j]= Button(cadre1, image = photo1,width=50, height = 50).grid(row=i, column=j)
                
                if tableau[i][j]==-2:   #touché
                    tableau_bouton[i][j]= Button(cadre1, image = photo3,width=50, height = 50).grid(row=i, column=j)
                    
                if tableau[i][j]==-3:   #coulé
                    tableau_bouton[i][j]= Button(cadre1, image = photo2,width=50, height = 50).grid(row=i, column=j)
                
   
                    
    nb_coule = nb_coule2                    #COMPTEUR 
    nombre_coups = nombre_coups+1
    coups_restants = nombre_tours-nombre_coups
    coups_.pack()
    coups_.place(x=100,y=900)
    Compteur = Label(fenetre,text=coups_restants,font='Univers',height=1,bg='#55aadd')
    Compteur.pack()
    Compteur.place(x=210,y=900)
    print ("nbcps",nombre_coups,"nbtrs",nombre_tours,'nbrest',coups_restants,'nbcoule',nb_coule2, )
    
    
    
    
    
    
def partie_perdue():
    global nombre_tours,nombre_coups
    
    
    Bouton_Retour_Choix_Grille.pack()                                          
    Bouton_Retour_Choix_Grille.place(x=950, y=350)                              #Placement des elements utilisés avec pack
    
    image_perdu.pack()
    image_perdu.place(x=600,y=335)
    
    Bouton_Quitter.pack()
    Bouton_Quitter.place(x=950, y=500)
    
    
    nombre_coups = 0                                                            #réinitialisation des variables
    
    
    
    
    
def partie_gagnee():
    global nombre_tours,nombre_coups
                                           
    
    Bouton_Retour_Choix_Grille.pack()                                           
    Bouton_Retour_Choix_Grille.place(x=950, y=350)                              #Placement des elements utilisés avec pack
    
    image_gagne.pack()
    image_gagne.place(x=600,y=335)
    
    Bouton_Quitter.pack()
    Bouton_Quitter.place(x=950, y=500)
    
    
    nombre_coups = 0                                                            #réinitialisation des variables
    
    
    
    
    
    
def Difficile(a,b):
    global nombre_tours,nombre_coup,nb_gagne,nb_coule,nombre_coups
    

    nb_gagne = 5                                                                #mise a jour des termes de la partie 
    
    a = 10
    b = 10
    
    nombre_tours = 30    #nombre de coups max
    nombre_coups = 0     #nombre de coups faits
    
    grille_axb(a,b)      #initialisation de la def grille
    print (a,b)   
    
def Moyen(a,b):
    global nombre_tours,nombre_coups,nb_gagne,nb_coule,nombre_coups
    
    
    nb_gagne = 5                                                                #mise a jour des termes de la partie 
    
    a = 10
    b = 10
    
    nombre_tours = 40    #nombre de coups max
    nombre_coups = 0     #nombre de coups faits
    
    grille_axb(a,b)      #initialisation de la def grille
    print (a,b)
 
def Facile(a,b):
    global nombre_tours, nombre_coups,nb_gagne,nb_coule,nombre_coups
    
    
    nb_gagne = 5                                                                #mise a jour des termes de la partie 
    
    a = 10
    b = 10
    
    nombre_tours = 50    #nombre de coups max
    nombre_coups = 0     #nombre de coups faits
    
    grille_axb(a,b)      #initialisation de la def grille
    print (a,b)
    
    
    
    
    
    
def grille_axb(a,b):
    global fenetre,Bouton_Grille1,Bouton_Grille2,Bouton_Retour_Choix_Grille,cadre1
    
    Bouton_Facile.pack()                                                        #Disparition des elements dont on ne se sert plus avec pack_forget
    Bouton_Moyen.pack()             
    Bouton_Difficile.pack()
    
    Bouton_Facile.pack_forget()
    Bouton_Moyen.pack_forget()
    Bouton_Difficile.pack_forget()
    
    Bouton_Retour_Menu.pack()
    Bouton_Retour_Menu.pack_forget()
    
    Bouton_Retour_Choix_Grille.pack()                                            #Placement des elements utilisés avec pack
    Bouton_Retour_Choix_Grille.place(x=700, y=500)
    
    
    tableau_bouton= a*[0]                                                        #création de la grille de boutons
    for i in range(a):
        tableau_bouton[i] = b*[0]                               
    for i in range(a):
        for j in range(b):
            tableau_bouton[i][j] = Button(cadre1, image = photo,width=50, height = 50
                          ,command=lambda i=i, j=j:(test_touchecoule(i, j),affichage(tableau,tableau_bouton)
                          ,affiche_grille(tableau))).grid(row=i, column=j)
                                
    
    cadre1.pack                                                                  #affichage du canvas dans lequel est la grille
    cadre1.place(x=20,y=50)
    time.sleep(0.2)
    
    
    PlaySound('audio/musique_jeu.wav', SND_ASYNC | SND_ALIAS | SND_LOOP)
   

    
    
    
def choix_grille():
    global fenetre,Bouton_Jouer,Bouton_Quitter
    
    Bouton_Jouer.pack()                                                          #Disparition des elements dont on ne se sert plus avec pack_forget                 
    Bouton_Jouer.pack_forget()
  
    Bouton_Quitter.pack()
    Bouton_Quitter.pack_forget()
    
    Bouton_Facile.pack()                                                         #Placement des elements utilisés avec pack
    Bouton_Facile.place(x=500, y=400)
    
    Bouton_Moyen.pack()
    Bouton_Moyen.place(x=700, y=400)
    
    Bouton_Difficile.pack()
    Bouton_Difficile.place(x=900, y=400)
 
    Bouton_Retour_Menu.pack()
    Bouton_Retour_Menu.place(x=900, y=600)
    
    
    
    
def retour_choix_grille():
    global fenetre,tableau,cadre,Bouton_Retour_Choix_Grille,tableau_bouton,nombre_coups,nombre_tours, nb_coule2, nb_coule
    
    cadre1.pack()                                                                #Disparition des elements dont on ne se sert plus avec pack_forget
    cadre1.pack_forget()
    
    image_gagne.pack()
    image_gagne.pack_forget()
    
    image_perdu.pack()
    image_perdu.pack_forget()
    
    Bouton_Retour_Choix_Grille.pack()
    Bouton_Retour_Choix_Grille.pack_forget()
    
    Bouton_Quitter.pack()
    Bouton_Quitter.pack_forget()
    
    Bouton_Facile.pack()                                                         #Placement des elements utilisés avec pack
    Bouton_Facile.place(x=500, y=400)
    
    Bouton_Moyen.pack()
    Bouton_Moyen.place(x=700, y=400)
    
    Bouton_Difficile.pack()
    Bouton_Difficile.place(x=900, y=400)
    
    Bouton_Retour_Menu.pack()
    Bouton_Retour_Menu.place(x=900, y=600)
    

    
    for i in range (a) :                                                        
        for j in range (b) :
            tableau[i][j] = 0
            


    placer(5)                                                                   #placement des bateaux et réaffichage de la grille
    placer(4)
    placer(3)
    placer(3)
    placer(2)
    
    nombre_tours==0                                                             #Réinitalisation des variables pour chaques parties
    nb_coule=0
    nb_coule2=0

def retour_Menu():
    
    Bouton_Facile.pack()                                                        #Disparition des elements dont on ne se sert plus avec pack_forget
    Bouton_Facile.pack_forget()
    
    Bouton_Moyen.pack()
    Bouton_Moyen.pack_forget()
    
    Bouton_Difficile.pack()
    Bouton_Difficile.pack_forget()
    
    Bouton_Jouer.pack()                                                         #Placement des elements utilisés avec pack
    Bouton_Jouer.place(x=700, y=350)
    
    Bouton_Quitter.pack()
    Bouton_Quitter.place(x=950, y=350)

    Bouton_Retour_Menu.pack()
    Bouton_Retour_Menu.pack_forget()
    
    
    

################################################################################################################################################################# 
#################################################################################################################################################################


                #MAIN PROG

#FENETRE D'ACCUEIL et initialisation de tout les packs





fenetre = Tk.Tk()                                                               #création fenetre
fenetre.title("Crapouillotage")
fenetre.resizable(width=False, height=False)
fenetre.geometry("1280x960")



photologo=Tk.PhotoImage(file ='Images/logo.gif')                                #initialisation des images          

photo6=Tk.PhotoImage(file ='Images/Accueil.gif')

photo=Tk.PhotoImage(file ='Images/blanc.gif')

photo1=Tk.PhotoImage(file ='Images/raté.gif')

photo2=Tk.PhotoImage(file ='Images/touché.gif')

photo3=Tk.PhotoImage(file ='Images/coulé.gif')

photo4=Tk.PhotoImage(file ='Images/gagné.gif')

photo5=Tk.PhotoImage(file='Images/perdu.gif')



                #CREATION DU MENU JOUER_QUITTER


label = Tk.Label(image = photo6)                                                #Image de fond         
label.place(x = 0 , y = 0)

label = Tk.Label(image = photologo)                                             #Image logo
label.place(x = 700 , y = 40)


Bouton_Jouer = Button(fenetre,height=5,width=20,font='Raavi',text='JOUER',relief=GROOVE
                      ,borderwidth=2
                      ,command=lambda: [son_boutons_next(),choix_grille()],bg="#B50D0D")
Bouton_Jouer.pack()
Bouton_Jouer.place(x=700, y=350)
Bouton_Quitter = Button(fenetre,height=5,width=20,font='Raavi',relief=GROOVE,text="QUITTER"
                        ,borderwidth=2
                        ,command =lambda: [son_boutons_retour(),fenetre.destroy()],bg="grey")
Bouton_Quitter.pack()
Bouton_Quitter.place(x=950, y=350)


                #CREATION DES VARIABLES DE LA CONSOLE

a=10
b=10

tableau = a*[0]
for i in range (a) :
    tableau[i] = b*[0]
    
tabposition = 100*[0]
for i in range (100) :
    tabposition[i] = 5*[0]

numero_bato = 1

placer(5)      #appelation de la def placer dans la console
placer(4)
placer(3)
placer(3)
placer(2)
       

                #BARRE DU HAUT POUR QUITTER



menubar = Menu(fenetre)
menu1 = Menu(menubar, tearoff=0)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.destroy)
menubar.add_cascade(label="Fichier", menu=menu1)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar) 



                #INITIALISATION DES DIFFERENTS BOUTONS/LABELS/CANVAS


image_gagne = Tk.Label(image = photo4)


image_perdu = Tk.Label(image = photo5)




Bouton_Facile= Button(fenetre,height=5, width=20 ,font='Raavi', relief=GROOVE, text= "FACILE" 
                       ,borderwidth=2
                       ,command = lambda: [son_boutons_next(),Facile(a,b)] 
                       ,bg="#B50D0D"  )


Bouton_Moyen= Button(fenetre,height=5, width=20 ,font='Raavi', relief=GROOVE, text="MOYEN"
                       ,borderwidth=2
                       ,command = lambda:[son_boutons_next(),Moyen(a,b)]
                       ,bg="#B50D0D")


Bouton_Difficile= Button(fenetre,height=5, width=20 ,font='Raavi', relief=GROOVE, text='DIFFICILE'
                        , borderwidth=2
                       ,command = lambda:[son_boutons_next(),Difficile(a,b)]
                       ,bg="#B50D0D")


Bouton_Retour_Choix_Grille= Button(fenetre, height=5, width=20 ,font='Raavi', relief=GROOVE, text= "RETOUR GRILLE" 
                       ,borderwidth=2
                       ,command = lambda:[son_boutons_retour(),retour_choix_grille()] 
                       ,bg="grey"  )


Bouton_Retour_Menu= Button(fenetre, height=5, width=20 ,font='Raavi', relief=GROOVE, text= "RETOUR MENU" 
                       ,borderwidth=2
                       ,command = lambda:[son_boutons_retour(),retour_Menu()] 
                       ,bg="grey"  )


cadre1= Canvas(fenetre, bg="grey") 
coups_= Label(fenetre,text= 'coups restants: ', font='Univers',bg='#55aadd')


                #INITIALISTAUION DES VARIABLES 


nombre_tours = 0
nombre_coups = 0
nb_gagne = 0 
nb_coule = 0
nb_coule2 = 0 
coups_restants = 0



fenetre.mainloop()




#####################
#####################



# DEBUT



affiche_grille(tableau)

for i in range (numero_bato) :
    for j in range (5) :
        print(tabposition[i][j], end=' ')
    print(sep=" ")


#for s in range (1) :
#    v = random.randint(0, 9)
#    r = random.randint(0, 9)
#    test_sylvain(v, r)
    
#for i in range (b) :
#    for j in range (a) :
#        test_sylvain(i, j)

affiche_grille(tableau)

for i in range (numero_bato) :
    for j in range (5) :
        print(tabposition[i][j], end=' ')
print(sep=" ")