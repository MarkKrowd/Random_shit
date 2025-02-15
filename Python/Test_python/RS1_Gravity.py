from tkinter import *
import time
import winsound
# Définitions fonctions

#Menu
def Main():
	Fenetre.pack()
	Fenetre.bind_all ("<Return>", Demarrer)
	Game.bind_all ("<Escape>", Se_Barrer)
	
	global Depart_X
	global Depart_Y
	global Niveau1_X
	global Niveau1_Y
	global Player_X
	global Player_Y
	global Vitesse_Depart
	global a
	global b
	global cAv
	global cRe
	
	Vitesse_Depart = -4
	Depart_X = 0
	Depart_Y = 0
	Player_X = 40
	Player_Y = 1060
	Niveau1_X = 0
	Niveau1_Y = 600
	a = 1
	b = 0
	cAv = 0
	cRe = 0
	###################################################winsound.PlaySound('Sounds/Main.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
	Depart
	
	Niveau1
	#print("Main")


def Se_Barrer(event):
	sys.exit()

	
def Demarrer(event):	
	global a
	global b
	global TimeCAR
	global Vitesse_Depart
	global Depart_Y
	global Niveau1_Y
	global Player_Y
	global TempsA
	global TempsB
	Fenetre.unbind("<Return>")
	Fenetre.bind_all("<Return>", print ("nope"))
	###########################winsound.PlaySound('Sounds/MainToGame.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
	while a == 1:
		TempsA = time.time()
		Fenetre.move (Depart,0,Vitesse_Depart)
		Fenetre.move (Niveau1,0,Vitesse_Depart)
		Fenetre.move (Player,0,Vitesse_Depart)
		Depart_Y -=4
		Niveau1_Y -=4
		Player_Y -=4
		Fenetre.update()
		TempsB = time.time()
		if (TempsB - TempsA) < 0.01:
			time.sleep (0.01 - (TempsB-TempsA))
		if Depart_Y == -600:
			Vitesse_Depart = 0
			a = 0
			b=1
			TimeCAR = 0	
			CAR()
	#print("Demarrer")


def CAR():
	global b
	while b == 1:
		global TimeCAR
		global cAv
		if TimeCAR == 0:
			CAR3 = Fenetre.create_image (540, 200, image = PNG3, anchor = NW)
			CAR3
		elif TimeCAR == 1:		
			Fenetre.move(CAR3,0,1000)
		elif TimeCAR == 2:
			CAR2 = Fenetre.create_image (540, 200, image = PNG2, anchor = NW)
			CAR2
		elif TimeCAR == 3:
			Fenetre.move(CAR2,0,1000)
		elif TimeCAR == 4:
			CAR1 = Fenetre.create_image (540, 200, image = PNG1, anchor = NW)
			CAR1
		elif TimeCAR == 5:
			Fenetre.move(CAR1,0,1000)
		elif TimeCAR == 6:
			b = 0
			Fenetre.move(L5,1500,0)
			FuelLVL = Fenetre.create_image (0, 0, image = FuelLVL0PNG, anchor = NW)
			Fenetre.bind_all ("<Left>", Reculer)
			Fenetre.bind_all ("<Right>", Avancer)
			Fenetre.bind_all ("<Down>", Stop)
			Fenetre.bind_all ("<space>", Sauter)
			Fenetre.bind_all ("<a>", Reculer)
			Fenetre.bind_all ("<d>", Avancer)
			Fenetre.bind_all ("<s>", Stop)
			Fenetre.bind_all ("<w>", Sauter)
			Fenetre.bind_all ("<Up>", Sauter)
			Fenetre.bind_all("<r>", Restart)
			
		
		TimeCAR +=1
		Fenetre.update()
		time.sleep(0.5)
	#print("CAR")
	
	


