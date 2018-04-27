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

                                          #FONCTIONS#
    
def alert():
    showinfo("alerte", "Bravo!")  
    
#SON  


def son_boutons_next(): 
    PlaySound('U:/theo.boyer/ISN/Crapouillotage-master/audio/audio_bouton_next.wav', SND_ASYNC | SND_FILENAME)       

def son_boutons_retour():
    PlaySound('U:/theo.boyer/ISN/Crapouillotage-master/audio/audio_bouton_retour.wav', SND_ASYNC | SND_FILENAME)
    
          

#Placement des bateaux dans la console        
def placer (x):
    global numero_bato, tabposition
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
     

def affichage(tableau, tableau_bouton):
    
    for i in range (a):
        for j in range (b):
            if tableau[i][j]==-1:
                tableau_bouton[i][j]= Button(cadre1, image = photo1,width=50, height = 50).grid(row=i, column=j)
                
            if tableau[i][j]==-2:
                tableau_bouton[i][j]= Button(cadre1, image = photo2,width=50, height = 50).grid(row=i, column=j)
                
            if tableau[i][j]==-3:
                tableau_bouton[i][j]= Button(cadre1, image = photo3,width=50, height = 50).grid(row=i, column=j)



def Difficile(a,b):
    a = 10
    b = 10
    grille_axb(a,b)
    print (a,b)
    
    
    tableau = a*[0]
    for i in range (a) :
        tableau[i] = b*[0]
    
    tabposition = 10*[0]
    for i in range (10) :
        tabposition[i] = 5*[0]
        
    numero_bato = 1
    
    
def Moyen(a,b):
    a = 10
    b = 10
    grille_axb(a,b)
    print (a,b)
    
    tableau = a*[0]
    for i in range (a) :
        tableau[i] = b*[0]
    
    tabposition = 10*[0]
    for i in range (10) :
        tabposition[i] = 5*[0]
        
    numero_bato = 1
    
    
def Facile(a,b):
    a = 10
    b = 10
    grille_axb(a,b)
    print (a,b)
    
    tableau = a*[0]
    for i in range (a) :
        tableau[i] = b*[0]
    
    tabposition = 10*[0]
    for i in range (10) :
        tabposition[i] = 5*[0]
        
    numero_bato = 1
    
def grille_axb(a,b):
    global fenetre,Bouton_Grille1,Bouton_Grille2,Bouton_Retour_Choix_Grille,cadre1
    
    Bouton_Facile.pack()
    Bouton_Moyen.pack()
    Bouton_Difficile.pack()
    
    Bouton_Facile.pack_forget()
    Bouton_Moyen.pack_forget()
    Bouton_Difficile.pack_forget()
    
    Bouton_Retour_Menu.pack()
    Bouton_Retour_Menu.pack_forget()
    
    Bouton_Retour_Choix_Grille.pack()
    Bouton_Retour_Choix_Grille.place(x=700, y=500)
    
    
    tableau_bouton= a*[0]
    for i in range(a):
        tableau_bouton[i] = b*[0]
    for i in range(a):
        for j in range(b):
            tableau_bouton[i][j] = Button(cadre1, image = photo,width=50, height = 50
                          ,command=lambda i=i, j=j:(test_sylvain(i, j),affichage(tableau,tableau_bouton), affiche_grille(tableau))).grid(row=i, column=j)
    
    
    cadre1.pack 
    cadre1.place(x=20,y=50)
    time.sleep(0.2)
    
    
    PlaySound('U:/theo.boyer/ISN/Crapouillotage-master/musique_jeu.wav', SND_ASYNC | SND_ALIAS | SND_LOOP)
   
def choix_grille():
    global fenetre,Bouton_Jouer,Bouton_Quitter,Bouton_Grille1,Bouton_Grille2
    
    Bouton_Jouer.pack()
    Bouton_Jouer.pack_forget()
    
    Bouton_Quitter.pack()
    Bouton_Quitter.pack_forget()
    
    Bouton_Facile.pack()
    Bouton_Facile.place(x=500, y=400)
    
    Bouton_Moyen.pack()
    Bouton_Moyen.place(x=700, y=400)
    
    Bouton_Difficile.pack()
    Bouton_Difficile.place(x=900, y=400)
 
    Bouton_Retour_Menu.pack()
    Bouton_Retour_Menu.place(x=900, y=600)
    
    
