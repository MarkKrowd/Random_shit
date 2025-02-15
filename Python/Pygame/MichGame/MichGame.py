# -*- coding: utf-8 -*-
from __future__ import division

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import random
import numpy as np
import math
import sys
import tkinter as Tkinter
import time



root = Tkinter.Tk()
pygame.mixer.pre_init(44100, -16, 10, 2048)
pygame.mixer.init()
pygame.init()

blanc = (255,255,255)
noir = (0,0,0)
rouge = (200,0,0)
jaune = (200,200,0)
vert = (0,190,0)
vert_clair = (0,255,0)
jaune_clair = (230,230,0)
rouge_clair = (255,0,0)
gris_clair = (191,191,191)
gris_moyen = (134,134,134)
gris_fonce = (75,75,75)
bleu = (43,19,255)
bleu_clair = (65,157,250)

FPS = 60

largeur_ecran = 1280
hauteur_ecran = 720

display  = (largeur_ecran,hauteur_ecran)

MichDisplay = pygame.display.set_mode(display)
pygame.display.set_caption('MichGame')

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms", 20)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

fullscreen = False
Bratwurst = False
Currywurst = False

Bouton_FR = pygame.mixer.Sound("Sounds/Bouton_FR.wav")
Bouton_EN = pygame.mixer.Sound("Sounds/Bouton_EN.wav")
Bouton_DE = pygame.mixer.Sound("Sounds/Bouton_DE.wav")
Bouton_ET = pygame.mixer.Sound("Sounds/Bouton_ET.wav")

Main_FR = pygame.mixer.Sound("Sounds/Main_FR.wav")
Main_DE = pygame.mixer.Sound("Sounds/Main_DE.wav")
Main_EN = pygame.mixer.Sound("Sounds/Main_EN.wav")
Main_ET = pygame.mixer.Sound("Sounds/Main_ET.wav")


Jy = 0
Jx = 0
Language = "Frouzien"

saucisse1 = pygame.image.load("Graphics/Currywurst.png")
saucisse2 = pygame.image.load("Graphics/Bratwurst.png")

Dico_FR = ("Jouer", #0
			"Options", #1
			"Quitter", #2
			"Taille de l'interface", #3
			"Ecran plein (la taille de l'interface n'aura pas d'importance)", #4
			"Language", #5
			"Oui", #6
			"Non", #7
			"Appliquer", #8
			"Annuler" #9
			)
			
Dico_EN = ("Play", #0
			"Settings", #1
			"Quit", #2
			"Screen size", #3
			"Fullscreen (then the size doesn't matter)", #4
			"Language", #5
			"Yes", #6
			"No", #7
			"Apply", #8
			"Cancel" #9
			)

Dico_DE = ("Spielen", #0
			"Optionen", #1
			"Beenden", #2
			"Schnittstellengroesse", #3
			"Vollbild (die Groesse der Benutzeroberflaeche spielt keine Rolle)", #4
			"Sprache", #5
			"Ja", #6
			"Nein", #7
			"Ubernehmen", #8
			"Abbrechen", #9
			"Bratwurst", #-2
			"Currywurst" #-1
			)

Dico_ET = ("010010110010", #0
			"0100110111001110011", #1
			"0101010010101110010", #2
			"01010100101", #3
			"Penis", #4
			"01000101", #5
			"1", #6
			"0", #7
			"01000011101011", #8
			"T'as pas de couilles Bob" #9
			)
			
Dico = Dico_FR

def text_objects(text,color,size):
	if size == "small":
		textSurface = smallfont.render(text,True,color)
	if size == "medium":
		textSurface = medfont.render(text,True,color)
	if size == "large":
		textSurface = largefont.render(text,True,color)
	return textSurface, textSurface.get_rect()
		
def text_to_button(msg, color, buttonx, buttony ,buttonwidth ,buttonheight ,size="small"):
	textSurf,textRect = text_objects(msg,color,size)
	textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
	MichDisplay.blit(textSurf,textRect)
	
		
def message_to_screen(msg,color, x_central, y_central, size = "small"):
	textSurf, textRect = text_objects(msg,color,size)
	textRect.center = x_central, y_central
	MichDisplay.blit(textSurf,textRect)

	

	

