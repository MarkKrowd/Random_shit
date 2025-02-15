from tkinter import *
import time

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
	
	Vitesse_Depart = -3
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
	
	Depart
	
	Niveau1
	print("Main")


def Se_Barrer(event):
	sys.exit()

	
def Demarrer(event):
	global a
	global b
	global TimeCAR
	Fenetre.unbind("<Return>")
	Fenetre.bind_all("<Return>", print ("nope"))
	while a == 1:
		global Vitesse_Depart
		global Depart_Y
		global Niveau1_Y
		global Player_Y
		Fenetre.move (Depart,0,Vitesse_Depart)
		Fenetre.move (Niveau1,0,Vitesse_Depart)
		Fenetre.move (Player,0,Vitesse_Depart)
		Depart_Y -=3
		Niveau1_Y -=3
		Player_Y -=3
		
		Fenetre.update()
		time.sleep (0.01)
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
	
	if cRe == 1 or Vitesse_Chute != 0 or Vitesse_Up == 1:
		print ("T'es pressé couz?")
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
				Vit_XNiv1 = 2
			if Niveau1_X == 0:
				Vit_XPlay = -2
				Vit_XNiv1 = 0
			if Player_X==40:
				Vit_XPlay = 0
				Stopp()
		
			
			Hitbox_Murs_Re()
			Fenetre.move(Niveau1,Vit_XNiv1,0)
			Fenetre.move(Player,Vit_XPlay,0)
			Fenetre.move(PlayerAV,Vit_XPlay,0)
			Fenetre.move(PlayerRe,Vit_XPlay,0)
			Fenetre.move(PlayerUp,Vit_XPlay,0)
			Fenetre.move(PlayerUpBa,Vit_XPlay,0)
			
			Player_X += Vit_XPlay
			Niveau1_X += Vit_XNiv1
			TempsB = time.time()
			Fenetre.update()
			if (TempsB-TempsA)<0.005 and not (TempsB-TempsA)<0:
				time.sleep(0.005-(TempsB-TempsA))
			Chutes_mvmt()
			Hitbox_Chutes()
			Hitbox_Murs_Re()
	
	#print("Reculer")


def Avancer(event):
	global cAv
	global TempsA
	global TempsB
	global VitXPlay
	global VitXNiv1
	global Player_X
	global Niveau1_X
	
	
	if cAv == 1 or Vitesse_Chute != 0 or Vitesse_Up == 1: 
		print ("T'es pressé couz?")
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
				VitXPlay = 2
			if Player_X==576:
				VitXPlay = 0
				VitXNiv1 = -2
			Hitbox_Murs_Av()
			Fenetre.move(Niveau1,VitXNiv1,0)
			Fenetre.move(Player,VitXPlay,0)
			Fenetre.move(PlayerAV,VitXPlay,0)
			Fenetre.move(PlayerRe,VitXPlay,0)
			Fenetre.move(PlayerUp,VitXPlay,0)
			Fenetre.move(PlayerUpBa,VitXPlay,0)
			
			Player_X += VitXPlay
			Niveau1_X += VitXNiv1
			TempsB = time.time()
			Fenetre.update()
			if (TempsB-TempsA)<0.005 and not (TempsB-TempsA)<0:
				time.sleep(0.005-(TempsB-TempsA))
			Chutes_mvmt()
			Hitbox_Chutes()
			Hitbox_Murs_Av()
	
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

