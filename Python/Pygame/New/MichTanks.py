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

fire_sound = pygame.mixer.Sound("Fire.wav")
explosion_sound = pygame.mixer.Sound("Xplosion.wav")


clock = pygame.time.Clock()

tankWidth = 40
tankHeight = 20


turretWidth = 5
wheelWidth = 5 
ground_height = int(display_height*0.1)-tankHeight-wheelWidth


FPS = 60

MichDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Tanks')

icon = pygame.image.load("icon.png") #32x32
pygame.display.set_icon(icon)

#img = pygame.image.load('Head.png')
#appleimg = pygame.image.load("Apple.png")

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

def barrier(xlocation,randomHeight,barrier_width):
	pygame.draw.rect(MichDisplay,black,[xlocation-barrier_width/2, display_height-randomHeight, barrier_width, randomHeight])
	
	
	
	
	
	
	
def score(score):
	text = smallfont.render("Score: "+str(score), True, black)
	MichDisplay.blit(text, [0,0])
	
def explosion(x,y,size=50):
	pygame.mixer.Sound.play(explosion_sound)
	explode = True
	
	while explode:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		startPoint = x,y
		colorChoices = [red, light_red,yellow,light_yellow]
		
		magnitude = 1
		while magnitude < size:
			exploding_bit_x = x + random.randrange(-1*magnitude,magnitude)
			exploding_bit_y = y + random.randrange(-1*magnitude,magnitude)
			
			pygame.draw.circle(MichDisplay, colorChoices[random.randrange(0,4)],(exploding_bit_x,exploding_bit_y),random.randrange(1,5))
			magnitude += 1
			pygame.display.update()
			clock.tick(100)
		explode = False
	
		
def fireShell(xy,tankx,tanky,turPos,gun_power,xlocation,barrier_width,randomHeight,enemyTankX,enemyTankY):
	
	fire = True
	startingShell = list(xy)
	global tankMove
	global changeTur
	global power_change
	mainTankSpeed = 2
	e_damage = 0
	
	while fire:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					if tankMove == -mainTankSpeed:
						tankMove = 0
					else:
						pass
				elif event.key == pygame.K_RIGHT:
					if tankMove == mainTankSpeed:
						tankMove = 0
					else:
						pass
				elif event.key == pygame.K_UP:
					if changeTur==1:
						changeTur = 0
				elif event.key == pygame.K_DOWN:
					if changeTur==-1:
						changeTur = 0
				elif event.key == pygame.K_a:
					if power_change == -1:
						power_change = 0
				elif event.key == pygame.K_d:
					if power_change == 1:
						power_change = 0
		
		pygame.draw.circle(MichDisplay,red,(startingShell[0],startingShell[1]),5)
		
		if tank == "enemy":
			startingShell[0] += (12 - turPos)*2	
		else:
			startingShell[0] -= (12 - turPos)*2
		startingShell[1] += int((((startingShell[0]-xy[0])*0.015/(gun_power/50))**2) - (turPos+turPos/(12-turPos)))
		
		if startingShell[1] > display_height-ground_height:
			hit_x = int((startingShell[0]*(display_height-ground_height))/startingShell[1])
			hit_y = int(display_height-ground_height)
			if enemyTankX + 10 > hit_x > enemyTankX - 10:
				e_damage = 25
			elif enemyTankX + 15 > hit_x > enemyTankX - 15:
				e_damage = 18
			elif enemyTankX + 25 > hit_x > enemyTankX - 25:
				e_damage = 10
			elif enemyTankX + 35 > hit_x > enemyTankX - 35:
				e_damage = 5
			explosion (hit_x,hit_y)
			fire = False
			
		
		check_x_1 = startingShell[0] <= xlocation + barrier_width/2
		check_x_2 = startingShell[0] >= xlocation - barrier_width/2
		
		check_y_1 = startingShell[1] <= display_height
		check_y_2 = startingShell[1] >= display_height - randomHeight
		
		if check_x_1 and check_x_2 and check_y_1 and check_y_2:
			hit_x = int(startingShell[0])
			hit_y = int(startingShell[1])
			explosion (int(xlocation + barrier_width/2),hit_y)
			fire = False
		
		pygame.display.update()
		clock.tick(60)
	return e_damage