def Reculer(event):
	global TempsA
	global TempsB
	global cRe
	global Vit_XPlay
	global Vit_XNiv1
	global Player_X
	global Niveau1_X
	
	if cRe == 0 and Vitesse_Chute == 0 and Vitesse_Up == 0 and Spam == 0:
		
		if cAv == 1:
			Stopp()
		
		cRe = 1
	
		Fenetre.move(Player,-1000,0)
		Fenetre.move(PlayerRe,1000,0)
	
		while cRe == 1:
			
			TempsA = time.time()
			if Player_X == 576:
				Vit_XPlay = 0
				Vit_XNiv1 = 4
			if Niveau1_X == 0:
				Vit_XPlay = -4
				Vit_XNiv1 = 0
			if Player_X==40:
				Vit_XPlay = 0
				Stopp()
			Hitbox_Murs_Re()
			Fenetre.move(Fuel1,Vit_XNiv1,0)
			Fenetre.move(Fuel2,Vit_XNiv1,0)
			Fenetre.move(Fuel3,Vit_XNiv1,0)
			Fenetre.move(Fuel4,Vit_XNiv1,0)
			Fenetre.move(Fuel5,Vit_XNiv1,0)
			Fenetre.move(Niveau1,Vit_XNiv1,0)
			Fenetre.move(Player,Vit_XPlay,0)
			Fenetre.move(PlayerAV,Vit_XPlay,0)
			Fenetre.move(PlayerRe,Vit_XPlay,0)
			Fenetre.move(PlayerUp,Vit_XPlay,0)
			Fenetre.move(PlayerUpBa,Vit_XPlay,0)
			
			Player_X += Vit_XPlay
			Niveau1_X += Vit_XNiv1
			Fenetre.update()
			Chutes_mvmt()
			Hitbox_Chutes()
			Hitbox_Murs_Re()
			TempsB = time.time()
			if (TempsB-TempsA)<0.01:
				time.sleep(0.01-(TempsB-TempsA))
	
	#print("Reculer")


def Avancer(event):
	global cAv
	global TempsA
	global TempsB
	global VitXPlay
	global VitXNiv1
	global Player_X
	global Niveau1_X
	
	
	if cAv == 0 and Vitesse_Chute == 0 and Vitesse_Up == 0 and Spam == 0:
		
		if cRe == 1:
			Stopp()
		
		cAv = 1
	
		Fenetre.move(Player,-1000,0)
		Fenetre.move(PlayerAV,1000,0)
	
		while cAv == 1:
			TempsA = time.time()
			
			if Niveau1_X==0:
				VitXNiv1 = 0
				VitXPlay = 4
			if Player_X==576:
				VitXPlay = 0
				VitXNiv1 = -4
			Hitbox_Murs_Av()
			Fenetre.move(Fuel1,VitXNiv1,0)
			Fenetre.move(Fuel2,VitXNiv1,0)
			Fenetre.move(Fuel3,VitXNiv1,0)
			Fenetre.move(Fuel4,VitXNiv1,0)
			Fenetre.move(Fuel5,VitXNiv1,0)
			Fenetre.move(Niveau1,VitXNiv1,0)
			Fenetre.move(Player,VitXPlay,0)
			Fenetre.move(PlayerAV,VitXPlay,0)
			Fenetre.move(PlayerRe,VitXPlay,0)
			Fenetre.move(PlayerUp,VitXPlay,0)
			Fenetre.move(PlayerUpBa,VitXPlay,0)
			
			Player_X += VitXPlay
			Niveau1_X += VitXNiv1
			
			Fenetre.update()
			Chutes_mvmt()
			Hitbox_Chutes()
			Hitbox_Murs_Av()
			TempsB = time.time()
			#print (TempsB-TempsA)
			if (TempsB-TempsA)<0.01:
				time.sleep(0.01-(TempsB-TempsA))
	
	#print("Avancer")


def Stop(event):
	global cAv
	global cRe
	if Spam == 1:
		print ("nope")
	else:
		if cAv == 1:
			Fenetre.move(Player,1000,0)
			Fenetre.move(PlayerAV,-1000,0)
		cAv = 0
		if cRe == 1:
			Fenetre.move(Player,1000,0)
			Fenetre.move(PlayerRe,-1000,0)
		cRe = 0
		Fenetre.update()
		#print ("Stop")


def Stopp():
	global cAv
	global cRe
	if cAv == 1:
		Fenetre.move(Player,1000,0)
		Fenetre.move(PlayerAV,-1000,0)
	cAv = 0
	if cRe == 1:
		Fenetre.move(Player,1000,0)
		Fenetre.move(PlayerRe,-1000,0)
	cRe = 0
	Fenetre.update()
	#print ("Stopp")