def Bouton(x_centre, y_centre, texte, couleur_passive, couleur_active, fonction = None):
	global new_hauteur_ecran
	global new_largeur_ecran
	global fullscreen
	global options
	global Appliquer
	global Language
	global Bratwurst
	global Currywurst
	
	cur = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	
	largeur_bouton = 40
	hauteur_bouton = 60
	
	for letters in texte:
		largeur_bouton += 10
	
	
	
		
	x = x_centre - (largeur_bouton/2)
	y = y_centre - (hauteur_bouton/2)
	
	if x + largeur_bouton > cur[0] > x and y + hauteur_bouton > cur[1] > y:
		pygame.draw.rect(MichDisplay, couleur_active, (x,y,largeur_bouton,hauteur_bouton))
		if click[0] == 1 and fonction != None:
			if fonction == "Language":
				if Language == "Frouzien":
					Language = "English"
					pygame.mixer.Sound.stop(Main_FR)
					pygame.mixer.Sound.play(Main_EN, -1)
				elif Language == "English":
					Language = "Deutsch"
					pygame.mixer.Sound.stop(Main_EN)
					pygame.mixer.Sound.play(Main_DE, -1)
				elif Language == "Deutsch":
					Language = "E.T."
					pygame.mixer.Sound.stop(Main_DE)
					pygame.mixer.Sound.play(Main_ET, -1)
				elif Language == "E.T.":
					Language = "Frouzien"	
					pygame.mixer.Sound.stop(Main_ET)
					pygame.mixer.Sound.play(Main_FR, -1)
				clock.tick(5)
			if Language == "Frouzien" and fonction!=Options:
				pygame.mixer.Sound.play(Bouton_FR)
			elif Language == "Deutsch" and fonction!=Options:
				pygame.mixer.Sound.play(Bouton_DE)
			elif Language == "English" and fonction!=Options:
				pygame.mixer.Sound.play(Bouton_EN)
			elif Language == "E.T." and fonction!=Options:
				pygame.mixer.Sound.play(Bouton_ET)
			if fonction == "Quitter":
				pygame.quit()
				quit()
			elif fonction == "Jouer":
				Jeu()
				clock.tick(5)
			elif fonction == "Options":
				if Language == "Frouzien":
					pygame.mixer.Sound.play(Bouton_FR)
				elif Language == "Deutsch":
					pygame.mixer.Sound.play(Bouton_DE)
				elif Language == "English":
					pygame.mixer.Sound.play(Bouton_EN)
				elif Language == "E.T.":
					pygame.mixer.Sound.play(Bouton_ET)
				Options()
				clock.tick(5)
			elif fonction == "Change_Taille":
				if new_largeur_ecran == 1280:
					new_largeur_ecran = 1920
				elif new_largeur_ecran == 1920:
					new_largeur_ecran = 800
				elif new_largeur_ecran == 800:
					new_largeur_ecran = 1280
				elif new_largeur_ecran != 0:
					new_largeur_ecran = 800
				if new_hauteur_ecran == 720:
					new_hauteur_ecran = 1080
				elif new_hauteur_ecran == 1080:
					new_hauteur_ecran = 600
				elif new_hauteur_ecran == 600:
					new_hauteur_ecran = 720
				elif new_hauteur_ecran != 0:
					new_hauteur_ecran = 600
				clock.tick(5)
			elif fonction == "Fullscreen":
				if fullscreen:
					fullscreen = False
				else:
					fullscreen = True
				clock.tick(5)
			elif fonction == "Appliquer":
				Appliquer = True
				options = False
				clock.tick(5)
			elif fonction == "Annuler":
				options = False
				clock.tick(5)
			
			elif fonction == "Bratwurst":
				Bratwurst = True	
				clock.tick(5)				
			elif fonction == "Currywurst":
				Currywurst = True
				clock.tick(5)
			
			
				
			
				
	else:
		pygame.draw.rect(MichDisplay, couleur_passive, (x,y,largeur_bouton,hauteur_bouton))
	
	text_to_button(texte, noir,x,y,largeur_bouton,hauteur_bouton)
	
	
