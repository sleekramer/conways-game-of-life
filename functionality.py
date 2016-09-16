import math
import random
import pygame
from conway_shapes import click_handler, Conway_Shape
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

def user_select(gridDict, x, y, click_option):
	x = round_up_nearest_ten(x) - 10
	y = round_up_nearest_ten(y) - 10

	# if mouse pos != within banner add square
	# Banner Dimensions: (0, 470, 500, 30)
	if 500 > x > 0 and 470 > y > 0:
		button_tone()
		if gridDict[x,y].stat == 1:
			gridDict[x,y].stat = 0
		else:
			print "Creating %s at [%s,%s]" % (Conway_Shape(click_option).name, x, y)
			click_handler(gridDict, x, y, click_option)

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

def reset(display_surface, x, y, run, pos=(0,0), mstate=(0,0,0)):
	xanchor = int(x/2.)
	yanchor = int(y/2.)
	if (xanchor+10+50) > pos[0] > (xanchor+10) and (y-25+20) > pos[1] > y-25:
		pygame.draw.rect(display_surface, b_red, (xanchor+10, y-25, 50, 20))
		if mstate[0]:
			res_menu = True
			run = False
			button_tone()
		else:
			res_menu = False
			pass
	else:
		pygame.draw.rect(display_surface, red, (xanchor+10, y-25, 50, 20))
		res_menu = False

	smallText = pygame.font.Font("freesansbold.ttf",12)
	textSurf, textRect = text_objects("RESET", smallText)
	textRect.center = ( (xanchor+10+(50/2)), (y-25+(20/2)) )
	display_surface.blit(textSurf, textRect)

	return run, res_menu

def reset_options(display_surface, x, y, pos=(0,0), mstate=(0,0,0)):
	xanchor = int(x/2.)
	yanchor = int(y/2.)

	pygame.draw.rect(display_surface, white, (xanchor-(yanchor/2.), 0-(y/4.0)+200, yanchor, 230))
	smallText = pygame.font.Font("freesansbold.ttf",18)
	textSurf, textRect = text_objects("Blank", smallText)
	textRect.center = ( (xanchor), (0-(y/4.0)+210) )
	display_surface.blit(textSurf, textRect)

	textSurf, textRect = text_objects("Gun", smallText)
	textRect.center = ( (xanchor), (0-(y/4.0)+240) )
	display_surface.blit(textSurf, textRect)

	textSurf, textRect = text_objects("Ten", smallText)
	textRect.center = ( (xanchor), (0-(y/4.0)+270) )
	display_surface.blit(textSurf, textRect)

	textSurf, textRect = text_objects("Binary", smallText)
	textRect.center = ( (xanchor), (0-(y/4.0)+300) )
	display_surface.blit(textSurf, textRect)

	textSurf, textRect = text_objects("Face", smallText)
	textRect.center = ( (xanchor), (0-(y/4.0)+330) )
	display_surface.blit(textSurf, textRect)

	textSurf, textRect = text_objects("Maze", smallText)
	textRect.center = ( (xanchor), (0-(y/4.0)+360) )
	display_surface.blit(textSurf, textRect)

	textSurf, textRect = text_objects("Pulsar", smallText)
	textRect.center = ( (xanchor), (0-(y/4.0)+390) )
	display_surface.blit(textSurf, textRect)

	textSurf, textRect = text_objects("Gliders", smallText)
	textRect.center = ( (xanchor), (0-(y/4.0)+420) )
	display_surface.blit(textSurf, textRect)

	# print str((pos[0],pos[1]))
	# clear
	if xanchor+30 > pos[0] > xanchor-30 and 94 > pos[1] > 74:
		if mstate[0]:
			option = 'Blank'
		else:
			option = ''
	elif xanchor+30 > pos[0] > xanchor-30 and 122 > pos[1] > 102:
		# print str((pos[0],pos[1]))
		if mstate[0]:
			option = 'Gun'
		else:
			option = ''
	elif xanchor+30 > pos[0] > xanchor-30 and 151 > pos[1] > 135:
		# print str((pos[0],pos[1]))
		if mstate[0]:
			option = 'Ten'
		else:
			option = ''
	elif xanchor+30 > pos[0] > xanchor-30 and 186 > pos[1] > 164:
		# print str((pos[0],pos[1]))
		if mstate[0]:
			option = 'Binary'
		else:
			option = ''
	elif xanchor+30 > pos[0] > xanchor-30 and 215 > pos[1] > 195:
		# print str((pos[0],pos[1]))
		if mstate[0]:
			option = 'Face'
		else:
			option = ''
	elif xanchor+30 > pos[0] > xanchor-30 and 243 > pos[1] > 225:
		# print str((pos[0],pos[1]))
		if mstate[0]:
			option = 'Maze'
		else:
			option = ''
	elif xanchor+30 > pos[0] > xanchor-30 and 275 > pos[1] > 255:
		# print str((pos[0],pos[1]))
		if mstate[0]:
			option = 'Pulsar'
		else:
			option = ''
	elif xanchor+30 > pos[0] > xanchor-30 and 305 > pos[1] > 285:
		# print str((pos[0],pos[1]))
		if mstate[0]:
			option = 'Gliders'
		else:
			option = ''
	else:
		option = ''

	return option

def click_creator(display_surface, x, y, click_option, pos=(0,0), mstate=(0,0,0), ):
	xanchor = int(x/2.)
	if (xanchor-230+50) > pos[0] > (xanchor-230) and (y-25+20) > pos[1] > y-25:
		pygame.draw.rect(display_surface, (200,200,200), (xanchor-230, y-25, 50, 20))
		if mstate[0]:
			click_option = (click_option + 1) % (Conway_Shape(1).max() + 1) or 1
		else:
			pass
	else:
		pygame.draw.rect(display_surface, (150,150,150), (xanchor-230, y-25, 50, 20))


	smallText = pygame.font.Font("freesansbold.ttf",12)
	textSurf, textRect = text_objects(Conway_Shape(click_option).name, smallText)
	textRect.center = ( (xanchor-230+(50/2)), (y-25+(20/2)) )
	display_surface.blit(textSurf, textRect)

	return click_option