#Sauter quand le joueur marche en avant
def Sauter_Avant():
	global Y0
	global d1
	global d2
	global d3
	global Vitesse_Chute
	global Player_Y
	global Spam
	global Vitesse_Up
	global VitXPlay
	global VitXNiv1
	global Player_X
	global Niveau1_X
	global TempsA
	global TempsB
	Spam = 1
	Y0 = Player_Y
	Fenetre.move(Player,-1000,0)
	Fenetre.move(PlayerUp,1000,0)
			
	d1 = 1
	
			
	while d1 == 1:
		TempsA=time.time()
		if Niveau1_X==0:
			VitXNiv1 = 0
			VitXPlay = 2
		if Player_X==576:
			VitXPlay = 0
			VitXNiv1 = -2
		Hitbox_Murs_Av()
		Fenetre.move(Niveau1,VitXNiv1,0)
		Fenetre.move(PlayerUp,VitXPlay,-4)
		Fenetre.move(Player, VitXPlay,-4)
		Fenetre.move(PlayerAV, VitXPlay,-4)
		Fenetre.move(PlayerRe, VitXPlay,-4)
		Fenetre.move(PlayerUpBa, VitXPlay,-4)
		Player_Y -= 4
		Player_X += VitXPlay
		Niveau1_X += VitXNiv1
		TempsB=time.time()
		if (TempsB-TempsA)<0.005 and not (TempsB-TempsA)<0:
			time.sleep(0.005-(TempsB-TempsA))
		if Player_Y + 60 == Y0:
			d1 = 0
			Fenetre.move(PlayerUp,-1000,0)
			Fenetre.move(Player,1000,0)
		Fenetre.update()
		Hitbox_Murs_Av()
	if cAv != 0:
		d2 = 1
	else:
		Fenetre.move(PlayerUp,-1000,0)
		Fenetre.move(Player,1000,0)
	while d2 == 1:
		TempsA=time.time()
		if Niveau1_X==0:
			VitXNiv1 = 0
			VitXPlay = 2
		if Player_X==576:
			VitXPlay = 0
			VitXNiv1 = -2
		Hitbox_Murs_Av()
		Fenetre.move(Niveau1,VitXNiv1,0)
		Fenetre.move(Player,VitXPlay,-3)
		Fenetre.move(PlayerUp, VitXPlay,-3)
		Fenetre.move(PlayerAV, VitXPlay,-3)
		Fenetre.move(PlayerRe, VitXPlay,-3)
		Fenetre.move(PlayerUpBa, VitXPlay,-3)
		Player_Y -= 3
		Player_X += VitXPlay
		Niveau1_X += VitXNiv1
		TempsB=time.time()
		if (TempsB-TempsA)<0.005 and not (TempsB-TempsA)<0:
			time.sleep(0.005-(TempsB-TempsA))
		if Player_Y + 108 == Y0:
			d2 = 0
		Fenetre.update()
		Hitbox_Murs_Av()
	if cAv != 0:
		d3 = 1
	while d3 == 1:
		TempsA=time.time()
		if Niveau1_X==0:
			
			VitXNiv1 = 0
			VitXPlay = 2
		if Player_X==576:
			VitXPlay = 0
			VitXNiv1 = -2
		Hitbox_Murs_Av()
		Fenetre.move(Niveau1,VitXNiv1,0)
		Fenetre.move(Player,VitXPlay,-2)
		Fenetre.move(PlayerUp, VitXPlay,-2)
		Fenetre.move(PlayerAV, VitXPlay,-2)
		Fenetre.move(PlayerRe, VitXPlay,-2)
		Fenetre.move(PlayerUpBa, VitXPlay,-2)
		Player_Y -= 2
		Player_X += VitXPlay
		Niveau1_X += VitXNiv1
		TempsB=time.time()
		if (TempsB-TempsA)<0.005 and not (TempsB-TempsA)<0:
			time.sleep(0.005-(TempsB-TempsA))
		if Player_Y + 140 == Y0:
			d3 = 0
		Fenetre.update()
		Hitbox_Murs_Av()
	if cAv != 0:
		d1 = 1
	while d1 == 1:
		TempsA=time.time()
		if Niveau1_X==0:
			VitXNiv1 = 0
			VitXPlay = 2
		if Player_X==576:
			VitXPlay = 0
			VitXNiv1 = -2
		Hitbox_Murs_Av()
		Fenetre.move(Niveau1,VitXNiv1,0)
		Fenetre.move(Player,VitXPlay,-1)
		Fenetre.move(PlayerUp, VitXPlay,-1)
		Fenetre.move(PlayerAV, VitXPlay,-1)
		Fenetre.move(PlayerRe, VitXPlay,-1)
		Fenetre.move(PlayerUpBa, VitXPlay,-1)
		Player_Y -= 1
		Player_X += VitXPlay
		Niveau1_X += VitXNiv1
		TempsB=time.time()
		if (TempsB-TempsA)<0.005 and not (TempsB-TempsA)<0:
			time.sleep(0.005-(TempsB-TempsA))
		if Player_Y + 155 == Y0:
			d1 = 0
		Fenetre.update()
		Hitbox_Murs_Av()
	Vitesse_Chute = 1
	while Vitesse_Chute > 0:
		TempsA=time.time()
		if Niveau1_X==0:
			VitXNiv1 = 0
			VitXPlay = 2
		if Player_X==576:
			VitXPlay = 0
			VitXNiv1 = -2
		if Player_Y + 155 == Y0:
			Vitesse_Chute = 1
		if Player_Y + 140 == Y0:
			Vitesse_Chute = 2
		if Player_Y + 108 == Y0:
			Vitesse_Chute = 3
		if Player_Y + 60 == Y0:
			Vitesse_Chute = 4
		Hitbox_Murs_Av()
		Fenetre.move(Niveau1,VitXNiv1,0)
		Fenetre.move(Player,VitXPlay,Vitesse_Chute)
		Fenetre.move(PlayerUp, VitXPlay,Vitesse_Chute)
		Fenetre.move(PlayerAV, VitXPlay,Vitesse_Chute)
		Fenetre.move(PlayerRe, VitXPlay,Vitesse_Chute)
		Fenetre.move(PlayerUpBa, VitXPlay,Vitesse_Chute)
		Player_Y += Vitesse_Chute
		Player_X += VitXPlay
		Niveau1_X += VitXNiv1
		TempsB=time.time()
		if (TempsB-TempsA)<0.005 and not (TempsB-TempsA)<0:
			time.sleep(0.005-(TempsB-TempsA))
		Hitbox_Chutes()
		Fenetre.update()
		Hitbox_Murs_Av()
	Spam = 0
	#print("Sauter_Avant")

