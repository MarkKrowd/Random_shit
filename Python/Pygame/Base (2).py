import pygame
import time
import random
#ep 79


pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
yellow = (200,200,0)
green = (0,190,0)
light_green = (0,255,0)
light_yellow = (230,230,0)
light_red = (255,0,0)


display_width = 800
display_height = 600



clock = pygame.time.Clock()

FPS = 60


MichDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Pseudo3D')

#icon = pygame.image.load("icon.png") #32x32
#pygame.display.set_icon(icon)


smallfont = pygame.font.SysFont("comicsansms", 20)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)


	
def Gameloop():
	
	while True:
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					pass
				elif event.key == pygame.K_RIGHT:
					pass
				
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					pass
				elif event.key == pygame.K_RIGHT:
					pass
				
		MichDisplay.fill(black)
		
		clock.tick(FPS)
		

	pygame.quit()
	quit()

Gameloop()