#Sauter quoi
def Sauter (event):
	global Y0
	global d1
	global d2
	global d10
	global d11
	global V0
	global Vitesse_Chute
	global Player_Y
	global Spam
	global TempsC
	global TempsD
	global Temps_Chute
	global Player_X
	global Niveau1_X
	
	if Spam == 0:
		if cAv == 1:
			Sauter_Avant()
		elif cRe == 1:	
			Sauter_Arriere()
		else:
			Spam = 1
			d1 = 1
			d2 = 0
			d10 = 1
			d11 = 1
			Y0 = Player_Y
			V0 = 6.5
			while d1 == 1:
				TempsC = time.time()
				if d10 == 1: 
					Fenetre.move(Player,-1000,0)
					Fenetre.move(PlayerUp,1000,0)
					d10 = 0
				Vitesse_Chute = 14*Temps_Chute - V0
				Fenetre.move(Player,0,Vitesse_Chute)
				Fenetre.move(PlayerUp, 0,Vitesse_Chute)		
				Fenetre.move(PlayerAV, 0,Vitesse_Chute)
				Fenetre.move(PlayerRe, 0,Vitesse_Chute)
				Fenetre.move(PlayerUpBa, 0,Vitesse_Chute)
				Player_Y += Vitesse_Chute
				#print ("Niv1_X = ", Niveau1_X, "PlayX = ", Player_X, "PlayY = ", Player_Y)
				#print (Vitesse_Chute)
				Temps_Chute += 0.01
				
				Fenetre.update()		
				if Vitesse_Chute > 0:
					Hitbox_Chutes()
				Plafonds()
				if d2 == 1:
					d1 = 0
				if (Y0-Player_Y > 100 or d1 == 0) and d11 == 1:
					Fenetre.move(PlayerUp,-1000,0)
					Fenetre.move(Player,1000,0)
					d11 = 0
				TempsD = time.time()
				if TempsD-TempsC < 0.01:
					time.sleep(0.01-(TempsD-TempsC))
			Spam = 0
			d2 = 0
			Temps_Chute = 0
			V0 = 0

def Sauter_Avant():
	global Y0
	global d1
	global d2
	global d10
	global d11
	global V0
	global Vitesse_Chute
	global Player_Y
	global Spam
	global TempsC
	global TempsD
	global Temps_Chute
	global Player_X
	global Niveau1_X
	Spam = 1
	d1 = 1
	d2 = 0
	d10 = 1
	d11 = 0
	V0 = 6.5
	Y0 = Player_Y
	while d1 == 1:
		TempsC = time.time()
		if d10 == 1: 
			Fenetre.move(PlayerAV,-1000,0)
			Fenetre.move(PlayerUp,1000,0)
			d10 = 0
			d11 = 1
		if Niveau1_X==0:
			VitXNiv1 = 0
			VitXPlay = 4
		if Player_X==576:
			VitXPlay = 0
			VitXNiv1 = -4
		Vitesse_Chute = 14*Temps_Chute - V0
		Hitbox_Murs_Av()
		Fenetre.move(Fuel1,VitXNiv1,0)
		Fenetre.move(Fuel2,VitXNiv1,0)
		Fenetre.move(Fuel3,VitXNiv1,0)
		Fenetre.move(Fuel4,VitXNiv1,0)
		Fenetre.move(Fuel5,VitXNiv1,0)
		Fenetre.move(Niveau1,VitXNiv1,0)
		Fenetre.move(Player,VitXPlay,Vitesse_Chute)
		Fenetre.move(PlayerUp, VitXPlay,Vitesse_Chute)
		Fenetre.move(PlayerAV, VitXPlay,Vitesse_Chute)
		Fenetre.move(PlayerRe, VitXPlay,Vitesse_Chute)
		Fenetre.move(PlayerUpBa, VitXPlay,Vitesse_Chute)
		Player_Y += Vitesse_Chute
		Player_X += VitXPlay
		Niveau1_X += VitXNiv1
		print ("Niv1_X = ", Niveau1_X, "PlayX = ", Player_X, "PlayY = ", Player_Y)
		Temps_Chute += 0.01
		
		Fenetre.update()
		print (Player_Y, Vitesse_Chute)
		if Vitesse_Chute >= 0:
			Hitbox_Chutes()
		if d2 == 1:
			d1 = 0
		Hitbox_Murs_Av()
		Plafonds()
		if (Y0-Player_Y > 100 or d1 == 0) and d11 == 1:
			Fenetre.move(PlayerUp,-1000,0)
			Fenetre.move(PlayerAV,1000,0)
			d11 = 0
		TempsD = time.time()
		print(TempsD-TempsC)
		if TempsD-TempsC < 0.01:
			time.sleep(0.01-(TempsD-TempsC))
			
	Spam = 0
	d2 = 0
	Temps_Chute = 0
	V0 = 0