def e_fireShell(xy,tankx,tanky,turPos,gun_power,xlocation,barrier_width,randomHeight,ptankX,ptankY):
	
	damage = 0
	currentPower = 10
	power_found = False
	
	while not power_found:
		currentPower += 1
		if currentPower > 100:
			power_found = True
		fire = True
		startingShell = list(xy)
		
		while fire:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			
			#pygame.draw.circle(MichDisplay,red,(startingShell[0],startingShell[1]),5)
			
			
			startingShell[0] += (12 - turPos)*2	
			
			startingShell[1] += int((((startingShell[0]-xy[0])*0.015/(currentPower/50))**2) - (turPos+turPos/(12-turPos)))
			
			if startingShell[1] > display_height-ground_height:
				hit_x = int((startingShell[0]*(display_height-ground_height))/startingShell[1])
				hit_y = int(display_height-ground_height)
				#explosion (hit_x,hit_y)
				if ptankX + 5 > hit_x > ptankX-5:
					power_found = True
				fire = False
			
			
			check_x_1 = startingShell[0] <= xlocation + barrier_width/2
			check_x_2 = startingShell[0] >= xlocation - barrier_width/2
			
			check_y_1 = startingShell[1] <= display_height
			check_y_2 = startingShell[1] >= display_height - randomHeight
			
			if check_x_1 and check_x_2 and check_y_1 and check_y_2:
				hit_x = int(startingShell[0])
				hit_y = int(startingShell[1])
				#explosion (int(xlocation + barrier_width/2),hit_y)
				fire = False


	fire = True
	startingShell = list(xy)
	gun_power = random.randrange(int(currentPower*0.9), int(currentPower*1.1))
	while fire:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		pygame.draw.circle(MichDisplay,red,(startingShell[0],startingShell[1]),5)
		
		
		startingShell[0] += (12 - turPos)*2	
		
		
		startingShell[1] += int((((startingShell[0]-xy[0])*0.015/(gun_power/50))**2) - (turPos+turPos/(12-turPos)))
		
		if startingShell[1] > display_height-ground_height:
			hit_x = int((startingShell[0]*(display_height-ground_height))/startingShell[1])
			hit_y = int(display_height-ground_height)
			if ptankX + 10 > hit_x > ptankX - 10:
				damage = 25
			elif ptankX + 15 > hit_x > ptankX - 15:
				damage = 18
			elif ptankX + 25 > hit_x > ptankX - 25:
				damage = 10
			elif ptankX + 35 > hit_x > ptankX - 35:
				damage = 5
			explosion (hit_x,hit_y)
			fire = False
		
		
		
		check_x_1 = startingShell[0] <= xlocation + barrier_width/2
		check_x_2 = startingShell[0] >= xlocation - barrier_width/2
		
		check_y_1 = startingShell[1] <= display_height
		check_y_2 = startingShell[1] >= display_height - randomHeight
		
		if check_x_1 and check_x_2 and check_y_1 and check_y_2:
			hit_x = int(startingShell[0])
			hit_y = int(startingShell[1])
			explosion (int(xlocation + barrier_width/2),hit_y)
			fire = False
		
		
		
		pygame.display.update()
		clock.tick(60)
	return damage
	
		
def power(level):
	text = smallfont.render("Power:"+str(level)+"%",True,black)
	MichDisplay.blit(text,[display_width/2,0])

def game_intro():
	
	intro = True
	gcont = False
	
	while intro:
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		MichDisplay.fill(white)
		message_to_screen("Tanks",green,-100,"large")
		message_to_screen("L'objectif est de tirer sur les adversaires", black, -30)
		message_to_screen("avant qu'ils ne vous tirent dessus.", black)
		message_to_screen("Plus vous detruirez d'adversaires, plus ils seront coriaces!", black, 30)
		#message_to_screen("Appuyez sur C pour jouer, P pour mettre en pause ou sur Q pour quitter.", black, 90)

		button("Jouer", 150,500,100,50, green, light_green, action = "play")
		button("Controles", 350,500,100,50, yellow, light_yellow, action = "controls")
		button("Quitter", 550,500,100,50, red, light_red, action = "quit")
		
		
		pygame.display.update()
		clock.tick(FPS)
		
def game_over():
	
	game_over = True
	gcont = False
	
	while game_over:
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
		
		MichDisplay.fill(white)
		message_to_screen("Game Over",green,-100,"large")
		message_to_screen("Vous avez mouru.", black, -30)
		
		
		#message_to_screen("Appuyez sur C pour jouer, P pour mettre en pause ou sur Q pour quitter.", black, 90)

		button("Recommencer", 150,500,150,50, green, light_green, action = "play")
		button("Controles", 350,500,100,50, yellow, light_yellow, action = "controls")
		button("Quitter", 550,500,100,50, red, light_red, action = "quit")
		
		
		pygame.display.update()
		clock.tick(FPS)