#Sauter quand le joueur marche en arrière
def Sauter_Arriere():
	global Y0
	global d1
	global d2
	global d3
	global Vitesse_Chute
	global Player_Y
	global Spam
	global Vitesse_Up
	global VitXPlay
	global VitXNiv1
	global Player_X
	global Niveau1_X
	global TempsA
	global TempsB
	Spam = 1
	Y0 = Player_Y
	Fenetre.move(PlayerRe,-1000,0)
	Fenetre.move(PlayerUpBa,1000,0)
			
	d1 = 1
	
			
	while d1 == 1:
		TempsA=time.time()
		if Player_X == 576:
			Vit_XPlay = 0
			Vit_XNiv1 = 2
		if Niveau1_X == 0:
			Vit_XPlay = -2
			Vit_XNiv1 = 0
		if Player_X==40:
			Vit_XPlay = 0
		Hitbox_Murs_Re()
		Fenetre.move(Niveau1,Vit_XNiv1,0)
		Fenetre.move(PlayerUp,Vit_XPlay,-4)
		Fenetre.move(Player, Vit_XPlay,-4)
		Fenetre.move(PlayerAV, Vit_XPlay,-4)
		Fenetre.move(PlayerRe, Vit_XPlay,-4)
		Fenetre.move(PlayerUpBa,Vit_XPlay,-4)
		Player_Y -= 4
		Player_X += Vit_XPlay
		Niveau1_X += Vit_XNiv1
		TempsB=time.time()
		if (TempsB-TempsA)<0.005 and not (TempsB-TempsA)<0:
			time.sleep(0.005-(TempsB-TempsA))
		if Player_Y + 60 == Y0:
			d1 = 0
			Fenetre.move(PlayerUpBa,-1000,0)
			Fenetre.move(PlayerRe,1000,0)
		Fenetre.update()
		Hitbox_Murs_Re()
	if cRe != 0:
		d2 = 1
	else:
		Fenetre.move(PlayerUpBa,-1000,0)
		Fenetre.move(PlayerRe,1000,0)
	while d2 == 1:
		TempsA=time.time()
		if Player_X == 576:
			Vit_XPlay = 0
			Vit_XNiv1 = 2
		if Niveau1_X == 0:
			Vit_XPlay = -2
			Vit_XNiv1 = 0
		if Player_X==40:
			Vit_XPlay = 0
		Hitbox_Murs_Re()
		Fenetre.move(Niveau1,Vit_XNiv1,0)
		Fenetre.move(Player,Vit_XPlay,-3)
		Fenetre.move(PlayerUp, Vit_XPlay,-3)
		Fenetre.move(PlayerAV, Vit_XPlay,-3)
		Fenetre.move(PlayerRe, Vit_XPlay,-3)
		Fenetre.move(PlayerUpBa, Vit_XPlay,-3)
		Player_Y -= 3
		Player_X += Vit_XPlay
		Niveau1_X += Vit_XNiv1
		TempsB=time.time()
		if (TempsB-TempsA)<0.005 and not (TempsB-TempsA)<0:
			time.sleep(0.005-(TempsB-TempsA))
		if Player_Y + 108 == Y0:
			d2 = 0
		Fenetre.update()
		Hitbox_Murs_Re()
	if cRe != 0:
		d3 = 1
	while d3 == 1:
		TempsA=time.time()
		if Player_X == 576:
			Vit_XPlay = 0
			Vit_XNiv1 = 2
		if Niveau1_X == 0:
			Vit_XPlay = -2
			Vit_XNiv1 = 0
		if Player_X==40:
			Vit_XPlay = 0
		Hitbox_Murs_Re()
		Fenetre.move(Niveau1,Vit_XNiv1,0)
		Fenetre.move(Player,Vit_XPlay,-2)
		Fenetre.move(PlayerUp, Vit_XPlay,-2)
		Fenetre.move(PlayerAV, Vit_XPlay,-2)
		Fenetre.move(PlayerRe, Vit_XPlay,-2)
		Fenetre.move(PlayerUpBa, Vit_XPlay,-2)
		Player_Y -= 2
		Player_X += Vit_XPlay
		Niveau1_X += Vit_XNiv1
		TempsB=time.time()
		if (TempsB-TempsA)<0.005 and not (TempsB-TempsA)<0:
			time.sleep(0.005-(TempsB-TempsA))
		if Player_Y + 140 == Y0:
			d3 = 0
		Fenetre.update()
		Hitbox_Murs_Re()
	if cRe != 0:
		d1 = 1
	while d1 == 1:
		TempsA=time.time()
		if Player_X == 576:
			Vit_XPlay = 0
			Vit_XNiv1 = 2
		if Niveau1_X == 0:
			Vit_XPlay = -2
			Vit_XNiv1 = 0
		if Player_X==40:
			Vit_XPlay = 0
		Hitbox_Murs_Re()
		Fenetre.move(Niveau1,Vit_XNiv1,0)
		Fenetre.move(Player,Vit_XPlay,-1)
		Fenetre.move(PlayerUp, Vit_XPlay,-1)
		Fenetre.move(PlayerAV, Vit_XPlay,-1)
		Fenetre.move(PlayerRe, Vit_XPlay,-1)
		Fenetre.move(PlayerUpBa, Vit_XPlay,-1)
		Player_Y -= 1
		Player_X += Vit_XPlay
		Niveau1_X += Vit_XNiv1
		TempsB=time.time()
		if (TempsB-TempsA)<0.005 and not (TempsB-TempsA)<0:
			time.sleep(0.005-(TempsB-TempsA))
		if Player_Y + 155 == Y0:
			d1 = 0
		Fenetre.update()
		Hitbox_Murs_Re()
	Vitesse_Chute = 1
	while Vitesse_Chute > 0:
		TempsA=time.time()
		if Player_X == 576:
			Vit_XPlay = 0
			Vit_XNiv1 = 2
		if Niveau1_X == 0:
			Vit_XPlay = -2
			Vit_XNiv1 = 0
		if Player_X==40:
			Vit_XPlay = 0
			
		if Player_Y + 155 == Y0:
			Vitesse_Chute = 1
		if Player_Y + 140 == Y0:
			Vitesse_Chute = 2
		if Player_Y + 108 == Y0:
			Vitesse_Chute = 3
		if Player_Y + 60 == Y0:
			Vitesse_Chute = 4
		Hitbox_Murs_Re()		
		Fenetre.move(Niveau1,Vit_XNiv1,0)
		Fenetre.move(Player,Vit_XPlay,Vitesse_Chute)
		Fenetre.move(PlayerUp, Vit_XPlay,Vitesse_Chute)
		Fenetre.move(PlayerAV, Vit_XPlay,Vitesse_Chute)
		Fenetre.move(PlayerRe, Vit_XPlay,Vitesse_Chute)
		Fenetre.move(PlayerUpBa, Vit_XPlay,Vitesse_Chute)
		Player_Y += Vitesse_Chute
		Player_X += Vit_XPlay
		Niveau1_X += Vit_XNiv1
		TempsB=time.time()
		if (TempsB-TempsA)<0.005 and not (TempsB-TempsA)<0:
			time.sleep(0.005-(TempsB-TempsA))
		Hitbox_Chutes()
		Fenetre.update()
		Hitbox_Murs_Re()
	Spam = 0
	#print("Sauter_Arriere")