def Sauter_Arriere():
	global Y0
	global d1
	global d2
	global d10
	global d11
	global V0
	global Vitesse_Chute
	global Player_Y
	global Spam
	global TempsC
	global TempsD
	global Temps_Chute
	global Player_X
	global Niveau1_X
	Spam = 1
	d1 = 1
	d2 = 0
	d10 = 1
	d11 = 0
	V0 = 6.5
	Y0 = Player_Y
	while d1 == 1:
		TempsC = time.time()
		if d10 == 1: 
			Fenetre.move(PlayerRe,-1000,0)
			Fenetre.move(PlayerUpBa,1000,0)
			d10 = 0
			d11 = 1
		Hitbox_Murs_Av()
		if Player_X == 576:
			Vit_XPlay = 0
			Vit_XNiv1 = 4
		if Niveau1_X == 0:
			Vit_XPlay = -4
			Vit_XNiv1 = 0
		if Player_X==40:
			Vit_XPlay = 0	
		
		Vitesse_Chute = 14*Temps_Chute - V0
		Hitbox_Murs_Re()
		Fenetre.move(Fuel1,Vit_XNiv1,0)
		Fenetre.move(Fuel2,Vit_XNiv1,0)
		Fenetre.move(Fuel3,Vit_XNiv1,0)
		Fenetre.move(Fuel4,Vit_XNiv1,0)
		Fenetre.move(Fuel5,Vit_XNiv1,0)
		Fenetre.move(Niveau1,Vit_XNiv1,0)
		Fenetre.move(Player,Vit_XPlay,Vitesse_Chute)
		Fenetre.move(PlayerUp, Vit_XPlay,Vitesse_Chute)
		Fenetre.move(PlayerAV, Vit_XPlay,Vitesse_Chute)
		Fenetre.move(PlayerRe, Vit_XPlay,Vitesse_Chute)
		Fenetre.move(PlayerUpBa, Vit_XPlay,Vitesse_Chute)
		Player_Y += Vitesse_Chute
		Player_X += Vit_XPlay
		Niveau1_X += Vit_XNiv1	
		print ("Niv1_X = ", Niveau1_X, "PlayX = ", Player_X, "PlayY = ", Player_Y)
		Temps_Chute += 0.01
		
		Fenetre.update()
		print (Player_Y, Vitesse_Chute)
		if Vitesse_Chute >= 0:
			Hitbox_Chutes()
		if d2 == 1:
			d1 = 0
		Hitbox_Murs_Re()
		Plafonds()
		if (Y0-Player_Y > 100 or d1 == 0) and d11 == 1:
			Fenetre.move(PlayerUpBa,-1000,0)
			Fenetre.move(PlayerRe,1000,0)
			d11 = 0
		TempsD = time.time()
		print(TempsD-TempsC)
		if TempsD-TempsC < 0.01:
			time.sleep(0.01-(TempsD-TempsC))
	Spam = 0
	d2 = 0
	Temps_Chute = 0
	V0 = 0

