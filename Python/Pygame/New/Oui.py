import pygame
import time
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((1200,1000))

gameDisplay.fill(blue)

Pix = pygame.PixelArray(gameDisplay)

Pix[10][10] = green

pygame.draw.line(gameDisplay,red,(200,300), (500,700),5)
pygame.draw.circle(gameDisplay,red,(50,50), 100)

pygame.draw.rect(gameDisplay,green,(150,150,200,100))

pygame.draw.polygon(gameDisplay,white,((140,5),(200,16),(25,546),(234,234),(63,546) ))

while True:
	a = time.time()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	
	
	pygame.display.update()
	b = time.time()
	print(1/(b-a))