#Sauter quoi
def Sauter(event):
	global Y0
	global d1
	global d2
	global d3
	global Vitesse_Chute
	global Player_Y
	global Spam
	global Vitesse_Up
	global VitXPlay
	global VitXNiv1
	global Player_X
	global Niveau1_X
	global TempsA
	global TempsB
	
	if Spam ==1:
		print("Spaaaaaaaaaaaam")
	if Spam ==0:
		
		if cAv == 1:
			Sauter_Avant()
		elif cRe == 1:	
			Sauter_Arriere()
		elif Spam != 1:
			Spam = 1
			Y0 = Player_Y
			Phase_1()
			Vitesse_Chute = 1
			
			while Vitesse_Chute > 0:
				TempsA=time.time()
				if Player_Y + 155 == Y0:
					Vitesse_Chute = 1
				if Player_Y + 140 == Y0:
					Vitesse_Chute = 2
				if Player_Y + 108 == Y0:
					Vitesse_Chute = 3
				if Player_Y + 60 == Y0:
					Vitesse_Chute = 4
				
				Fenetre.move(Player,0,Vitesse_Chute)
				Fenetre.move(PlayerUp, 0,Vitesse_Chute)
				Fenetre.move(PlayerAV, 0,Vitesse_Chute)
				Fenetre.move(PlayerRe, 0,Vitesse_Chute)
				Fenetre.move(PlayerUpBa, 0,Vitesse_Chute)
				Player_Y += Vitesse_Chute
				TempsB=time.time()
				if (TempsB-TempsA)<0.005 and not (TempsB-TempsA)<0:
					time.sleep(0.005-(TempsB-TempsA))
				if d1 == 1:
					Hitbox_Chutes()
				Fenetre.update()
				
			d1 = 0
		Spam = 0
	#print ("Sauter")
	