#Quand une chute est détectée
def Chute():
	global Y0
	global d1
	global d2
	global d3
	global Vitesse_Chute
	global Player_Y
	global Player_X
	global Niveau1_X
	global TempsA
	global TempsB
	global Temps_Chute
	global Vit_XPlay
	
	
	d1 = 1
	d2 = 0
	
	if cAv == 1:
		while d1 == 1:
			TempsC = time.time()
			Vitesse_Chute = 14*Temps_Chute - V0
			Hitbox_Murs_Av()
			Fenetre.move(Fuel1,VitXNiv1,0)
			Fenetre.move(Fuel2,VitXNiv1,0)
			Fenetre.move(Fuel3,VitXNiv1,0)
			Fenetre.move(Fuel4,VitXNiv1,0)
			Fenetre.move(Fuel5,VitXNiv1,0)
			Fenetre.move(Niveau1, VitXNiv1,0)
			Fenetre.move(Player, VitXPlay,Vitesse_Chute)
			Fenetre.move(PlayerUp, VitXPlay,Vitesse_Chute)		
			Fenetre.move(PlayerAV, VitXPlay,Vitesse_Chute)
			Fenetre.move(PlayerRe, VitXPlay,Vitesse_Chute)
			Fenetre.move(PlayerUpBa, VitXPlay,Vitesse_Chute)
			Player_Y += Vitesse_Chute
			Player_X += VitXPlay
			Niveau1_X += VitXNiv1
			Temps_Chute += 0.01
		
			Fenetre.update()	
			Plafonds()
			Hitbox_Chutes() 
		
			if d2 == 1:
				d1 = 0
			if Vitesse_Chute==0 and Player_Y > 600:
				Recommencer()
			Hitbox_Murs_Av()
			TempsD = time.time()
			if TempsD-TempsC < 0.01:
				time.sleep(0.01-(TempsD-TempsC))
	elif cRe == 1:
		while d1 == 1:
			TempsC = time.time()
			if Player_X==40:
				Vit_XPlay = 0
			Vitesse_Chute = 14*Temps_Chute - V0
			Hitbox_Murs_Re()
			Fenetre.move(Fuel1,Vit_XNiv1,0)
			Fenetre.move(Fuel2,Vit_XNiv1,0)
			Fenetre.move(Fuel3,Vit_XNiv1,0)
			Fenetre.move(Fuel4,Vit_XNiv1,0)
			Fenetre.move(Fuel5,Vit_XNiv1,0)
			Fenetre.move(Niveau1, Vit_XNiv1,0)
			Fenetre.move(Player, Vit_XPlay,Vitesse_Chute)
			Fenetre.move(PlayerUp, Vit_XPlay,Vitesse_Chute)		
			Fenetre.move(PlayerAV, Vit_XPlay,Vitesse_Chute)
			Fenetre.move(PlayerRe, Vit_XPlay,Vitesse_Chute)
			Fenetre.move(PlayerUpBa, Vit_XPlay,Vitesse_Chute)
			Player_Y += Vitesse_Chute
			Player_X += Vit_XPlay
			Niveau1_X += Vit_XNiv1
			#print (Vitesse_Chute)
			Temps_Chute += 0.01
		
			Fenetre.update()	
			Plafonds()
			Hitbox_Chutes() 
		
			if d2 == 1:
				d1 = 0
			if Vitesse_Chute==0 and Player_Y > 600:
				Recommencer()
			Hitbox_Murs_Re()
			TempsD = time.time()
			if TempsD-TempsC < 0.01:
				time.sleep(0.01-(TempsD-TempsC))
	else:
		while d1 == 1:
			TempsC = time.time()
			Vitesse_Chute = 14*Temps_Chute - V0
			Fenetre.move(Player,0,Vitesse_Chute)
			Fenetre.move(PlayerUp, 0,Vitesse_Chute)		
			Fenetre.move(PlayerAV, 0,Vitesse_Chute)
			Fenetre.move(PlayerRe, 0,Vitesse_Chute)
			Fenetre.move(PlayerUpBa, 0,Vitesse_Chute)
			Player_Y += Vitesse_Chute
			#print (Vitesse_Chute)
			Temps_Chute += 0.01
		
			Fenetre.update()	
			Plafonds()
			Hitbox_Chutes() 
		
			if d2 == 1:
				d1 = 0
			if Vitesse_Chute==0 and Player_Y > 600:
				Recommencer()
			TempsD = time.time()
			if TempsD-TempsC < 0.01:
				time.sleep(0.01-(TempsD-TempsC))
		
	d2 = 0
	Temps_Chute = 0
		
		
	#print ("Chute")
		
def Plafonds():
	global Temps_Chute
	print(Temps_Chute)
	if Vitesse_Chute<0 and ((-600>Niveau1_X>-677 and 420>Player_Y>399) or (-665>Niveau1_X>-878 and 320>Player_Y>305)):
		Temps_Chute = 2*(6.5/14)-Temps_Chute
		print ("oui")



#Détection de chutes en déplacement vertical
def Hitbox_Chutes():
# Taille joueur:	50/100
	global Vitesse_Chute
	global d2
	#Marquer tous les trous par "and not" et laisser 1 de marge de chaque côté
	if Player_Y > 449 and not (334<Player_X<506) and not (-230>Niveau1_X>-250) and not (-879>Niveau1_X>-950):
		Vitesse_Chute = 0 
		d2 = 1
		
	if 100 <= Player_X < 580 and 306 <= Player_Y <= 315 and -165<= Niveau1_X <= 0:
		Vitesse_Chute = 0
		d2 = 1
		
	elif -246>Niveau1_X>-304 and 280<=Player_Y<= 287:
		Vitesse_Chute = 0
		d2 = 1
	
	elif -403>Niveau1_X>-663 and 298<=Player_Y<=305:
		Vitesse_Chute = 0
		d2 = 1
	
	elif -657>Niveau1_X>-882 and 185<=Player_Y<=195:
		Vitesse_Chute = 0
		d2 = 1
	
	if Player_Y > 610:
		Vitesse_Chute = 0
		d2 = 1
		Recommencer()
		
	#print ("Hitbox_Chutes")

