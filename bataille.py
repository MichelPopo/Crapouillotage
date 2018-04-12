import os    #efface la console
os.system("cls") 
import random
from copy import deepcopy



from tkinter import * 
import tkinter as Tk 
from PIL import Image
import tkinter.font as tkFont
import time

a = 12
b = 12

tableau = a*[0]
for i in range (a) :
    tableau[i] = b*[0]
    
tabposition = 10*[0]
for i in range (10) :
    tabposition[i] = 5*[0]

numero_bato = 1

    #LE BATÔ LA
    
def alert():
    showinfo("alerte", "Bravo!")
    

def position(i,j):
    global tableau
    print(i , " " , j)
    
    
def affichage(tableau, tableau_bouton):
    for i in range (a):
        for j in range (b):
            if tableau[i][j]==-1:
                tableau_bouton[i][j]= Button(cadre1, image = photo1,width=50, height = 50).grid(row=i, column=j)
            if tableau[i][j]==-2:
                tableau_bouton[i][j]= Button(cadre1, image = photo2,width=50, height = 50).grid(row=i, column=j)
            if tableau[i][j]==-3:
                tableau_bouton[i][j]= Button(cadre1, image = photo3,width=50, height = 50).grid(row=i, column=j)
    
    
    
    
    
    
    
     #SON  

     




    
    
        
        #MENU 
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
    

placer(4)
placer(5)
placer(3)
placer(2)
placer(2)
placer(8)
placer(4)
    
    
    
def grille10x10():
    global fenetre,Bouton_Grille1,Bouton_Grille2,Bouton_Retour_Choix_Grille,cadre
    
    Bouton_Grille1.pack()
    Bouton_Grille2.pack()
    
    Bouton_Grille1.pack_forget()
    Bouton_Grille2.pack_forget()
    
    Bouton_Retour_Menu.pack()
    Bouton_Retour_Menu.pack_forget()
    
    Bouton_Retour_Choix_Grille.pack()
    Bouton_Retour_Choix_Grille.place(x=700, y=500)
    
    cadre1.pack 
    cadre1.place(x=20,y=50)
    tableau_bouton= a*[0]
    for i in range(a):
        tableau_bouton[i] = b*[0]
    for i in range(a):
        for j in range(b):
            tableau_bouton[i][j] = Button(cadre1, image = photo,width=50, height = 50, command=lambda i=i, j=j:(test_sylvain(i, j),affichage(tableau,tableau_bouton), affiche_grille(tableau))).grid(row=i, column=j)
    time.sleep(1)


# def grille6x6():
#     global fenetre,Bouton_Grille1,Bouton_Grille2,Bouton_Retour_Choix_Grille,cadre

#     Bouton_Grille1.pack()
#     Bouton_Grille2.pack()
    
#     Bouton_Grille1.pack_forget()
#     Bouton_Grille2.pack_forget()
    
#     Bouton_Retour_Menu.pack()
#     Bouton_Retour_Menu.pack_forget()
    
#     Bouton_Retour_Choix_Grille.pack()
#     Bouton_Retour_Choix_Grille.place(x=700, y=500)
    
#     cadre2.pack
#     cadre2.place(x=100,y=150)
    
#     tableau_bouton= 6*[0]
#     for i in range(6):
#         tableau_bouton[i] = 6*[0]
#     for i in range(6):
#         for j in range(6):
#             tableau_bouton[i][j] = Button(cadre2, image = photo,width=50, height = 50, command=lambda i=i, j=j: position(i, j), affichage_grille)).grid(row=i, column=j)
#     time.sleep(1)
    
    
    
def choix_grille():
    global fenetre,Bouton_Jouer,Bouton_Quitter,Bouton_Grille1,Bouton_Grille2
    
    Bouton_Jouer.pack()
    Bouton_Jouer.pack_forget()
    
    Bouton_Quitter.pack()
    Bouton_Quitter.pack_forget()
    
    Bouton_Grille1.pack()
    Bouton_Grille1.place(x=700, y=400)
    
    Bouton_Grille2.pack()
    Bouton_Grille2.place(x=900, y=400)
 
    Bouton_Retour_Menu.pack()
    Bouton_Retour_Menu.place(x=900, y=600)
    
    
