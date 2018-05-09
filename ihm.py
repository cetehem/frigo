from tkinter import *
from tkinter.messagebox import *

fenetre = Tk()

##########################


# Image (Top left corner) Bleu
#photo = PhotoImage(file="photo.jpg")
canvas_image = Canvas(fenetre,width=700, height=400, bg='blue')
#canvas_image.create_image(0, 0, anchor=NW, image=photo)
canvas_image.pack(side=TOP)



# Stock, date et poids (Top right corner) Rouge
canvas_topright = Canvas(canvas_image,width=350, height=200, bg='red')
canvas_topright.pack(side=RIGHT)



# Ajout (Bottom left corner) Jaune
canvas_ajout = Canvas(fenetre,width=700, height=400, bg='yellow')
canvas_ajout.pack(side=BOTTOM)



# Liste (Bottom right corner) Vert
canvas_list = Canvas(canvas_ajout,width=350, height=200, bg='green')
canvas_list.pack(side=RIGHT)


##########################


# Affichage du stock
stock = 0
Frame2 = Frame(canvas_topright, borderwidth=2, relief=GROOVE)
Frame2.pack(side=TOP, padx=10, pady=10)

Frame3 = Frame(Frame2, bg="white", borderwidth=2, relief=GROOVE)
Frame3.pack(side=RIGHT, padx=5, pady=5)

Label(Frame2, text="Stock :").pack(padx=10, pady=10)
Label(Frame3, text=stock,bg="white").pack(padx=10, pady=10)

# Affichage du poids
poids = 0
Frame2 = Frame(canvas_topright, borderwidth=2, relief=GROOVE)
Frame2.pack(padx=10, pady=10)

Frame3 = Frame(Frame2, bg="white", borderwidth=2, relief=GROOVE)
Frame3.pack(side=RIGHT, padx=5, pady=5)

Label(Frame2, text="Poids :").pack(padx=10, pady=10)
Label(Frame3, text=poids, bg="white").pack(padx=10, pady=10)

# Affichage de la date d'entrée du dernier produit
date_last_product = 2018
Frame2 = Frame(canvas_topright, borderwidth=2, relief=GROOVE)
Frame2.pack(side=BOTTOM, padx=10, pady=10)

Frame3 = Frame(Frame2, bg="white", borderwidth=2, relief=GROOVE)
Frame3.pack(side=RIGHT, padx=5, pady=5)

Label(Frame2, text="Date d'entrée du dernier produit :").pack(padx=10, pady=10)
Label(Frame3, text=date_last_product, bg="white").pack(padx=10, pady=10)

# remplissage case bleu
Frame3 = Frame(canvas_image, bg="white", borderwidth=2, relief=GROOVE)
Frame3.pack(side=RIGHT, padx=5, pady=5)
Label(Frame3, text="Je ne sers a rien :*", bg="white").pack(padx=10, pady=10)


##########################


# Liste de produit (bottom right)

liste = Listbox(canvas_list)

liste.insert(1, "Patates")
liste.insert(2, "Carrotes")
liste.insert(3, "Tomates")
liste.insert(4, "Salades")
liste.insert(5, "Oignons")
liste.insert(6, "Courgettes")
liste.insert(7, "Choux")
liste.insert(8, "Fraises")
liste.insert(9, "Cerises")
liste.insert(10, "Pommes")

liste.pack()

# Boutton d'action de la liste

bouton_list=Button(canvas_list, text="Valider", command=fenetre.quit)
bouton_list.pack(side=BOTTOM,)


##########################

# Boutton de retrait

def recupere():
    showinfo("Alerte", entree.get())

value = StringVar() 
value.set("Valeur")
entree = Entry(canvas_ajout, textvariable=value, width=30)
entree.pack()

bouton = Button(canvas_ajout, text="Retrait de produit", command=recupere)
bouton.pack()

# Boutton de stockage

def stockage():
    showinfo("Alerte", stock.get())

value = StringVar() 
value.set("Valeur")
stocker = Entry(canvas_ajout, textvariable=value, width=30)
stocker.pack()

bouton = Button(canvas_ajout, text="Retrait de produit", command=stockage)
bouton.pack()


























fenetre.mainloop()