#Quand une chute est détectée
def Chute():
	global Y0
	global d1
	global d2
	global d3
	global Vitesse_Chute
	global Player_Y
	global TempsA
	global TempsB
	
	if cAv == 1 or cRe == 1:	
		Stopp()
	Y0 = Player_Y
	Vitesse_Chute = 1
	while Vitesse_Chute > 0:
		TempsA=time.time()
		
		if Player_Y  == Y0:
			Vitesse_Chute = 1
		elif Player_Y -10 == Y0:
			Vitesse_Chute = 2
		elif Player_Y -30 == Y0:
			Vitesse_Chute = 3
		elif Player_Y -60 == Y0:
			Vitesse_Chute = 4
		if Player_Y > 600:
			Vitesse_Chute = 0
		if Vitesse_Chute != 0:
			Hitbox_Chutes()
			Fenetre.update()
		
		Fenetre.move(Player,0,Vitesse_Chute)
		Fenetre.move(PlayerUp, 0,Vitesse_Chute)
		Fenetre.move(PlayerAV, 0,Vitesse_Chute)
		Fenetre.move(PlayerRe, 0,Vitesse_Chute)
		Fenetre.move(PlayerUpBa, 0,Vitesse_Chute)
		Player_Y += Vitesse_Chute
		
		Fenetre.update()
		TempsB=time.time()
		if (TempsB-TempsA)<0.005 and not (TempsB-TempsA)<0:
			time.sleep(0.005-(TempsB-TempsA))
		
		if Vitesse_Chute==0 and Player_Y > 600:
			Recommencer()
	#print ("Chute")
		
	

