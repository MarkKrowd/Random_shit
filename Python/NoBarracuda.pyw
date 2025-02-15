from tkinter import *


def telech():
	global Lien
	lien = str(Lien.get())
	lien = lien.split("=")
	if len(lien) !=1:
		lien = lien[1]
		lien = lien.split("&")
		lien = lien[0]
		lien = lien.replace("%2f", "/")
		lien = lien.replace("%3a", ":")
		webbrowser.open(lien)
	Lien.delete(0, END)
	
	

fenetre = Tk()
fenetre.title("Barracuda c'est chiant")

Lien = Entry()
Lien.place(x=400, y=30, width=800, height=25)
Lien.pack()


Commande = Button(fenetre, text="Télécharger", command = telech)
Commande.pack()

bouton= Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()


fenetre.geometry("300x100+300+0")
fenetre.mainloop()