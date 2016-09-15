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

# returns a random rgb() color tuple from a preset array
def random_color():
	colors = [(255,0,0),(255,0,255),(135,0,255),(0,0,255),(0,195,255),(0,255,0),(225,255,0),(255,155,0)]
	return colors[random.randint(0,7)]

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
	if (xanchor-60+50) > pos[0] > (xanchor-60) and (y-25+20) > pos[1] > y-25:
		pygame.draw.rect(display_surface, b_red, (xanchor-60, y-25, 50, 20))
		if mstate[0]:
			run = False
			button_tone()
		else:
			run = True
	else:
		pygame.draw.rect(display_surface, red, (xanchor-60, y-25, 50, 20))
		run = True

	smallText = pygame.font.Font("freesansbold.ttf",12)
	textSurf, textRect = text_objects("STOP!", smallText)
	textRect.center = ( (xanchor-60+(50/2)), (y-25+(20/2)) )
	display_surface.blit(textSurf, textRect)

	return run

def reset(display_surface, x, y, pos=(0,0), mstate=(0,0,0)):
	xanchor = int(x/2.)
	yanchor = int(y/2.)
	if (xanchor+10+50) > pos[0] > (xanchor+10) and (y-25+20) > pos[1] > y-25:
		pygame.draw.rect(display_surface, b_red, (xanchor+10, y-25, 50, 20))
		if mstate[0]:
			# run = False
			button_tone()
		else:
			# run = True
			pass
	else:
		pygame.draw.rect(display_surface, red, (xanchor+10, y-25, 50, 20))
		# run = True

	smallText = pygame.font.Font("freesansbold.ttf",12)
	textSurf, textRect = text_objects("RESET", smallText)
	textRect.center = ( (xanchor+10+(50/2)), (y-25+(20/2)) )
	display_surface.blit(textSurf, textRect)

	return None

def reset_options(display_surface, x, y, pos=(0,0), mstate=(0,0,0)):
	pass











