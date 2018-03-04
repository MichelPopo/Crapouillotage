from tkinter import * 

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

croix=Image.open("U:/sylvain.rome/ISN/proprojet/croix.jpg")
croix.save('croix.gif','GIF')
photo=Tk.PhotoImage(file = 'croix.gif')
cadre=Canvas(fenetre, bg="grey") # creation d'un label)
cadre.place(x=35,y=30)

Bouton= 10*[0]
for i in range(10):
    Bouton[i] = 10*[0]
for i in range(10):
    for j in range(10):
        Bouton[i][j] = Button(cadre, image = photo,width=215, height = 110, command=lambda i=i, j=j: fonction(i, j)).grid(row=i, column=j)
fenetre.mainloop()
