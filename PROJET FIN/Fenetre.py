from tkinter import * 
import tkinter as Tk 
from PIL import Image
from wave import *
import tkinter.font as tkFont
from winsound import *
import time


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
    
    
    
    
    
    
    
     #SON  
        
       
def son_boutons_next(): 
    PlaySound('C:/Users/Sylvain/Documents/Etudes/Terminale/ISN/PROJET/audio/audio_bouton_next.wav', SND_ASYNC | SND_FILENAME)       

def son_boutons_retour():
    PlaySound('C:/Users/Sylvain/Documents/Etudes/Terminale/ISN/PROJET/audio/audio_bouton_retour.wav', SND_ASYNC | SND_FILENAME)




    
    
        
        #MENU 
 
    
    
    
    
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
    cadre1.place(x=100,y=150)
    Tableau= 10*[0]
    for i in range(10):
        Tableau[i] = 10*[0]
    for i in range(10):
        for j in range(10):
            Tableau[i][j] = Button(cadre1, image = photo,width=50, height = 50, command=lambda i=i, j=j: position(i, j)).grid(row=i, column=j)
    time.sleep(1)
    PlaySound('C:/Users/Sylvain/Documents/Etudes/Terminale/ISN/PROJET/musique_jeu.wav', SND_ASYNC | SND_ALIAS | SND_LOOP)
    
def grille6x6():
    global fenetre,Bouton_Grille1,Bouton_Grille2,Bouton_Retour_Choix_Grille,cadre

    Bouton_Grille1.pack()
    Bouton_Grille2.pack()
    
    Bouton_Grille1.pack_forget()
    Bouton_Grille2.pack_forget()
    
    Bouton_Retour_Menu.pack()
    Bouton_Retour_Menu.pack_forget()
    
    Bouton_Retour_Choix_Grille.pack()
    Bouton_Retour_Choix_Grille.place(x=700, y=500)
    
    cadre2.pack
    cadre2.place(x=100,y=150)
    
    Tableau= 6*[0]
    for i in range(6):
        Tableau[i] = 6*[0]
    for i in range(6):
        for j in range(6):
            Tableau[i][j] = Button(cadre2, image = photo,width=50, height = 50, command=lambda i=i, j=j: position(i, j)).grid(row=i, column=j)
    time.sleep(1)
    PlaySound('C:/Users/Sylvain/Documents/Etudes/Terminale/ISN/PROJET/musique_jeu.wav', SND_ASYNC | SND_FILENAME | SND_LOOP)
    
    
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
    global fenetre,Tableau,cadre,Bouton_Retour_Choix_Grille
    
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


logo=Image.open("C:/Users/Sylvain/Documents/Etudes/Terminale/ISN/PROJET/images/logo.png") #Importation image blanc de debut
logo.save('logo.gif','GIF')
photologo=Tk.PhotoImage(file ='logo.gif')

Accueil=Image.open("C:/Users/Sylvain/Documents/Etudes/Terminale/ISN/PROJET/images/Accueil2.png") #Importation image blanc de debut
Accueil.save('Accueil.gif','GIF')
photo6=Tk.PhotoImage(file ='Accueil.gif')

label = Tk.Label(image = photo6) 
label.place(x = 0 , y = 0)

label = Tk.Label(image = photologo) 
label.place(x = 700 , y = 40)


Bouton_Jouer = Button(fenetre,height=5,width=20,font='Raavi',relief=GROOVE,text= "JOUER",borderwidth=3,command= lambda: [son_boutons_next(),choix_grille()],bg="#B50D0D")
Bouton_Jouer.pack()
Bouton_Jouer.place(x=700, y=350)
Bouton_Quitter = Button(fenetre,height=5,width=20,font='Raavi',relief=GROOVE,text="QUITTER",borderwidth=3,command = lambda:[son_boutons_retour(),fenetre.destroy()],bg="grey")
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


coule=Image.open("C:/Users/Sylvain/Documents/Etudes/Terminale/ISN/PROJET/images/coulé.png") #Importation image blanc de debut
coule.save('coulé.gif','GIF')
photo3=Tk.PhotoImage(file ='coulé.gif')


rate=Image.open("C:/Users/Sylvain/Documents/Etudes/Terminale/ISN/PROJET/images/raté.png") #Importation image blanc de debut
rate.save('raté.gif','GIF')
photo1=Tk.PhotoImage(file ='raté.gif')


blanc=Image.open("C:/Users/Sylvain/Documents/Etudes/Terminale/ISN/PROJET/images/blanc.png") #Importation image blanc de debut
blanc.save('blanc.gif','GIF')
photo=Tk.PhotoImage(file ='blanc.gif')


touche=Image.open("C:/Users/Sylvain/Documents/Etudes/Terminale/ISN/PROJET/images/touché.png") #importation image croix de fin 
touche.save('touché.gif','GIF')
photo2=Tk.PhotoImage(file ='touché.gif')


Bouton_Grille1= Button(fenetre,height=5, width=20 ,font='Raavi', relief=GROOVE, text= "GRILLE 10x10" 
                       ,borderwidth=3
                       ,command = lambda: [son_boutons_next(),grille10x10()] ,bg="#B50D0D"  )

Bouton_Grille2= Button(fenetre,height=5, width=20 ,font='Raavi', relief=GROOVE, text="GRILLE 6x6"
                       ,borderwidth=3
                       ,command = lambda:[son_boutons_next(),grille6x6()] ,bg="#B50D0D")

Bouton_Retour_Choix_Grille= Button(fenetre, height=5, width=20 ,font='Raavi', relief=GROOVE, text= "RETOUR GRILLE" 
                       ,borderwidth=3
                       ,command = lambda:[son_boutons_retour(),retour_choix_grille()] ,bg="grey"  )

Bouton_Retour_Menu= Button(fenetre, height=5, width=20 ,font='Raavi', relief=GROOVE, text= "RETOUR MENU" 
                       ,borderwidth=3
                       ,command = lambda:[son_boutons_retour(),retour_Menu()] ,bg="grey"  )

cadre1= Canvas(fenetre, bg="grey") 
cadre2= Canvas(fenetre, bg="grey")

fenetre.mainloop()