def Options():
	global new_hauteur_ecran
	global new_largeur_ecran
	global fullscreen
	global Appliquer
	global largeur_ecran
	global hauteur_ecran
	global display
	global MichDisplay
	global options
	global Dico
	global Jy
	global Jx
	Appliquer = False
	options = True
	Txt_bouton_fullscreen = ""
	new_largeur_ecran = largeur_ecran
	new_hauteur_ecran = hauteur_ecran
	
	
	while options:
		MichDisplay.fill(noir)
		if fullscreen:
			Txt_bouton_fullscreen = Dico[6]
		if not fullscreen:
			Txt_bouton_fullscreen = Dico[7]
			
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		message_to_screen(Dico[3], blanc, largeur_ecran/2, hauteur_ecran/2 -160)
		Bouton(largeur_ecran/2, hauteur_ecran/2 -110, (str(new_largeur_ecran) + " x " + str(new_hauteur_ecran)), bleu, bleu_clair, fonction = "Change_Taille")
		message_to_screen(Dico[4], blanc, largeur_ecran/2, hauteur_ecran/2 -60)
		Bouton(largeur_ecran/2, hauteur_ecran/2 -10, str(Txt_bouton_fullscreen), bleu, bleu_clair, fonction = "Fullscreen")
		message_to_screen(Dico[5], blanc, largeur_ecran/2, hauteur_ecran/2 + 40)	
		Bouton(largeur_ecran/2, hauteur_ecran/2 +90, Language, bleu, bleu_clair, fonction = "Language")
		
		
		
		
		Bouton(largeur_ecran/2 - 200, hauteur_ecran/2 + 170, Dico[9] , rouge, rouge_clair, fonction = "Annuler")
		Bouton(largeur_ecran/2 + 200, hauteur_ecran/2 + 170, Dico[8] , rouge, rouge_clair, fonction = "Appliquer")
		
		pygame.display.update()
		clock.tick(FPS)
	if Appliquer and not fullscreen:
		
		Jy = Jy/hauteur_ecran*new_hauteur_ecran
		
		largeur_ecran = new_largeur_ecran
		hauteur_ecran = new_hauteur_ecran
		
		display  = (largeur_ecran,hauteur_ecran)
		MichDisplay = pygame.display.set_mode(display)
	elif Appliquer and fullscreen:
		
		Jy = Jy/hauteur_ecran*root.winfo_screenheight()
		
		largeur_ecran = root.winfo_screenwidth()
		hauteur_ecran = root.winfo_screenheight()	
	
		display  = (largeur_ecran,hauteur_ecran)
		MichDisplay = pygame.display.set_mode(display, FULLSCREEN)
	if Language == "Frouzien":
		Dico = Dico_FR
	elif Language == "English":
		Dico = Dico_EN
	elif Language == "Deutsch":
		Dico = Dico_DE
	elif Language == "E.T.":
		Dico = Dico_ET
	pygame.display.update()
	
	




def main():
	main = True
	pygame.mixer.Sound.play(Main_FR, -1)
	while main:
		MichDisplay.fill(noir)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
		
		
		
		
		
		Bouton(largeur_ecran/2, hauteur_ecran/2, Dico[0], rouge, rouge_clair, "Jouer")
		Bouton(largeur_ecran-80, 40, Dico[1], rouge, rouge_clair, "Options")
		Bouton(80, 40, Dico[2], rouge, rouge_clair, "Quitter")
		if Language == "Deutsch":	
			Bouton(largeur_ecran-80, hauteur_ecran - 40, Dico[-1], rouge, rouge_clair, "Bratwurst")
			Bouton(80, hauteur_ecran - 40, Dico[-2], rouge, rouge_clair, "Currywurst")
		
		if Bratwurst == 1:
			MichDisplay.blit(saucisse1, (120, 300))
		if Currywurst == 1:
			MichDisplay.blit(saucisse2, (largeur_ecran-320, 300))
		
		
		pygame.display.update()
		clock.tick(FPS)
		
