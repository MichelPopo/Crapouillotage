from tkinter import * 
import tkinter as Tk 
from PIL import Image

fenetre = Tk()
fenetre.title("graphique")
fenetre.resizable(width=False, height=False)
fenetre.geometry("800x800")

def alert():
    showinfo("alerte", "Bravo!")

menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=alert)
menu1.add_command(label="Editer", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)


menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar) 

coule=Image.open("U:/sylvain.rome/ISN/proprojet/coulé.png") #Importation image blanc de debut
coule.save('coulé.gif','GIF')
photo3=Tk.PhotoImage(file ='coulé.gif')

rate=Image.open("U:/sylvain.rome/ISN/proprojet/raté.png") #Importation image blanc de debut
rate.save('raté.gif','GIF')
photo1=Tk.PhotoImage(file ='raté.gif')

blanc=Image.open("U:/sylvain.rome/ISN/proprojet/blanc.png") #Importation image blanc de debut
blanc.save('blanc.gif','GIF')
photo=Tk.PhotoImage(file ='blanc.gif')

touche=Image.open("U:/sylvain.rome/ISN/proprojet/touché.png") #importation image croix de fin 
touche.save('touché.gif','GIF')
photo2=Tk.PhotoImage(file ='touché.gif')

cadre=Canvas(fenetre, bg="grey") # creation d'un label)
cadre.place(x=35,y=30)

def position(i,j):
    global Bouton
    print(i , "     " , j)
    Bouton[i][j]= Button(cadre, image = photo3,width=50, height = 50).grid(row=i, column=j)
     
Bouton= 10*[0]
for i in range(10):
    Bouton[i] = 10*[0]
for i in range(10):
    for j in range(10):
        Bouton[i][j] = Button(cadre, image = photo,width=50, height = 50, command=lambda i=i, j=j: position(i, j)).grid(row=i, column=j)

fenetre.mainloop()