def Hitbox_Murs_Re ():
	global d1
	global d2
	global d3
	global d11
	global VitXNiv1
	global Vit_XNiv1
	global VitXPlay
	global Vit_XPlay
	global FuelA
	global FuelB
	global FuelC
	global FuelD
	global FuelE
	#Murs
	
	if (-260>Niveau1_X>-303 and Player_Y > 287) or (-650>Niveau1_X>-670 and 195<Player_Y<409) or (-862>Niveau1_X>-882 and 195<Player_Y) or (330<Player_X<340 and Player_Y>440) or (-226>Niveau1_X>-236 and Player_Y>440) or (-874>Niveau1_X>-884 and Player_Y>440):
		d1 = 0
		d2 = 0
		d3 = 0
		if d11 == 1:
			Fenetre.move(PlayerUpBa,-1000,0)
			Fenetre.move(PlayerRe,1000,0)
			d11 = 0
		Stopp()
		Chute()	
		Vit_XNiv1=0	
		Vit_XPlay = 0
		
	
	#Fuels
	elif -714>Niveau1_X>-804 and Player_Y > 390 and FuelA == 0:
		Fenetre.move(Fuel1,0,-1000)
		FuelA = 1
		Fuel()
	elif -3494>Niveau1_X>-3584 and Player_Y > 390 and FuelB == 0:
		Fenetre.move(Fuel2,0,-1000)
		FuelB = 1
		Fuel()
	elif -7878>Niveau1_X>-7968 and Player_Y > 390 and FuelC == 0:
		Fenetre.move(Fuel3,0,-1000)
		FuelC = 1
		Fuel()
	elif -11350>Niveau1_X>-11440 and Player_Y > 390 and FuelD == 0:
		Fenetre.move(Fuel4,0,-1000)
		FuelD = 1
		Fuel()
	elif -16791>Niveau1_X>-16881 and Player_Y > 390 and FuelE == 0:
		Fenetre.move(Fuel5,0,-1000)
		FuelE = 1
		Fuel()
		
		
def Hitbox_Murs_Av ():
	global d1
	global d2
	global d3
	global d11
	global VitXNiv1
	global Vit_XNiv1
	global VitXPlay
	global Vit_XPlay
	global Fuel_LVL
	global FuelA
	global FuelB
	global FuelC
	global FuelD
	global FuelE
	#Murs
	
	if (-247>Niveau1_X>-290 and Player_Y > 286) or (-607>Niveau1_X>-627 and 195<Player_Y<409) or (-821>Niveau1_X>-841 and 195<Player_Y) or (500<Player_X<510 and Player_Y>440) or (-244>Niveau1_X>-256 and Player_Y>440) or (-995>Niveau1_X>-1005 and Player_Y>440):
		d1 = 0
		d2 = 0
		d3 = 0
		if d11 == 1:
			Fenetre.move(PlayerUp,-1000,0)
			Fenetre.move(PlayerAV,1000,0)
			d11 = 0
		Stopp()
		Chute()	
		VitXNiv1=0	
		VitXPlay = 0
	
	#Fuels
	elif -714>Niveau1_X>-804 and Player_Y > 390 and FuelA == 0:
		Fenetre.move(Fuel1,0,-1000)
		FuelA = 1
		Fuel()
	elif -3494>Niveau1_X>-3584 and Player_Y > 390 and FuelB == 0:
		Fenetre.move(Fuel2,0,-1000)
		FuelB = 1
		Fuel()
	elif -7878>Niveau1_X>-7968 and Player_Y > 390 and FuelC == 0:
		Fenetre.move(Fuel3,0,-1000)
		FuelC = 1
		Fuel()
	elif -11350>Niveau1_X>-11440 and Player_Y > 390 and FuelD == 0:
		Fenetre.move(Fuel4,0,-1000)
		FuelD = 1
		Fuel()
	elif -16791>Niveau1_X>-16881 and Player_Y > 390 and FuelE == 0:
		Fenetre.move(Fuel5,0,-1000)
		FuelE = 1
		Fuel()
		
	#Fin
	elif -18225>Niveau1_X:
		if Fuel_LVL == 5:
			print ("Gagné de Dieu!")
			Stopp()
		else:
			print ("Va voir chercher l'essence qui reste l'ami!")
	if -18230>Niveau1_X:
		Stopp()
		
		
		
#Détection de chutes en déplacement horizontal
def Chutes_mvmt():
	if 335<Player_X<505 and Player_Y > 449: #Trou 1
		Chute()
	#Trou 2
	if -231>Niveau1_X>-249 and Player_Y > 449:
		Chute()
	#Trou 3
	if -879>Niveau1_X>-1000 and Player_Y > 449:
		Chute()
	
	
	if 306 <= Player_Y <= 310 and (Player_X<100 or not 1>Niveau1_X>-165): #AJOUTER "XProchainePlateforme<Niveau1_X<-140" #Plateforme 1
		Chute()
	#Mur 1
	if 280<=Player_Y<= 284 and not -246>Niveau1_X>-304:
		Chute()
	#Plat 2
	if 298<=Player_Y<=305 and not -403>Niveau1_X>-663:
		Chute()
	#Plat 3
	if not -657>Niveau1_X>-882 and 185<=Player_Y<=195:
		Chute()
	#print ("Chutes_mvmt")
	
	

