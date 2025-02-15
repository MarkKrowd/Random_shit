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

def cube(startPoint, fullSize):
	node_1 = [startPoint[0],startPoint[1]]
	node_2 = [startPoint[0]+fullSize,startPoint[1]]
	node_3 = [startPoint[0]+fullSize,startPoint[1]+fullSize]
	node_4 = [startPoint[0],startPoint[1]+fullSize]
	
	offset = int(fullSize/2)
	
	x_mid = int(display_width / 2)
	x_offset = int(startPoint[0]-x_mid)
	
	y_mid = int(display_height / 2)
	y_offset = int(startPoint[1]-y_mid)
	
	
	node_5 = [node_1[0]+x_offset, node_1[1]+y_offset]
	node_6 = [node_2[0]+x_offset, node_2[1]+y_offset]
	node_7 = [node_3[0]+x_offset, node_3[1]+y_offset]
	node_8 = [node_4[0]+x_offset, node_4[1]+y_offset]
	
	
	pygame.draw.line(MichDisplay, white, (node_1),(node_2))
	pygame.draw.line(MichDisplay, white, (node_2),(node_3))
	pygame.draw.line(MichDisplay, white, (node_3),(node_4))
	pygame.draw.line(MichDisplay, white, (node_4),(node_1))
	pygame.draw.line(MichDisplay, white, (node_5),(node_6))
	pygame.draw.line(MichDisplay, white, (node_6),(node_7))
	pygame.draw.line(MichDisplay, white, (node_7),(node_8))
	pygame.draw.line(MichDisplay, white, (node_8),(node_5))
	pygame.draw.line(MichDisplay, white, (node_1),(node_5))
	pygame.draw.line(MichDisplay, white, (node_2),(node_6))
	pygame.draw.line(MichDisplay, white, (node_3),(node_7))
	pygame.draw.line(MichDisplay, white, (node_4),(node_8))
	
	pygame.draw.circle(MichDisplay,light_green, node_1, 5)
	pygame.draw.circle(MichDisplay,light_green, node_2, 5)
	pygame.draw.circle(MichDisplay,light_green, node_3, 5)
	pygame.draw.circle(MichDisplay,light_green, node_4, 5)
	
	pygame.draw.circle(MichDisplay,light_green, node_5, 5)
	pygame.draw.circle(MichDisplay,light_green, node_6, 5)
	pygame.draw.circle(MichDisplay,light_green, node_7, 5)
	pygame.draw.circle(MichDisplay,light_green, node_8, 5)
	


	
def Gameloop():

	location = [200,300]
	size = 200
	
	current_move = 0
	
	z_move = 0
	z_location = 1
	y_move = 0
	
	while True:
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					current_move = -5
				elif event.key == pygame.K_RIGHT:
					current_move = 5
					
					
				elif event.key == pygame.K_UP:
					y_move = -5
				elif event.key == pygame.K_DOWN:
					y_move = 5
				
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					current_move = 0
				elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_move = 0
		MichDisplay.fill(black)
		
		location[0] += current_move
		location[1] += y_move
		
		if 0 >z_location> 200:
			z_move = 0
		
		z_location += z_move
		
		current_size = int(size / (z_location))
		
		
		cube(location,current_size)
		pygame.display.update()
		
		clock.tick(FPS)
		

	pygame.quit()
	quit()

Gameloop()