def you_win():
	
	win = True
	gcont = False
	
	while win:
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
		
		MichDisplay.fill(white)
		message_to_screen("Vous avez gagne",green,-100,"large")
		message_to_screen("Toutes mes ficelles de calecon", black, -30)
		
		
		#message_to_screen("Appuyez sur C pour jouer, P pour mettre en pause ou sur Q pour quitter.", black, 90)

		button("Rejouer", 150,500,150,50, green, light_green, action = "play")
		button("Controles", 350,500,100,50, yellow, light_yellow, action = "controls")
		button("Quitter", 550,500,100,50, red, light_red, action = "quit")
		
		
		pygame.display.update()
		clock.tick(FPS)			
		
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
	
		
def message_to_screen(msg,color, y_displace=0, size = "small"):
	textSurf, textRect = text_objects(msg,color,size)
	textRect.center = (display_width/2),(display_height/2)+y_displace
	MichDisplay.blit(textSurf,textRect)
	
def tank(x,y,turPos):
	x = int(x)
	y = int(y)
	Wheels = 8
	
	possibleTurrets = [(x-27, y-2),(x-26, y-5),(x-25, y-8),(x-23, y-12),(x-20, y-14),(x-18, y-15),(x-15, y-17),(x-13, y-19),(x-11, y-21)]
	
	pygame.draw.circle(MichDisplay, black, (x,y), int(tankHeight/2))
	pygame.draw.rect(MichDisplay,black,(x-(tankWidth/2),y,tankWidth,tankHeight))
	
	pygame.draw.line(MichDisplay, black, (x,y), possibleTurrets[turPos], turretWidth)
	
	for n in range(Wheels):
		pygame.draw.circle(MichDisplay,black,(int(x-tankWidth/2+(tankWidth/Wheels)*n+(tankWidth/(2*Wheels))), y+tankHeight), wheelWidth)
	return possibleTurrets[turPos]
	
def enemy_tank(x,y,turPos):
	x = int(x)
	y = int(y)
	Wheels = 8
	
	possibleTurrets = [(x+27, y-2),(x+26, y-5),(x+25, y-8),(x+23, y-12),(x+20, y-14),(x+18, y-15),(x+15, y-17),(x+13, y-19),(x+11, y-21)]
	
	pygame.draw.circle(MichDisplay, black, (x,y), int(tankHeight/2))
	pygame.draw.rect(MichDisplay,black,(x-(tankWidth/2),y,tankWidth,tankHeight))
	
	pygame.draw.line(MichDisplay, black, (x,y), possibleTurrets[turPos], turretWidth)
	
	for n in range(Wheels):
		pygame.draw.circle(MichDisplay,black,(int(x-tankWidth/2+(tankWidth/Wheels)*n+(tankWidth/(2*Wheels))), y+tankHeight), wheelWidth)
	return possibleTurrets[turPos]
	

def game_controls():
	gcont = True
	intro = False
	
	
	while gcont:
	
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
		message_to_screen("Controles",green,-100,"large")
		message_to_screen("Tirer: Espace", black, -30)
		message_to_screen("Deplacer le canon: Fleches haut et bas", black)
		message_to_screen("Deplacer le tank: Fleches gauche et droite", black, 30)
		#message_to_screen("Appuyez sur C pour jouer, P pour mettre en pause ou sur Q pour quitter.", black, 90)

		button("Jouer", 150,500,100,50, green, light_green, action = "play")
		button("Retour", 350,500,100,50, yellow, light_yellow, action = "retour")
		button("Quitter", 550,500,100,50, red, light_red, action = "quit")
		
		
		pygame.display.update()
		clock.tick(FPS)
	
def button(text, x, y, width, height, inactive_color, active_color, action = None):
	cur = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if x + width > cur[0] > x and y + height > cur[1] > y:
		pygame.draw.rect(MichDisplay, active_color, (x,y,width,height))
		if click[0] == 1 and action != None:
			if action == "quit":
				pygame.quit()
			elif action == "controls":
				
				game_controls()
			elif action == "play":
				Gameloop()
			elif action == "retour":
				
				game_intro()
				
	else:
		pygame.draw.rect(MichDisplay, inactive_color, (x,y,width,height))
	text_to_button(text,black,x,y,width,height)

def health_bars(player_health, enemy_health):
		
	if player_health > 75:
		player_health_color = green
	elif player_health > 50:
		player_health_color = yellow
	else:
		player_health_color = red
			
	if enemy_health > 75:
		enemy_health_color = green
	elif enemy_health > 50:
		enemy_health_color = yellow
	else:
		enemy_health_color = red
			
	pygame.draw.rect(MichDisplay, player_health_color, (display_width-120,25,player_health,25))
	pygame.draw.rect(MichDisplay, enemy_health_color, (20,25,enemy_health,25))
	