def Recommencer():
	global LooseX
	if LooseX != 0:
		Fenetre.move(Loose,1500,0)
		LooseX +=1500
	
	if Vies == 1:
		Fenetre.move(L1,-1500,0)
		Fenetre.move(L0,1500,0)
		Fenetre.update()
		time.sleep(3)
		sys.exit()

	#print ("Recommencer")
def Restart (event):
	global LooseX
	global Niveau1_X
	global Player_X
	global Player_Y
	global Vitesse_Chute
	Stopp()
	if LooseX == 0:
		LooseX -= 1500
		Fenetre.move(Loose,-1500,0)
	#############################################################################################################Compteur()
	Vitesse_Chute = 0
	Fenetre.move(Fuel1,Niveau1_X*(-1),0)
	Fenetre.move(Fuel2,Niveau1_X*(-1),0)
	Fenetre.move(Fuel3,Niveau1_X*(-1),0)
	Fenetre.move(Fuel4,Niveau1_X*(-1),0)
	Fenetre.move(Fuel5,Niveau1_X*(-1),0)
	Fenetre.move(Niveau1,Niveau1_X*(-1),0)
	Fenetre.move(PlayerUp,Player_X*(-1)+40,Player_Y*(-1)+450)
	Fenetre.move(Player,Player_X*(-1)+40,Player_Y*(-1)+450)
	Fenetre.move(PlayerAV,Player_X*(-1)+40,Player_Y*(-1)+450)
	Fenetre.move(PlayerRe,Player_X*(-1)+40,Player_Y*(-1)+450)
	Fenetre.move(PlayerUpBa,Player_X*(-1)+40,Player_Y*(-1)+450)
	Niveau1_X = 0
	Player_X = 40
	Player_Y = 450
	#print ("Restart")

def Compteur():
	global Vies
	Vies -= 1
	if Vies == 4:
		Fenetre.move(L5,-1500,0)
		Fenetre.move(L4,1500,0)
	elif Vies == 3:
		Fenetre.move(L4,-1500,0)
		Fenetre.move(L3,1500,0)
	elif Vies == 2:
		Fenetre.move(L3,-1500,0)
		Fenetre.move(L2,1500,0)
	elif Vies == 1:
		Fenetre.move(L2,-1500,0)
		Fenetre.move(L1,1500,0)
	elif Vies == 0:
		Fenetre.move(L1,-1500,0)
		Fenetre.move(L0,1500,0)
		Fenetre.update()
		time.sleep(3)
		sys.exit()
	#print ("Compteur")

def Fuel():
	global Fuel_LVL
	Fuel_LVL += 1
	if Fuel_LVL == 1:
		FuelLVL = Fenetre.create_image (0, 0, image = FuelLVL1PNG, anchor = NW)
	elif Fuel_LVL == 2:
		FuelLVL = Fenetre.create_image (0, 0, image = FuelLVL2PNG, anchor = NW)
	elif Fuel_LVL == 3:
		FuelLVL = Fenetre.create_image (0, 0, image = FuelLVL3PNG, anchor = NW)
	elif Fuel_LVL == 4:
		FuelLVL = Fenetre.create_image (0, 0, image = FuelLVL4PNG, anchor = NW)
	elif Fuel_LVL == 5:
		FuelLVL = Fenetre.create_image (0, 0, image = FuelLVL5PNG, anchor = NW)

# Définitions

Game = Tk()
Game.title("RS I")
Game.geometry('1200x600+10+10')
Fenetre = Canvas(Game, width = 1200, height = 600, background = "black")

Vitesse_Depart = -2
Depart_X = 0
Depart_Y = 0
Niveau1_X = 0
Niveau1_Y = 600
Player_X = 40
Player_Y = 1050
a = 1
b = 0
d1 = 0
d2 = 0
d3 = 0
d10 = 0
d11 = 0
V0 = 0
cAv = 0
cRe = 0
TimeCAR = 10
Spam = 0
Fuel_LVL = 0
FuelA = 0
FuelB = 0
FuelC = 0
FuelD = 0
FuelE = 0

Temps_Chute = 0
LooseX = -1500

Vitesse_Chute = 0
Vitesse_Up = 0
VitXPlay = 0
VitYPlay = 0
Vit_XPlay = 0
Vit_YPlay = 0
VitXNiv1 = 0
Vit_XNiv1 = 0

Y0=450

Vies = 5