#1ère phase de saut, joueur monte
def Phase_1():
	global d1
	global d2
	global d3
	global Vitesse_Up
	global Spam
	global TempsA
	global TempsB
	Spam = 1
	Fenetre.move(Player,-1000,0)
	Fenetre.move(PlayerUp,1000,0)
	Vitesse_Up = 1
	d1 = 1
	d2 = 1
	d3 = 1
	global Player_Y
	while d1 == 1:
		TempsA=time.time()
		Fenetre.move(PlayerUp,0,-4)
		Fenetre.move(Player, 0,-4)
		Fenetre.move(PlayerAV, 0,-4)
		Fenetre.move(PlayerRe, 0,-4)
		Fenetre.move(PlayerUpBa,0,-4)
		Player_Y -= 4
		TempsB=time.time()
		if (TempsB-TempsA)<0.005 and not (TempsB-TempsA)<0:
			time.sleep(0.005-(TempsB-TempsA))
		if Player_Y + 60 == Y0:
			d1 = 0
			Fenetre.move(PlayerUp,-1000,0)
			Fenetre.move(Player,1000,0)
		Fenetre.update()
		
	while d2 == 1:
		TempsA=time.time()
		Fenetre.move(Player,0,-3)
		Fenetre.move(PlayerUp, 0,-3)
		Fenetre.move(PlayerAV, 0,-3)
		Fenetre.move(PlayerRe, 0,-3)
		Fenetre.move(PlayerUpBa, 0,-3)
		Player_Y -= 3
		TempsB=time.time()
		if (TempsB-TempsA)<0.005 and not (TempsB-TempsA)<0:
			time.sleep(0.005-(TempsB-TempsA))
		if Player_Y + 108 == Y0:
			d2 = 0
		Fenetre.update()
	while d3 == 1:
		TempsA=time.time()
		Fenetre.move(Player,0,-2)
		Fenetre.move(PlayerUp, 0,-2)
		Fenetre.move(PlayerAV, 0,-2)
		Fenetre.move(PlayerRe, 0,-2)
		Fenetre.move(PlayerUpBa, 0,-2)
		Player_Y -= 2
		TempsB=time.time()
		if (TempsB-TempsA)<0.005 and not (TempsB-TempsA)<0:
			time.sleep(0.005-(TempsB-TempsA))
		if Player_Y + 140 == Y0:
			d3 = 0
		Fenetre.update()
	d1 = 1
	while d1 == 1:
		TempsA=time.time()
		Fenetre.move(Player,0,-1)
		Fenetre.move(PlayerUp, 0,-1)
		Fenetre.move(PlayerAV, 0,-1)
		Fenetre.move(PlayerRe, 0,-1)
		Fenetre.move(PlayerUpBa, 0,-1)
		Player_Y -= 1
		TempsB=time.time()
		if (TempsB-TempsA)<0.005 and not (TempsB-TempsA)<0:
			time.sleep(0.005-(TempsB-TempsA))
		if Player_Y + 155 == Y0:
			d1 = 0
		Fenetre.update() 
	Vitesse_Up = 0
	d1 = 1
	#print ("Phase 1")

#Détection de chutes en déplacement vertical
def Hitbox_Chutes():
# Taille joueur:	50/100
	global Vitesse_Chute
	#Marquer tout les trous par "and not" et laisser 1 de marge de chaque côté
	if Player_Y > 449 and not (334<Player_X<506) and not (-230>Niveau1_X>-250):
		Vitesse_Chute = 0
	elif 100 <= Player_X < 580 and 306 <= Player_Y <= 310 and -165<= Niveau1_X <= 0:
		Vitesse_Chute = 0
	elif -246>Niveau1_X>-304 and 280<=Player_Y<= 284:
		Vitesse_Chute = 0
	if Player_Y > 610:
		Vitesse_Chute = 0
		Recommencer()
	#print ("Hitbox_Chutes")

def Hitbox_Murs_Re ():
	global d1
	global d2
	global d3
	global VitXNiv1
	global Vit_XNiv1
	global VitXPlay
	global Vit_XPlay
	#Mur 1
	
	if -260>Niveau1_X>-303 and Player_Y > 284:
		d1 = 0
		d2 = 0
		d3 = 0
		Stopp()
		Chute()	
		Vit_XNiv1=0	
		Vit_XPlay = 0
		
def Hitbox_Murs_Av ():
	global d1
	global d2
	global d3
	global VitXNiv1
	global Vit_XNiv1
	global VitXPlay
	global Vit_XPlay
	#Mur 1
	
	if -247>Niveau1_X>-290 and Player_Y > 284:
		d1 = 0
		d2 = 0
		d3 = 0
		Stopp()
		Chute()	
		VitXNiv1=0	
		VitXPlay = 0
		
		
#Détection de chutes en déplacement horizontal
def Chutes_mvmt():
	if 335<Player_X<505 and Player_Y > 449: #Trou 1
		Stopp()
		Chute()
	#Trou 2
	if -231>Niveau1_X>-249 and Player_Y > 449:
		Stopp()
		Chute()
	
	
	if 306 <= Player_Y <= 310 and (Player_X<100 or Niveau1_X<-165): #AJOUTER "XProchainePlateforme<Niveau1_X<-140" #Plateforme 1
		Stopp()
		Chute()
	#Mur 1
	if 280<=Player_Y<= 284 and not -246>Niveau1_X>-304:
		Stopp()
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
	Stopp()
	if LooseX == 0:
		LooseX -= 1500
		Fenetre.move(Loose,-1500,0)
	Compteur()
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

# Définitions

Game = Tk()
Game.title("RS I")
Game.geometry('1200x600+10+10')
Fenetre = Canvas(Game, width = 1200, height = 600, background = "black")

Vitesse_Depart = -3
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
cAv = 0
cRe = 0
TimeCAR = 10
Spam = 0


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

TempsA = 0
TempsB = 0


#Commandes de départ

Main()


	
	
	






Game.mainloop() #Lancement de la boucle principale