def Gameloop():
	global direction
	global tankMove
	global changeTur
	global power_change
	MichExit = False
	MichOver = False
	
	barrier_width = 30
	mainTankSpeed = 2
	
	player_health = 100
	enemy_health = 100
	
	fire_power=50
	power_change = 0
	
	mainTankX = display_width *0.9
	mainTankY = display_height *0.9
	tankMove = 0
	
	enemyTankX = display_width *0.1
	enemyTankY = display_height *0.9
	
	currentTurPos = 0
	changeTur = 0
	xlocation = (display_width/2) + random.randint(-0.2*display_width, 0.2*display_width)
	randomHeight = random.randrange(display_height*0.1,display_height*0.4)
	
	
	while not MichExit:
		
		if MichOver == True:
			message_to_screen("Aie..." , red , y_displace=-50, size ="large")
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
			
		
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					tankMove = -mainTankSpeed
				elif event.key == pygame.K_RIGHT:
					tankMove = mainTankSpeed
				elif event.key == pygame.K_UP:
					changeTur = 1
				elif event.key == pygame.K_DOWN:
					changeTur = -1
				elif event.key == pygame.K_p:
					pause()
				elif event.key == pygame.K_q:
					pygame.quit()
					quit()
				elif event.key == pygame.K_SPACE:
					pygame.mixer.Sound.play(fire_sound)
					e_damage = fireShell(gun,mainTankX,mainTankY,currentTurPos,fire_power,xlocation,barrier_width,randomHeight,enemyTankX,enemyTankY)
					enemy_health -= e_damage
					
					possibleMovement = ["f","r"]
					moveIndex = random.randrange(0,2)
					
					for x in range(random.randrange(0,10)):
						if display_width *0.3 > enemyTankX > display_width * 0.03:
							if possibleMovement[moveIndex] == "f":
								enemyTankX += 5
							elif possibleMovement[moveIndex] == "r":
								enemyTankX -=5
							
							MichDisplay.fill(white)
							health_bars(player_health, enemy_health)
							gun = tank(mainTankX,mainTankY,currentTurPos)
							enemy_gun = enemy_tank(enemyTankX,enemyTankY,8)
							fire_power += power_change
							if fire_power < 10:
								fire_power += 1
							elif fire_power > 100:
								fire_power -= 1
							power(fire_power)
		
		
							barrier(xlocation,randomHeight,barrier_width)
							MichDisplay.fill(green, rect=[0,display_height-ground_height, display_width, ground_height])
							
							pygame.display.update()
							clock.tick(FPS)
					pygame.mixer.Sound.play(fire_sound)
					damage = e_fireShell(enemy_gun,enemyTankX,enemyTankY,8,50,xlocation,barrier_width,randomHeight,mainTankX,mainTankY)
					player_health -= damage
					
				elif event.key == pygame.K_a:
					power_change = -1
				elif event.key == pygame.K_d:
					power_change = 1
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					if tankMove== -mainTankSpeed:
						tankMove = 0
					else:
						pass
				elif event.key == pygame.K_RIGHT:
					if tankMove== mainTankSpeed:
						tankMove = 0
					else:
						pass
				elif event.key == pygame.K_UP:
					if changeTur==1:
						changeTur = 0
				elif event.key == pygame.K_DOWN:
					if changeTur==-1:
						changeTur = 0
				elif event.key == pygame.K_a:
					if power_change == -1:
						power_change = 0
				elif event.key == pygame.K_d:
					if power_change == 1:
						power_change = 0
					
		
		mainTankX += tankMove
		currentTurPos += changeTur
		if currentTurPos > 8:
			currentTurPos = 8
		elif currentTurPos < 0:
			currentTurPos = 0
			
		if mainTankX - (tankWidth/2) < xlocation + (barrier_width/2):
			mainTankX += mainTankSpeed
		elif mainTankX + (tankWidth/2) > display_width:
			mainTankX -= mainTankSpeed
		MichDisplay.fill(white)
		
		health_bars(player_health, enemy_health)
		
		gun = tank(mainTankX,mainTankY,currentTurPos)
		enemy_gun = enemy_tank(enemyTankX,enemyTankY,8)
		fire_power += power_change
		
		
		if fire_power < 10:
			fire_power += 1
		elif fire_power > 100:
			fire_power -= 1
		power(fire_power)
		
		
		barrier(xlocation,randomHeight,barrier_width)
		MichDisplay.fill(green, rect=[0,display_height-ground_height, display_width, ground_height])
		
		pygame.display.update()
		
		if player_health < 1:
			game_over()
		elif enemy_health < 1:
			you_win()
		
		clock.tick(FPS)
		

	pygame.quit()
	quit()

game_intro()