#Images

DepartPNG = PhotoImage (file="Graphics/Menu.png")
Depart = Fenetre.create_image (Depart_X,Depart_Y,image = DepartPNG, anchor = NW)

Lvl1 = PhotoImage (file="Graphics/Game_1.png")
Niveau1 = Fenetre.create_image (Niveau1_X, Niveau1_Y,image = Lvl1, anchor = NW)

PlayerPNG = PhotoImage (file="Graphics/RS1.png")
PlayerPNGRe = PhotoImage (file="Graphics/RS1_back.png")
Player = Fenetre.create_image (Player_X, Player_Y, image = PlayerPNG, anchor = NW)
Player_Back = Fenetre.create_image (-960, Player_Y, image = PlayerPNG, anchor = NW)

PNG1 = PhotoImage (file="Graphics/1.png")
PNG2 = PhotoImage (file="Graphics/2.png")
PNG3 = PhotoImage (file="Graphics/3.png")		

PlayerPNG1 = PhotoImage (file="Graphics/RS1_Move_1.png")
PlayerPNG3 = PhotoImage (file="Graphics/RS1_Move_1b.png")
PlayerPNG4 = PhotoImage (file="Graphics/RS1_Up.png")
PlayerPNG5 = PhotoImage (file="Graphics/RS1_Up_Back.png")

LoosePNG = PhotoImage (file="Graphics/Loose.png")
Loose = Fenetre.create_image(-1500, 0, image = LoosePNG, anchor = NW)

PlayerAV = Fenetre.create_image (-960, 450, image = PlayerPNG1, anchor = NW)
PlayerRe = Fenetre.create_image (-960, 450, image = PlayerPNG3, anchor = NW)
PlayerUp = Fenetre.create_image (-960, 450, image = PlayerPNG4, anchor = NW)
PlayerUpBa = Fenetre.create_image (-960, 450, image = PlayerPNG5, anchor = NW)

LPNG1 = PhotoImage (file="Graphics/Life.png")
LPNG2 = PhotoImage (file="Graphics/Life_2.png")
LPNG3 = PhotoImage (file="Graphics/Life_3.png")
LPNG4 = PhotoImage (file="Graphics/Life_4.png")
LPNG5 = PhotoImage (file="Graphics/Life_5.png")
FinPND = PhotoImage (file="Graphics/Fin_Looser.png")

L0 = Fenetre.create_image (-1500, 0, image = FinPND, anchor = NW)
L1 = Fenetre.create_image (-1500, 0, image = LPNG1, anchor = NW)
L2 = Fenetre.create_image (-1500, 0, image = LPNG2, anchor = NW)
L3 = Fenetre.create_image (-1500, 0, image = LPNG3, anchor = NW)
L4 = Fenetre.create_image (-1500, 0, image = LPNG4, anchor = NW)
L5 = Fenetre.create_image (-1500, 0, image = LPNG5, anchor = NW)

Fuel1PNG = PhotoImage (file="Graphics/Fuel.png")
Fuel2PNG = PhotoImage (file="Graphics/Fuel.png")
Fuel3PNG = PhotoImage (file="Graphics/Fuel.png")
Fuel4PNG = PhotoImage (file="Graphics/Fuel.png")
Fuel5PNG = PhotoImage (file="Graphics/Fuel.png")

Fuel1 = Fenetre.create_image (1340, 490, image = Fuel1PNG, anchor = NW)
Fuel2 = Fenetre.create_image (4120, 490, image = Fuel2PNG, anchor = NW)
Fuel3 = Fenetre.create_image (8504, 490, image = Fuel3PNG, anchor = NW)
Fuel4 = Fenetre.create_image (11976, 490, image = Fuel4PNG, anchor = NW)
Fuel5 = Fenetre.create_image (17417, 490, image = Fuel5PNG, anchor = NW)

FuelLVL0PNG = PhotoImage (file="Graphics/Fuel_Lvl_0.png")
FuelLVL1PNG = PhotoImage (file="Graphics/Fuel_Lvl_1.png")
FuelLVL2PNG = PhotoImage (file="Graphics/Fuel_Lvl_2.png")
FuelLVL3PNG = PhotoImage (file="Graphics/Fuel_Lvl_3.png")
FuelLVL4PNG = PhotoImage (file="Graphics/Fuel_Lvl_4.png")
FuelLVL5PNG = PhotoImage (file="Graphics/Fuel_Lvl_5.png")

TempsA = 0
TempsB = 0
TempsC = 0
TempsD = 0


#Commandes de départ

Main()



	
	






Game.mainloop() #Lancement de la boucle principale
