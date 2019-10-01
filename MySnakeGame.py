# Snake Game!
import pygame, sys, random, time

# check for initializing errors
check_errors = pygame.init()
if check_errors[1] > 0:
	print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
	sys.exit(-1)
else:
	print("(+) PyGame successfully initialized!")

# Play surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake game!')

# Colors
red = pygame.Color(255, 0, 0) # gameover
green = pygame.Color(0, 255, 0) #snake
black = pygame.Color(0, 0, 0) #score
white = pygame.Color(255, 255, 255) #background
brown = pygame.Color(165, 42, 42) #food
blue = pygame.Color(0, 0, 250) #MainMenu
# FPS controller
fpsController = pygame.time.Clock()
fpsController.tick(10)

# Game over function
def gameOver(score):
	myFont = pygame.font.SysFont('monaco', 72)
	GOsurf = myFont.render('Game over!', True, red)
	GOrect = GOsurf.get_rect()
	GOrect.midtop = (360, 15)
	playSurface.blit(GOsurf,GOrect)
	showScore(score,0)
	pygame.display.update()
	time.sleep(3)
	MainMenu()
	
def showScore(score, choice=1):
	sFont = pygame.font.SysFont('monaco', 24)
	Ssurf = sFont.render('Score : {0}'.format(score) , True, black)
	Srect = Ssurf.get_rect()
	if choice == 1:
		Srect.midtop = (80, 10)
	else:
		Srect.midtop = (360, 120)
	playSurface.blit(Ssurf,Srect)
	
def showNewGame():
	NewFont = pygame.font.SysFont('serif', 30)
	Newsurf = NewFont.render('1. New Game', True, blue)
	Newrect = Newsurf.get_rect()
	Newrect.midtop = (360, 150)
	playSurface.blit(Newsurf, Newrect)

def showHelp():
	HelpFont = pygame.font.SysFont('serif', 30)
	Helpsurf = HelpFont.render('2. Help', True, blue)
	Helprect = Helpsurf.get_rect()
	Helprect.midtop = (320, 180)
	playSurface.blit(Helpsurf, Helprect)

def showAbout():
	AboutFont = pygame.font.SysFont('serif', 30)
	Aboutsurf = AboutFont.render('3. About', True, blue)
	Aboutrect = Aboutsurf.get_rect()
	Aboutrect.midtop = (330, 210)
	playSurface.blit(Aboutsurf, Aboutrect)

def showQuit():
	QuitFont = pygame.font.SysFont('serif', 30)
	Quitsurf = QuitFont.render('4. Quit', True, blue)
	Quitrect = Quitsurf.get_rect()
	Quitrect.midtop = (320, 240)
	playSurface.blit(Quitsurf, Quitrect)

# Main Logic of the game
def NewGame(tick):
	snakePos = [100, 50]
	snakeBody = [[100,50], [90,50], [80,50]]
	foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
	foodSpawn = True
	direction = 'RIGHT'
	changeto = direction
	score = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT or event.key == ord('d'):
					changeto = 'RIGHT' 
				if event.key == pygame.K_LEFT or event.key == ord('a'):
					changeto = 'LEFT' 
				if event.key == pygame.K_UP or event.key == ord('w'):
					changeto = 'UP' 
				if event.key == pygame.K_DOWN or event.key == ord('s'):
					changeto = 'DOWN' 
				if event.key == pygame.K_ESCAPE:
					pygame.event.post(pygame.event.Event(pygame.QUIT))

		# validation of direction
		if changeto == 'RIGHT' and not direction == 'LEFT':
			direction = 'RIGHT'
		if changeto == 'LEFT' and not direction == 'RIGHT':
			direction = 'LEFT'
		if changeto == 'UP' and not direction == 'DOWN':
			direction = 'UP'
		if changeto == 'DOWN' and not direction == 'UP':
			direction = 'DOWN'

		# Update snake position [x,y]
		if direction == 'RIGHT':
			snakePos[0] += 10
		if direction == 'LEFT':
			snakePos[0] -= 10
		if direction == 'UP':
			snakePos[1] -= 10
		if direction == 'DOWN':
			snakePos[1] += 10
		
		# Snake body mechanism
		snakeBody.insert(0, list(snakePos))
		if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
			score += 1
			foodSpawn = False
		else:
			snakeBody.pop()
			
		#Food Spawn
		if foodSpawn == False:
			foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10] 
		foodSpawn = True
		
		#Background
		playSurface.fill(white)
		
		#Draw Snake 
		for pos in snakeBody:
			pygame.draw.rect(playSurface, green, pygame.Rect(pos[0],pos[1],10,10))
		
		pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0],foodPos[1],10,10))
		
		# Bound
		if snakePos[0] > 710 or snakePos[0] < 0:
			gameOver(score)
		if snakePos[1] > 450 or snakePos[1] < 0:
			gameOver(score)
			
		# Self hit
		for block in snakeBody[1:]:
			if snakePos[0] == block[0] and snakePos[1] == block[1]:
				gameOver(score)
		
		showScore(score)
		pygame.display.update()
		fpsController.tick(tick)
		

