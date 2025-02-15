from tkinter import *
#First: les def
import time

# Pieds Player: X+55 (+40)   Y+110
# XMax Background = 3722

# Hitbox : Piques 1: X(540,620) Y(340, 430)
# Hitbox : Piques 2: X(1213,1293) Y(123, 213)
# Hitbox : Piques 3: X(1404,1484) Y(167, 257)
# Hitbox : Piques 4: X(1567,1647) Y(319, 409)
# Hitbox : Piques 5: X(2304,2384) Y(136, 226)
# Hitbox : Piques 6: X(3157,3237) Y(347, 437)
# Hitbox : Piques 7: X(3850,3930) Y(122, 212)
# Hitbox : Barrière fin: X(3765, 4550) Y(250, 285)
# Hitbox : Barrière milieu: X(2070, 2644) Y(250,285)


def repondre():
	nom.destroy()
	confirmer.destroy()
	
	Bjr.pack(side = "left", padx= 100)
	affichage["text"] = reponse.get()
	affichage.pack(side = "left", padx =0)
	reponse.destroy()
	jeu.pack(side = "right", padx = 20)
def tableau3():
	global Life
	global a
	
	jeu.destroy()
	Bjr.destroy()
	affichage.pack(side = "top")
	Game.geometry('800x600+100+100')
	fenetre.pack(side = "bottom", pady = 25)
	Background
	Player
	Instruction
	fenetre.bind_all("<Right>", avancer)
	fenetre.bind_all("<Up>", monter)
	fenetre.bind_all("<Down>", descendre)
	Game.bind_all ("<Escape>", Se_Barrer)
	

	
	
	
def DefeatTest():
		global X_background
		global X_Player
		global Y_Player
		
		if (540-95)<X_background<(620-95) and  (340-110)<Y_Player<(430-110):
			DefeatMan()
		if (1213-95)<X_background<(1293-95) and  (123-110)<Y_Player<(213-110):
			DefeatMan()
		if (1404-95)<X_background<(1484-95) and  (167-110)<Y_Player<(257-110):
			DefeatMan()
		if (1567-95)<X_background<(1647-95) and  (319-110)<Y_Player<(409-110):
			DefeatMan()
		if (2304-95)<X_background<(2384-95) and  (136-110)<Y_Player<(226-110):
			DefeatMan()
		if (3157-95)<X_background<(3237-95) and  (347-110)<Y_Player<(437-110):
			DefeatMan()
		if (73)<X_Player<(153) and  (122-110)<Y_Player<(212-110):
			DefeatMan()
		if (40)<X_Player<(800) and (140)<Y_Player<(175):
			DefeatMan()
		if (2070-95)<X_background<(2644-95) and (140)<Y_Player<(175):
			DefeatMan()
		
def Se_Barrer(event):
	sys.exit()
	
def avancer(event):
	global a
	a = 1
	while a==1:
		global X_background
		global Vitesse_hor
		global X_Player
		global Vitesse_hor_Player
		
		X_background += Vitesse_hor
		X_Player += Vitesse_hor_Player
		fenetre.move(Background,Vitesse_hor*(-1),0)
		fenetre.move(Player,Vitesse_hor_Player,0)
		fenetre.move(Instruction,0,-1)
		DefeatTest()
		if X_background >= 1000:
			Vitesse_hor = 6
			
		if X_background >= 1050:
			Vitesse_hor = 3
		if 1998<X_background < 2000:
			Vitesse_hor = 8
			
		if X_background >= 2050:
			Vitesse_hor = 4
		if X_background >= 3000:
			Vitesse_hor = 10
			
		if X_background >= 3050:
			Vitesse_hor = 5
		if X_background >= 3720:
			Vitesse_hor = 0
			Vitesse_hor_Player = 5
		if X_Player >= 400:
			Vitesse_hor_Player = 4
		if X_Player >= 430:
			Vitesse_hor_Player = 3
		if X_Player >= 450:
			Vitesse_hor_Player = 2
		if X_Player >= 550 and 0<Y_Player<130:
			Vitesse_hor_Player = 0.5
		if X_Player >= 750:
			DefeatMan()
		if X_Player >= 620 and 0<Y_Player<130:
			Vitesse_hor_Player = 0
			fenetre.create_image(0,0,image=Victory, anchor = NW)
			a = 0
		fenetre.update()
		time.sleep(0.005)

	
	
def monter (event):
	
	global Y_Player
	global Vitesse_vert
	if Y_Player >= 15:
		Vitesse_vert = 15
	if X_Player >= 620 and 50<Y_Player<130:
		Vitesse_vert = 0
	Y_Player -= Vitesse_vert
	fenetre.move(Player,0,Vitesse_vert*(-1))
	if Y_Player <= 14:
		Vitesse_vert = 0
	if X_Player >= 620 and 0<Y_Player<130:
		fenetre.create_image(0,0,image=Victory, anchor = NW)
		
def descendre (event):
	
	global Vitesse_vert_desc
	global Y_Player
	if Y_Player <= 345:
		Vitesse_vert_desc = 15
	if X_Player >= 620 and 50<Y_Player<130:
		Vitesse_vert_desc = 0
	Y_Player += Vitesse_vert_desc
	fenetre.move(Player,0,Vitesse_vert_desc)
	if Y_Player >= 346:
		Vitesse_vert_desc = 0
	if X_Player >= 620 and 0<Y_Player<130:
		fenetre.create_image(0,0,image=Victory, anchor = NW)
	
	
def DefeatMan ():
	global a
	fenetre.create_image(0,0,image=Final_Defeat, anchor = NW)
	a = 0
	
	

	
	

	

Game = Tk() #création de la fenêtre
Game.title("On s'occupe comme on peut")
Game.geometry('500x100+100+100')



nom = Label(Game, text = "Balancez une insulte au bol: ")
reponse = Entry(Game)
confirmer = Button(Game, text = "Clique ici l'ami", command=repondre)
Bjr = Label (Game, text = "Bienvenue, ")
affichage = Label(Game)
jeu = Button(Game, text = "Suite...", command=tableau3)
fenetre = Canvas (Game, width = 750, height = 500, background = "white")
PlayerStatic = PhotoImage (file= "Graphics/Player.png")
Level1 = PhotoImage (file= "Graphics/Level_1.png")
X_background = 00
Vitesse_hor = 2
Vitesse_vert = 15
Y_Player = 350
Vitesse_vert_desc = 0
Vitesse_hor_Player = 0
X_Player = 40
Instr_level_1=PhotoImage (file= "Graphics/Instru_Level_1.png")
Victory = PhotoImage (file= "Graphics/Victory.png")
Background = fenetre.create_image((X_background)*(-1),0,image=Level1, anchor = NW)
Player = fenetre.create_image(X_Player,Y_Player,image=PlayerStatic, anchor = NW)
Instruction = fenetre.create_image(0,0,image=Instr_level_1, anchor = NW)
Defeat = PhotoImage (file= "Graphics/Defeat.png")
Final_Defeat = PhotoImage (file= "Graphics/Final_Defeat.png")
a = 1





nom.pack()
reponse.pack()
confirmer.pack()











Game.mainloop() #Lancement de la boucle principale