def retour_choix_grille():
    global fenetre,tableau,cadre,Bouton_Retour_Choix_Grille,tableau_bouton
    
    cadre1.pack()
    cadre1.pack_forget()
    
    Bouton_Facile.pack()
    Bouton_Facile.place(x=500, y=400)
    
    Bouton_Moyen.pack()
    Bouton_Moyen.place(x=700, y=400)
    
    Bouton_Difficile.pack()
    Bouton_Difficile.place(x=900, y=400)
    
    Bouton_Retour_Choix_Grille.pack()
    Bouton_Retour_Choix_Grille.pack_forget()
    
    Bouton_Retour_Menu.pack()
    Bouton_Retour_Menu.place(x=900, y=600)
    
    for i in range (a) :
        for j in range (b) :
            tableau[i][j] = 0
            
    placer(5)
    placer(4)
    placer(3)
    placer(3)
    placer(2)
    placer(8)
    placer(8)
    
    
    
def retour_Menu():
    
    Bouton_Facile.pack()
    Bouton_Facile.pack_forget()
    
    Bouton_Moyen.pack()
    Bouton_Moyen.pack_forget()
    
    Bouton_Difficile.pack()
    Bouton_Difficile.pack_forget()
    
    Bouton_Jouer.pack()
    Bouton_Jouer.place(x=700, y=350)
    
    Bouton_Quitter.pack()
    Bouton_Quitter.place(x=950, y=350)

    Bouton_Retour_Menu.pack()
    Bouton_Retour_Menu.pack_forget()
    
    

##############################################################################  
##############################################################################

                                #DEBUT-PROGRAMME#

#FENETRE D'ACCUEIL et initialisation de tout les packs


fenetre = Tk.Tk()
fenetre.title("Crapouillotage")
fenetre.resizable(width=False, height=False)
fenetre.geometry("1280x960")

photologo=Tk.PhotoImage(file ='Images/logo.gif')

photo6=Tk.PhotoImage(file ='Images/Accueil.gif')

label = Tk.Label(image = photo6) 
label.place(x = 0 , y = 0)

label = Tk.Label(image = photologo) 
label.place(x = 700 , y = 40)

a=10
b=10

tableau = a*[0]
for i in range (a) :
    tableau[i] = b*[0]
    
tabposition = 30*[0]
for i in range (30) :
    tabposition[i] = 5*[0]

numero_bato = 1

placer(5)
placer(4)
placer(3)
placer(3)
placer(2)
placer(8)
placer(8)


Bouton_Jouer = Button(fenetre,height=5,width=20,text='JOUER', font='Univers',relief=GROOVE,borderwidth=3
                      ,command=lambda: [son_boutons_next(),choix_grille()],bg="#B50D0D")
Bouton_Jouer.pack()
Bouton_Jouer.place(x=700, y=350)
Bouton_Quitter = Button(fenetre,height=5,width=20,font='Univers',relief=GROOVE,text="QUITTER",borderwidth=3
                        ,command =lambda: [son_boutons_retour(),fenetre.destroy()],bg="grey")
Bouton_Quitter.pack()
Bouton_Quitter.place(x=950, y=350)

            

menubar = Menu(fenetre)


menu1 = Menu(menubar, tearoff=0)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.destroy)
menubar.add_cascade(label="Fichier", menu=menu1)


menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar) 



photo=Tk.PhotoImage(file ='Images/blanc.gif')

photo1=Tk.PhotoImage(file ='Images/raté.gif')

photo2=Tk.PhotoImage(file ='Images/touché.gif')

photo3=Tk.PhotoImage(file ='Images/coulé.gif')



Bouton_Facile= Button(fenetre,height=5, width=20 ,font='Raavi', relief=GROOVE, text= "FACILE" 
                       ,borderwidth=3
                       ,command = lambda: [son_boutons_next(),Facile(a,b)] 
                       ,bg="#B50D0D"  )


Bouton_Moyen= Button(fenetre,height=5, width=20 ,font='Raavi', relief=GROOVE, text="MOYEN"
                       ,borderwidth=3
                       ,command = lambda:[son_boutons_next(),Moyen(a,b)]
                       ,bg="#B50D0D")


Bouton_Difficile= Button(fenetre,height=5, width=20 ,font='Raavi', relief=GROOVE, text='DIFFICILE'
                       ,command = lambda:[son_boutons_next(),Difficile(a,b)]
                       ,bg="#B50D0D")


Bouton_Retour_Choix_Grille= Button(fenetre, height=5, width=20 ,font='Raavi', relief=GROOVE, text= "RETOUR GRILLE" 
                       ,borderwidth=3
                       ,command = lambda:[son_boutons_retour(),retour_choix_grille()] 
                       ,bg="grey"  )


Bouton_Retour_Menu= Button(fenetre, height=5, width=20 ,font='Raavi', relief=GROOVE, text= "RETOUR MENU" 
                       ,borderwidth=3
                       ,command = lambda:[son_boutons_retour(),retour_Menu()] 
                       ,bg="grey"  )


cadre1= Canvas(fenetre, bg="grey") 


 
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