def Help():
	while True:
		playSurface.fill(white)
		HelpFont = pygame.font.SysFont('times new roman', 20)
		Helpsurf = HelpFont.render('Use W, A, S, D or Up, Left, Down, Right arrow keys', True, blue)
		Helprect = Helpsurf.get_rect()
		Helprect.midtop = (350, 120)
		playSurface.blit(Helpsurf, Helprect)
		Helpsurf = HelpFont.render('to move the snake Up, Left, Down or Right respectively.', True, blue)
		Helprect = Helpsurf.get_rect()
		Helprect.midtop = (350, 140)
		playSurface.blit(Helpsurf, Helprect)
		Helpsurf = HelpFont.render('The objective of the game is to eat as many apples as possible!', True, blue)
		Helprect = Helpsurf.get_rect()
		Helprect.midtop = (350, 160)
		playSurface.blit(Helpsurf, Helprect)
		Helpsurf = HelpFont.render('Remember, the game will be over if you touch any of the', True, blue)
		Helprect = Helpsurf.get_rect()
		Helprect.midtop = (350, 180)
		playSurface.blit(Helpsurf, Helprect)
		Helpsurf = HelpFont.render('boundaries of the screen or touch your own snake body!', True, blue)
		Helprect = Helpsurf.get_rect()
		Helprect.midtop = (350, 200)
		playSurface.blit(Helpsurf, Helprect)
		Helpsurf = HelpFont.render('Good Luck! Press 9 to go back to Main Menu', True, blue)
		Helprect = Helpsurf.get_rect()
		Helprect.midtop = (350, 220)
		playSurface.blit(Helpsurf, Helprect)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == ord('9'):
					MainMenu()
		pygame.display.update()

def Difficulty():
	while True:
		playSurface.fill(white)
		SettingsFont = pygame.font.SysFont('calibri', 25)
		Settingssurf = SettingsFont.render('1. Easy', True, red)
		Settingsrect = Settingssurf.get_rect()
		Settingsrect.midtop = (340, 120)
		playSurface.blit(Settingssurf, Settingsrect)
		Settingssurf = SettingsFont.render('2. Medium', True, red)
		Settingsrect = Settingssurf.get_rect()
		Settingsrect.midtop = (340, 140)
		playSurface.blit(Settingssurf, Settingsrect)
		Settingssurf = SettingsFont.render('3. Hard', True, red)
		Settingsrect = Settingssurf.get_rect()
		Settingsrect.midtop = (340, 160)
		playSurface.blit(Settingssurf, Settingsrect)
		Settingssurf = SettingsFont.render('9. Main Menu', True, red)
		Settingsrect = Settingssurf.get_rect()
		Settingsrect.midtop = (340, 180)
		playSurface.blit(Settingssurf, Settingsrect)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == ord('1'):
					NewGame(10)
				if event.key == ord('2'):
					NewGame(20)
				if event.key == ord('3'):
					NewGame(30)
				if event.key == ord('9'):
					MainMenu()
		pygame.display.update()
			
def About():
	while True:
		playSurface.fill(white)
		AboutFont = pygame.font.SysFont('comic sans', 30)
		Aboutsurf = AboutFont.render('Snake Game by Kalpak, Janhavi and Snehal!', True, blue)
		Aboutrect = Aboutsurf.get_rect()
		Aboutrect.midtop = (360, 200)
		playSurface.blit(Aboutsurf, Aboutrect)
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == ord('9'):
						MainMenu()
		pygame.display.update()

def Quit():
	pygame.quit()
	sys.exit()

def MainMenu():
	while True:
		playSurface.fill(white)
		showNewGame()
		showHelp()
		showAbout()
		showQuit()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == ord('1'):
					Difficulty()
				if event.key == ord('2'):
					Help()
				if event.key == ord('3'):
					About()
				if event.key == ord('4'):
					Quit()
				if event.key == pygame.K_ESCAPE:
					pygame.event.post(pygame.event.Event(pygame.QUIT))
		pygame.display.update()
		
MainMenu()