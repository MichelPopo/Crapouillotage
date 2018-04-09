from tkinter import * 
import tkinter as Tk 
from PIL import Image
from wave import *

    #LE BATÔ LA
    


def alert():
    showinfo("alerte", "Bravo!")
    

def position(i,j):
    global Tableau
    print(i , " " , j)
    
    
def affichage(Tableau):
    for i in range (10):
        for j in range (10):
            if Tableau[i][j]==6:
                Tableau[i][j]= Button(cadre, image = photo1,width=50, height = 50).grid(row=i, column=j)
            if Tableau[i][j]==20 or 30 or 40 or 50:
                Tableau[i][j]= Button(cadre, image = photo2,width=50, height = 50).grid(row=i, column=j)
            if Tableau[i][j]==200 or 300 or 400 or 500:
                Tableau[i][j]= Button(cadre, image = photo3,width=50, height = 50).grid(row=i, column=j)
    
    
    
    
def grille10x10():
    global fenetre,Bouton_Grille1,Bouton_Grille2,Bouton_Retour_Choix_Grille,cadre
    
    Bouton_Grille1.pack()
    Bouton_Grille2.pack()
    
    Bouton_Grille1.pack_forget()
    Bouton_Grille2.pack_forget()
     
    
    Bouton_Retour_Choix_Grille.pack()
    Bouton_Retour_Choix_Grille.place(x=700, y=500)
    
    cadre.pack 
    cadre.place(x=100,y=150)
    Tableau= 10*[0]
    for i in range(10):
        Tableau[i] = 10*[0]
    for i in range(10):
        for j in range(10):
            Tableau[i][j] = Button(cadre, image = photo,width=50, height = 50, command=lambda i=i, j=j: position(i, j)).grid(row=i, column=j)
            
    
def grille6x6():
    global fenetre,Bouton_Grille1,Bouton_Grille2,Bouton_Retour_Choix_Grille,cadre

    Bouton_Grille1.pack()
    Bouton_Grille2.pack()
    
    Bouton_Grille1.pack_forget()
    Bouton_Grille2.pack_forget()
    
    Bouton_Retour_Choix_Grille.pack()
    Bouton_Retour_Choix_Grille.place(x=700, y=500)
    
    cadre.pack
    cadre.place(x=100,y=150)
    Tableau= 6*[0]
    for i in range(6):
        Tableau[i] = 6*[0]
    for i in range(6):
        for j in range(6):
            Tableau[i][j] = Button(cadre, image = photo,width=50, height = 50, command=lambda i=i, j=j: position(i, j)).grid(row=i, column=j)
    
def choix_grille():
    global fenetre,Bouton_Jouer,Bouton_Quitter,Bouton_Grille1,Bouton_Grille2
    
    Bouton_Jouer.pack()
    Bouton_Quitter.pack()
    
    Bouton_Jouer.pack_forget()
    Bouton_Quitter.pack_forget()
    
    Bouton_Grille1.pack()
    Bouton_Grille1.place(x=700, y=400)
    
    
    Bouton_Grille2.pack()
    Bouton_Grille2.place(x=950, y=400)
    
    
    
def retour_choix_grille():
    global fenetre,Tableau,cadre,Bouton_Retour_Choix_Grille
    
    cadre.pack()
    cadre.pack_forget()
    
    Bouton_Grille1.pack()
    Bouton_Grille1.place(x=700, y=600)
    
    Bouton_Grille2.pack()
    Bouton_Grille2.place(x=950, y=600)
    
    Bouton_Retour_Choix_Grille.pack()
    Bouton_Retour_Choix_Grille.pack_forget()




#FENETRE D'ACCUEIL

fenetre = Tk.Tk()
fenetre.title("Crapouillotage")
fenetre.resizable(width=False, height=False)
fenetre.geometry("1280x960")

logo=Image.open("C:/Users/Sylvain/Documents/Etudes/Terminale/ISN/PROJET/logo.png") #Importation image blanc de debut
logo.save('logo.gif','GIF')
photologo=Tk.PhotoImage(file ='logo.gif')


Accueil=Image.open("C:/Users/Sylvain/Documents/Etudes/Terminale/ISN/PROJET/Accueil2.png") #Importation image blanc de debut
Accueil.save('Accueil.gif','GIF')
photo6=Tk.PhotoImage(file ='Accueil.gif')

label = Tk.Label(image = photo6) 
label.place(x = 0 , y = 0)

label = Tk.Label(image = photologo) 
label.place(x = 700 , y = 40)

Bouton_Jouer= Button(fenetre, height=5, width=20 , relief=GROOVE, text= "JOUER" ,borderwidth=3, command = choix_grille ,bg="#B50D0D"  )
Bouton_Jouer.pack()
Bouton_Jouer.place(x=700, y=350)
Bouton_Quitter= Button(fenetre,height=5, width=20 , relief=GROOVE, text="QUITTER", borderwidth=3,command = fenetre.destroy,bg="grey")
Bouton_Quitter.pack()
Bouton_Quitter.place(x=950, y=350)

            
menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=alert)
menu1.add_command(label="Editer", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.destroy)
menubar.add_cascade(label="Fichier", menu=menu1)


menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar) 

coule=Image.open("C:/Users/Sylvain/Documents/Etudes/Terminale/ISN/PROJET/coulé.png") #Importation image blanc de debut
coule.save('coulé.gif','GIF')
photo3=Tk.PhotoImage(file ='coulé.gif')

rate=Image.open("C:/Users/Sylvain/Documents/Etudes/Terminale/ISN/PROJET/raté.png") #Importation image blanc de debut
rate.save('raté.gif','GIF')
photo1=Tk.PhotoImage(file ='raté.gif')

blanc=Image.open("C:/Users/Sylvain/Documents/Etudes/Terminale/ISN/PROJET/blanc.png") #Importation image blanc de debut
blanc.save('blanc.gif','GIF')
photo=Tk.PhotoImage(file ='blanc.gif')

touche=Image.open("C:/Users/Sylvain/Documents/Etudes/Terminale/ISN/PROJET/touché.png") #importation image croix de fin 
touche.save('touché.gif','GIF')
photo2=Tk.PhotoImage(file ='touché.gif')

Bouton_Grille1= Button(fenetre,height=5, width=20 , relief=GROOVE, text= "GRILLE 10x10" ,borderwidth=3, command = grille10x10 ,bg="#B50D0D"  )
Bouton_Grille2= Button(fenetre,height=5, width=20 , relief=GROOVE, text="GRILLE 6x6", borderwidth=3,command = grille6x6 ,bg="grey")
Bouton_Retour_Choix_Grille= Button(fenetre, height=5, width=20 , relief=GROOVE, text= "RETOUR" ,borderwidth=3, command = retour_choix_grille ,bg="#B50D0D"  )
cadre= Canvas(fenetre, bg="grey") 

fenetre.mainloop()
