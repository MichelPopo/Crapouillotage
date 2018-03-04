from tkinter import*
import tkinter as Tk

a=1 #on crée une variable, initalisée à 1
def changer_le_fond(): #on crée une fonction
    global a           #on définit que a est du type global, cela signifie que sa valeur peut être modifiée à l'interieur de la fonction et que nous gardons cette nouvelle valeur, on pourra donc relancer plusieurs fois la fonction avec une valeur différente de a
    if a>0: #on lit la valeur de a en fonction elle rentre soit dans le if soit dans le elif
        fenetre.config(bg="green") #on change de couleur le fond de la fenêtre
        Texte.config(text="fond vert") #on change le texte
        Texte.config(bg="blue") #on change la couleur de la zone de texte
        a=a*(-1) #en mutltipliant par -1, on chnage le signe de a, donc après cette ligne, a=1*(-1) donc a=-1 et passe dans le elif
    elif a<0: #si la valeur est cette fois ci inferieur à 0 elle rentre dans le elif
        fenetre.config(bg="yellow") #on change de couleur le fond de la fenêtre
        Texte.config(text="fond jaune") #on change le texte
        Texte.config(bg="white") #on change la couleur de la zone de texte
        a=a*(-1) #pareil que dans le if, en multipliant, a passe de -1 à 1 et ne rempli plus la condition du elif, elle rentrera donc dans le if lorsque la fonction sera relancée
        

fenetre=Tk.Tk() #on crée une fenêtre
fenetre.geometry("500x600") #on choisit la taille de la fenêtre
fenetre.resizable(width=False,  height=False)
fenetre.config(bg="yellow") #on choisit une couleur au fond de la fenêtre 
Texte = Tk.Label(fenetre,  text="fond jaune",  bg="white") #on crée une zone de texte
Texte.place(x=210,  y=125) #on positionne le texte
Texte.config(bg="white") #on choisit la couleur du fond de la zone de texte
Bouton_valider = Button(fenetre, text = "appuyer pour changer la couleur", command = changer_le_fond, bg = "red") #création d'un bouton, lorsqu'il est activé il appelle la fonction "chnager_le_fond", on définit la couleur et le texte placé sur le bouton
Bouton_valider.place(x=140,y=150) #on positionne ensuite le bouton

fenetre.mainloop() #on lance ensuite la fenêtre