def Jeu():

	global Jy
	
	Jeu = True
	
	Scene = 0
	Level = 0
	
	Jx = 50
	Jy = -50
	
	X_acc = 0
	
	ARF = 1
	
	Jy_Orig = 0
	
	T_Chute = 0
	Vitesse_x = 0
	Vitesse_y = 0
	Vitesse = 0
	
	Vitesse_actuelle = 10
	
	dUp = 1
	gUp = 1
	V0 = 0
	
	TLStart = 0
	TLStop = 0
	while Jeu:
		TLStart = time.time()
		MichDisplay.fill(noir)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					if Jx > hauteur_ecran/60:
						Vitesse_x = -Vitesse_actuelle
						gUp = 0
						dUp = 1
				elif event.key == pygame.K_RIGHT:
					Vitesse_x = Vitesse_actuelle
					dUp = 0
					gUp = 1
				elif event.key == pygame.K_SPACE:
					V0 = -hauteur_ecran*0.8
					ARF = 1
					
					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					if gUp == 0:
						Vitesse_x = 0
					gUp = 1
					
				elif event.key == pygame.K_RIGHT:
					if dUp == 0:
						Vitesse_x = 0
					dUp = 1
				
				
				
		if Level == 0:
			#1m = hauteur_ecran/10
			#g = 1/2*9.81*ecran/10*t**2
			#v = 9.81*ecran/10*t
			
			if (Jy < hauteur_ecran*0.9-(hauteur_ecran/60) or ARF == 1) and T_Chute == 0:
				Jy_Orig = Jy
				T_Chute = 1.00000000/FPS
				ARF = 0
			elif T_Chute == 0 and Jy == hauteur_ecran*0.9-hauteur_ecran/60:
				pass
			elif Jy < hauteur_ecran*0.9 or V0 != 0:
				Jy = 4.905*0.1*hauteur_ecran*(T_Chute**2)+Jy_Orig+(V0*T_Chute)
				Vitesse_y = 9.81*T_Chute*hauteur_ecran/10 + V0
				#print("Vitesse_verticale = " + str(Vitesse_y/hauteur_ecran*10) + " m/s, " + str(Vitesse_y*3.6/hauteur_ecran*10) + " km/h")
				if (4.905*0.1*hauteur_ecran*(T_Chute**2)+Jy_Orig+(V0*T_Chute)) > hauteur_ecran*0.9-(hauteur_ecran/60):
					Jy = hauteur_ecran*0.9-(hauteur_ecran/60)
					if Vitesse_y/hauteur_ecran*10 > 10:
						Splash()		
						pygame.mixer.Sound.play(Bouton_DE)
					
					elif Vitesse_y != 0:
						pygame.mixer.Sound.play(Bouton_FR)
					if Vitesse_y*10/hauteur_ecran<1:
						V0 = 0
						T_Chute = 0
						Vitesse_y = 0
					V0 = -Vitesse_y/2
					T_Chute = 1/FPS
					Vitesse_y = -Vitesse_y/2
					Jy_Orig = Jy
					
				if T_Chute != 0:
					T_Chute += 1.00000000/FPS	
					
			
			
			if Vitesse_x == Vitesse_actuelle:
				X_acc += Vitesse_actuelle/10.00000
				if X_acc > Vitesse_actuelle:
					X_acc = Vitesse_actuelle
				Jx += X_acc	
			elif Vitesse_x == 0 and dUp == 1 and X_acc>0:
				X_acc -= Vitesse_actuelle/10.00000
				if X_acc < 0:
					X_acc = 0
				Jx += X_acc
			elif Vitesse_x == -Vitesse_actuelle:
				X_acc -= Vitesse_actuelle/10.00000
				if X_acc < -Vitesse_actuelle:
					X_acc = -Vitesse_actuelle
				Jx += X_acc	
			elif Vitesse_x == 0 and gUp == 1 and X_acc<0:
				X_acc += Vitesse_actuelle/10.00000
				if X_acc > 0:
					X_acc = 0
				Jx += X_acc
			
			if Jx-(hauteur_ecran/60) < 0 :
				pygame.mixer.Sound.play(Bouton_FR)
				Jx = (hauteur_ecran/60)		
				X_acc = -X_acc
				if X_acc == 0.3:
					X_acc = 0
			if X_acc != 0:
				#print("Vitesse_horizontale = " + str(X_acc) + " m/s, " + str(X_acc*3.6) + " km/h")
				pass
			Joueur_0(Jx,Jy)
			if ((X_acc**2+Vitesse_y**2)**0.5) != 0:
				print("Vitesse_absolue = " + str((X_acc**2+(Vitesse_y/hauteur_ecran*10)**2)**0.5) + " m/s, " + str(((X_acc**2+(Vitesse_y/hauteur_ecran*10)**2)**0.5)*3.6) + " km/h")
				pass
		if Level == 1:
			pass
		
		if Scene == 0:
			Decor_0()
		elif Scene == 2:
			pass
			
		
			
		
		Bouton(largeur_ecran-80, 40, Dico[1], rouge, rouge_clair, "Options")
		Bouton(80, 40, Dico[2], rouge, rouge_clair, "Quitter")
		pygame.display.update()
		TLStop = time.time()
		
		
		if (TLStop-TLStart)<(1/FPS):
			
			time.sleep((1/FPS)-(TLStop-TLStart))
		else:
			message_to_screen("FPSSS",rouge,largeur_ecran/2,hauteur_ecran/2,"large")
	
def Decor_0():
	pygame.draw.rect(MichDisplay,blanc,(0,hauteur_ecran*0.9,largeur_ecran, hauteur_ecran*0.1))

def Joueur_0(X,Y):
	X = int(X)
	Y = int(Y)
	h = int(hauteur_ecran/60)
	pygame.draw.circle(MichDisplay,rouge,(X,Y),h)
	
def Splash():
	print("GAME OVER")
	
	
	
	

main()
pygame.quit()
quit()