def retour_choix_grille():
    global fenetre,tableau,cadre,Bouton_Retour_Choix_Grille
    
    cadre1.pack()
    cadre1.pack_forget()
    cadre2.pack()
    cadre2.pack_forget()
    
    
    Bouton_Grille1.pack()
    Bouton_Grille1.place(x=700, y=400)
    
    Bouton_Grille2.pack()
    Bouton_Grille2.place(x=900, y=400)
    
    Bouton_Retour_Choix_Grille.pack()
    Bouton_Retour_Choix_Grille.pack_forget()
    
    Bouton_Retour_Menu.pack()
    Bouton_Retour_Menu.place(x=900, y=600)


def retour_Menu():
    
    Bouton_Grille1.pack()
    Bouton_Grille1.pack_forget()
    Bouton_Grille2.pack()
    Bouton_Grille2.pack_forget()
    
    Bouton_Jouer.pack()
    Bouton_Jouer.place(x=700, y=350)
    
    Bouton_Quitter.pack()
    Bouton_Quitter.place(x=950, y=350)

    Bouton_Retour_Menu.pack()
    Bouton_Retour_Menu.pack_forget()




#FENETRE D'ACCUEIL et initialisation de tout les packs

fenetre = Tk.Tk()
fenetre.title("Crapouillotage")
fenetre.resizable(width=False, height=False)
fenetre.geometry("1280x960")


#logo=Image.open("C:/Users/Sylvain/Documents/Etudes/Terminale/ISN/PROJET/images/logo.png") #Importation image blanc de debut
#logo.save('logo.gif','GIF')
photologo=Tk.PhotoImage(file ='Images/logo.gif')

#Accueil=Image.open("C:/Users/Sylvain/Documents/Etudes/Terminale/ISN/PROJET/images/Accueil2.png") #Importation image blanc de debut
#Accueil.save('Accueil.gif','GIF')
photo6=Tk.PhotoImage(file ='Images/Accueil.gif')

label = Tk.Label(image = photo6) 
label.place(x = 0 , y = 0)

label = Tk.Label(image = photologo) 
label.place(x = 700 , y = 40)


Bouton_Jouer = Button(fenetre,height=5,width=20,font='Raavi',relief=GROOVE,text= "JOUER",borderwidth=3,command=choix_grille,bg="#B50D0D")
Bouton_Jouer.pack()
Bouton_Jouer.place(x=700, y=350)
Bouton_Quitter = Button(fenetre,height=5,width=20,font='Raavi',relief=GROOVE,text="QUITTER",borderwidth=3,command = fenetre.destroy,bg="grey")
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


#coule=Image.open("C:/Users/Sylvain/Documents/Etudes/Terminale/ISN/PROJET/images/coulé.png") #Importation image blanc de debut
#coule.save('coulé.gif','GIF')
photo3=Tk.PhotoImage(file ='Images/coulé.gif')


#rate=Image.open("C:/Users/Sylvain/Documents/Etudes/Terminale/ISN/PROJET/images/raté.png") #Importation image blanc de debut
#rate.save('raté.gif','GIF')
photo1=Tk.PhotoImage(file ='Images/raté.gif')


#blanc=Image.open("C:/Users/Sylvain/Documents/Etudes/Terminale/ISN/PROJET/images/blanc.png") #Importation image blanc de debut
#blanc.save('blanc.gif','GIF')
photo=Tk.PhotoImage(file ='Images/blanc.gif')


#touche=Image.open("C:/Users/Sylvain/Documents/Etudes/Terminale/ISN/PROJET/images/touché.png") #importation image croix de fin 
#touche.save('touché.gif','GIF')
photo2=Tk.PhotoImage(file ='Images/touché.gif')


Bouton_Grille1= Button(fenetre,height=5, width=20 ,font='Raavi', relief=GROOVE, text= "GRILLE 10x10" 
                       ,borderwidth=3
                       ,command =grille10x10 ,bg="#B50D0D"  )

Bouton_Grille2= Button(fenetre,height=5, width=20 ,font='Raavi', relief=GROOVE, text="GRILLE 6x6"
                       ,borderwidth=3
        ,bg="#B50D0D")

Bouton_Retour_Choix_Grille= Button(fenetre, height=5, width=20 ,font='Raavi', relief=GROOVE, text= "RETOUR GRILLE" 
                       ,borderwidth=3
                       ,command =retour_choix_grille ,bg="grey"  )

Bouton_Retour_Menu= Button(fenetre, height=5, width=20 ,font='Raavi', relief=GROOVE, text= "RETOUR MENU" 
                       ,borderwidth=3
                       ,command = retour_Menu ,bg="grey"  )

cadre1= Canvas(fenetre, bg="grey") 
cadre2= Canvas(fenetre, bg="grey")

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
