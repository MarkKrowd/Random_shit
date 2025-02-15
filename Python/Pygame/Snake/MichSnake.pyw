import pygame
import random
import time

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,190,0)

display_width = 800
display_height = 600
AppleThickness = 10
block_size = 10


clock = pygame.time.Clock()

FPS = 15
direction = "right"

MichDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('MichSnake')

icon = pygame.image.load("Apple2.png") #32x32
pygame.display.set_icon(icon)

img = pygame.image.load('Head.png')
appleimg = pygame.image.load("Apple.png")

smallfont = pygame.font.SysFont("comicsansms", 20)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

def pause():
	paused = True
	if paused == True:
		message_to_screen("Pause",black,-100,size="large")
		message_to_screen("Appuyez sur C pour continuer ou sur Q pour quitter",black)
	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					paused = False
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
		
		
		pygame.display.update()
		clock.tick(5)

def score(score):
	text = smallfont.render("Score: "+str(score), True, black)
	MichDisplay.blit(text, [0,0])

def game_intro():
	
	intro = True
	
	
	while intro:
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					intro = False
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
		
		MichDisplay.fill(white)
		message_to_screen("Bienvenue",green,-100,"large")
		message_to_screen("L'objectif est de manger les pommes rouges.", black, -30)
		message_to_screen("Plus vous mangerez de pommes, plus vous grandirez.", black)
		message_to_screen("Si vous vous mordez, vous perdrez!", black, 30)
		message_to_screen("Appuyez sur C pour jouer, P pour mettre en pause ou sur Q pour quitter.", black, 90)
		pygame.display.update()
		clock.tick(5)
		


def snake(block_size, snakeList):

	if direction == "right":
		head = pygame.transform.rotate(img, 270)
	if direction == "left":
		head = pygame.transform.rotate(img, 90)
	if direction == "up":
		head = img
	if direction == "down":
		head = pygame.transform.rotate(img, 180)
	
	MichDisplay.blit(head, (snakeList[-1][0],snakeList[-1][1]))
	
	for XnY in snakeList[:-1]:
		pygame.draw.rect(MichDisplay, green, [XnY[0],XnY[1],block_size,block_size])
		
def text_objects(text,color,size):
	if size == "small":
		textSurface = smallfont.render(text,True,color)
	if size == "medium":
		textSurface = medfont.render(text,True,color)
	if size == "large":
		textSurface = largefont.render(text,True,color)
	return textSurface, textSurface.get_rect()
		
		
def message_to_screen(msg,color, y_displace=0, size = "small"):
	textSurf, textRect = text_objects(msg,color,size)
	textRect.center = (display_width/2),(display_height/2)+y_displace
	MichDisplay.blit(textSurf,textRect)

def Gameloop():
	global direction
	MichExit = False
	MichOver = False
	direction = "right"

	lead_x = display_width/2
	lead_y = display_height/2
	
	lead_x_change = 0
	lead_y_change = 0
	
	snakeList = []
	snakeLenght = 1
	
	
	randAppleX = round(random.randrange(0,display_width-AppleThickness)/10)*10
	randAppleY = round(random.randrange(0,display_height-AppleThickness)/10)*10

	while not MichExit:
		a = time.time()
		if MichOver == True:
			message_to_screen("Aïe..." , red , y_displace=-50, size ="large")
			message_to_screen("Appuyez sur C pour recommencer ou sur Q pour quitter", black, y_displace = 50)
		while MichOver == True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					MichExit = True
					MichOver = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						MichExit = True
						MichOver = False
					if event.key == pygame.K_c:
						Gameloop()
			pygame.display.update()
			clock.tick(FPS)
			
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				MichExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					if direction == "right":
						pass
					else:
						lead_x_change = -block_size
						lead_y_change = 0
						direction = "left"
				elif event.key == pygame.K_RIGHT:
					if direction == "left":
						pass
					else:
						lead_x_change = block_size
						lead_y_change = 0
						direction = "right"
				elif event.key == pygame.K_DOWN:
					if direction == "up":
						pass
					else:
						lead_y_change = block_size
						lead_x_change = 0
						direction = "down"
				elif event.key == pygame.K_UP:
					if direction == "down":
						pass
					else:
						lead_y_change = -block_size
						lead_x_change = 0
						direction = "up"
				elif event.key == pygame.K_p:
					pause()
				elif event.key == pygame.K_q:
					pygame.quit()
					quit()
				
		lead_x += lead_x_change
		lead_y += lead_y_change
		
		if lead_x >= display_width or lead_x < 0 or lead_y < 0 or lead_y >= display_height:
			MichOver = True
			
		MichDisplay.fill(white)
		
		
		#pygame.draw.rect(MichDisplay, red, [randAppleX,randAppleY,AppleThickness,AppleThickness])
		MichDisplay.blit(appleimg,(randAppleX,randAppleY))
		
		snakeHead = []
		snakeHead.append(lead_x)
		snakeHead.append(lead_y)
		snakeList.append(snakeHead)
		
		if len(snakeList) > snakeLenght:
			del snakeList[0]
		
		for eachSegment in snakeList[:-1]:
			if eachSegment == snakeHead:
				MichOver = True
				
		snake(block_size, snakeList)
		
		score(snakeLenght-1)
		
		pygame.display.update()
		if randAppleX <= lead_x < randAppleX+AppleThickness and randAppleY <= lead_y < randAppleY+AppleThickness:
			randAppleX = round(random.randrange(0,display_width-AppleThickness)/10)*10
			randAppleY = round(random.randrange(0,display_height-AppleThickness)/10)*10
			snakeLenght += 1
			
		b = time.time()
		diff = b-a
		#print (1/(1/FPS-diff))
		clock.tick(1/(1/FPS-diff))
		

	pygame.quit()
	quit()
game_intro()
Gameloop()