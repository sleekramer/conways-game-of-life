import math
import random
import pygame

black = (0,  0,  0)
white = (255,255,255)
darkgrey = (40, 40, 40)
red = (220,20,60)
b_red = (255,0,0)
green = (0,200,0)
b_green = (0,255,0)

def round_up_nearest_ten(n):
	return int(math.ceil(n / 10.0)) * 10

# create a conway glider
def create_glider(gridDict, x, y):
	x = round_up_nearest_ten(x)
	y = round_up_nearest_ten(y)

	#catches when drawn pixels are off of screen
	try:
		# draw one of four orientations for glider
		direction = random.randint(0,3)
		if direction == 0:
			gridDict[x,y].stat = 1
			gridDict[x+10,y-10].stat = 1
			gridDict[x+20,y+10].stat = 1
			gridDict[x+20,y].stat = 1
			gridDict[x+20,y-10].stat = 1
		elif direction == 1:
			gridDict[x,y].stat = 1
			gridDict[x-10,y-10].stat = 1
			gridDict[x-10,y-20].stat = 1
			gridDict[x,y-20].stat = 1
			gridDict[x+10,y-20].stat = 1
		elif direction == 2:
			gridDict[x,y].stat = 1
			gridDict[x-10,y+10].stat = 1
			gridDict[x-20,y+10].stat = 1
			gridDict[x-20,y].stat = 1
			gridDict[x-20,y-10].stat = 1
		else:
			gridDict[x,y].stat = 1
			gridDict[x+10,y+10].stat = 1
			gridDict[x+10,y+20].stat = 1
			gridDict[x,y+20].stat = 1
			gridDict[x-10,y+20].stat = 1
	except KeyError:
		pass

# returns a random rgb() color tuple from a preset array
def random_color():
	colors = [(255,0,0),(255,0,255),(135,0,255),(0,0,255),(0,195,255),(0,255,0),(225,255,0),(255,155,0)]
	return colors[random.randint(0,7)]

def gun(gridDict):
	# far left four squares
	gridDict[390-300,200].stat = 1
	gridDict[400-300,200].stat = 1
	gridDict[390-300,210].stat = 1
	gridDict[400-300,210].stat = 1

	# middle left
	gridDict[470-300,210].stat = 1
	gridDict[470-300,220].stat = 1
	gridDict[480-300,220].stat = 1
	gridDict[480-300,200].stat = 1
	gridDict[490-300,200].stat = 1
	gridDict[490-300,210].stat = 1

	#middle-middle
	gridDict[550-300,220].stat = 1
	gridDict[550-300,230].stat = 1
	gridDict[550-300,240].stat = 1
	gridDict[560-300,220].stat = 1
	gridDict[570-300,230].stat = 1

	#middle-top
	gridDict[610-300,210-20].stat = 1
	gridDict[610-300,220-20].stat = 1
	gridDict[620-300,220-20].stat = 1
	gridDict[620-300,200-20].stat = 1
	gridDict[630-300,200-20].stat = 1
	gridDict[630-300,210-20].stat = 1

	#middle-bottom
	gridDict[630-300,210-20+110].stat = 1
	gridDict[630-300,220-20+110].stat = 1
	gridDict[640-300,210-20+110].stat = 1
	gridDict[650-300,210-20+110].stat = 1
	gridDict[640-300,210-20+130].stat = 1

	#right bottom
	gridDict[740-300,250].stat = 1
	gridDict[740-300,250+10].stat = 1
	gridDict[740-300,250+20].stat = 1
	gridDict[750-300,250].stat = 1
	gridDict[760-300,250+10].stat = 1

	#far right four squares
	gridDict[730-300,180].stat = 1
	gridDict[740-300,180].stat = 1
	gridDict[730-300,190].stat = 1
	gridDict[740-300,190].stat = 1

def button_tone():
	button = pygame.mixer.Sound('sound/button2.wav')
	pygame.mixer.Sound.play(button)

def user_select(gridDict, x, y):
	x = round_up_nearest_ten(x) - 10
	y = round_up_nearest_ten(y) - 10

	# if mouse pos != within banner add square
	# Banner Dimensions: (0, 470, 500, 30)
	if 500 > x > 0 and 470 > y > 0:
		button_tone()
		gridDict[x,y].stat = 1

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def start(display_surface, x, y, pos=(0,0), mstate=(0,0,0)):
	xanchor = int(x/2.)
	yanchor = int(y/2.)
	if xanchor-25+50 > pos[0] > xanchor-25 and y-25+20 > pos[1] > y-25:
		pygame.draw.rect(display_surface, b_green, (xanchor-25, y-25, 50, 20))
		if mstate[0]:
			run = True
			button_tone()
		else:
			run = False
	else:
		pygame.draw.rect(display_surface, green, (xanchor-25, y-25, 50, 20))
		run = False

	smallText = pygame.font.Font("freesansbold.ttf",12)
	textSurf, textRect = text_objects("START!", smallText)
	textRect.center = ( (xanchor-25+(50/2)), (y-25+(20/2)) )
	display_surface.blit(textSurf, textRect)

	return run


def stop(display_surface, x, y, pos=(0,0), mstate=(0,0,0)):
	xanchor = int(x/2.)
	yanchor = int(y/2.)
	if 225+50 > pos[0] > 225 and 475+20 > pos[1] > 475:
		pygame.draw.rect(display_surface, b_red, (225, 475, 50, 20))
		if mstate[0]:
			run = False
			button_tone()
		else:
			run = True
	else:
		pygame.draw.rect(display_surface, red, (225, 475, 50, 20))
		run = True

	smallText = pygame.font.Font("freesansbold.ttf",12)
	textSurf, textRect = text_objects("STOP!", smallText)
	textRect.center = ( (225+(50/2)), (475+(20/2)) )
	display_surface.blit(textSurf, textRect)


	return run
