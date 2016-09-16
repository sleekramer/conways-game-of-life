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

def render_textrect(string, font, rect, text_color, background_color, justification=0):
    """Returns a surface containing the passed text string, reformatted
    to fit within the given rect, word-wrapping as necessary. The text
    will be anti-aliased.

    Takes the following arguments:

    string - the text you wish to render. \n begins a new line.
    font - a Font object
    rect - a rectstyle giving the size of the surface requested.
    text_color - a three-byte tuple of the rgb value of the
                 text color. ex (0, 0, 0) = BLACK
    background_color - a three-byte tuple of the rgb value of the surface.
    justification - 0 (default) left-justified
                    1 horizontally centered
                    2 right-justified

    Returns the following values:

    Success - a surface object with the text rendered onto it.
    Failure - raises a TextRectException if the text won't fit onto the surface.
    """

    import pygame

    final_lines = []

    requested_lines = string.splitlines()

    # Create a series of lines that will fit on the provided
    # rectangle.

    for requested_line in requested_lines:
        if font.size(requested_line)[0] > rect.width:
            words = requested_line.split(' ')
            # if any of our words are too long to fit, return.
            for word in words:
                if font.size(word)[0] >= rect.width:
                    raise TextRectException, "The word " + word + " is too long to fit in the rect passed."
            # Start a new line
            accumulated_line = ""
            for word in words:
                test_line = accumulated_line + word + " "
                # Build the line while the words fit.
                if font.size(test_line)[0] < rect.width:
                    accumulated_line = test_line
                else:
                    final_lines.append(accumulated_line)
                    accumulated_line = word + " "
            final_lines.append(accumulated_line)
        else:
            final_lines.append(requested_line)

    # Let's try to write the text out on the surface.

    surface = pygame.Surface(rect.size)
    surface.fill(background_color)

    accumulated_height = 0
    for line in final_lines:
        if accumulated_height + font.size(line)[1] >= rect.height:
            raise TextRectException, "Once word-wrapped, the text string was too tall to fit in the rect."
        if line != "":
            tempsurface = font.render(line, 1, text_color)
            if justification == 0:
                surface.blit(tempsurface, (0, accumulated_height))
            elif justification == 1:
                surface.blit(tempsurface, ((rect.width - tempsurface.get_width()) / 2, accumulated_height))
            elif justification == 2:
                surface.blit(tempsurface, (rect.width - tempsurface.get_width(), accumulated_height))
            else:
                raise TextRectException, "Invalid justification argument: " + str(justification)
        accumulated_height += font.size(line)[1]

    return surface

def round_up_nearest_ten(n):
	return int(math.ceil(n / 10.0)) * 10

# returns a random rgb() color tuple from a preset array
def random_color():
	colors = [(255,0,0),(255,0,255),(135,0,255),(0,0,255),(0,195,255),(0,255,0),(225,255,0),(255,155,0)]
	return colors[random.randint(0,7)]

def button_tone():
	button = pygame.mixer.Sound('sound/button2.wav')
	pygame.mixer.Sound.play(button)


def user_select(gridDict, x, y, w, h, click_option):
	x = round_up_nearest_ten(x) - 10
	y = round_up_nearest_ten(y) - 10

	# if mouse pos != within banner add square
	# Banner Dimensions: (0, 470, 500, 30)
	if w > x > w-w and h-30 > y > h-h:
		button_tone()
		if gridDict[x,y].stat == 1:
			gridDict[x,y].stat = 0
		else:
			# print "Creating %s at [%s,%s]" % (Conway_Shape(click_option).name, x, y)
			click_handler(gridDict, x, y, click_option)



def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def draw_text(display_surface, text, center, size):
	smallText = pygame.font.Font("freesansbold.ttf", size)
	textSurf, textRect = text_objects(text, smallText)
	textRect.center = center
	display_surface.blit(textSurf, textRect)

def start(display_surface, x, y, pos=(0,0), mstate=(0,0,0)):
	xanchor = int(x/2.) - 25
	yanchor = y - 25
	w, h = 50, 20 # width and height of button
	if xanchor+w > pos[0] > xanchor and yanchor+h > pos[1] > yanchor:
		pygame.draw.rect(display_surface, b_green, (xanchor, yanchor, w, h))
		if mstate[0]:
			run = True
			button_tone()
		else:
			run = False
	else:
		pygame.draw.rect(display_surface, green, (xanchor, yanchor, w, h))
		run = False
	draw_text(display_surface, "START!", ((xanchor+(w/2)),(yanchor+(h/2))), 12)

	return run


def stop(display_surface, x, y, pos=(0,0), mstate=(0,0,0)):
	xanchor = int(x/2.) - 60
	yanchor = y-25
	w, h = 50, 20 # width and height of button
	if (xanchor+w) > pos[0] > (xanchor) and (yanchor+h) > pos[1] > yanchor:
		pygame.draw.rect(display_surface, b_red, (xanchor, yanchor, w, h))
		if mstate[0]:
			run = False
			button_tone()
		else:
			run = True
	else:
		pygame.draw.rect(display_surface, red, (xanchor, yanchor, w, h))
		run = True
	draw_text(display_surface, "STOP!", ((xanchor+(w/2)),(yanchor+(h/2))), 12)

	return run

def reset(display_surface, x, y, run, pos=(0,0), mstate=(0,0,0)):
	xanchor = int(x/2.) + 10
	yanchor = y - 25
	w, h = 50, 20 # width and height of button
	if (xanchor+w) > pos[0] > (xanchor) and (yanchor+h) > pos[1] > yanchor:
		pygame.draw.rect(display_surface, b_red, (xanchor, yanchor, w, h))
		if mstate[0]:
			res_menu = True
			run = False
			button_tone()
		else:
			res_menu = False
			pass
	else:
		pygame.draw.rect(display_surface, red, (xanchor, yanchor, w, h))
		res_menu = False

	draw_text(display_surface, "RESET", ((xanchor+(w/2)),(yanchor+(h/2))), 12)

	return run, res_menu

def info_button(display_surface, x, y, run, pos=(0,0), mstate=(0,0,0)):
	r = 10 # radius
	xanchor = 20
	yanchor = y-25+r

	pygame.draw.circle(display_surface, black, (xanchor, (yanchor)), r, 2)
	draw_text(display_surface, "i", (xanchor,(yanchor+2)), 15)

	# if 30 > pos[0] > 10 and y-5 > pos[1] > y-22:
	# 	if mstate[0]:
	# 		show_i = True
	# 		run = False
	# 	else:
	# 		show_i = False
	# else:
	# 	show_i = False
	show_i = ((30 > pos[0] > 10 and y-5 > pos[1] > y-22) and mstate[0])
	if show_i:
		run = False
	return run, show_i

def info(display_surface, x, y, pos=(0,0), mstate=(0,0,0)):
	pygame.draw.rect(display_surface, white, (0, 0, x, y))

	draw_text(display_surface, "Back", (24,10), 18)

	text_info = """John Conway's Cellular Automaton"""
	text_info2 = """\n\nRules:\n\nEach Cell with one or no neighbors dies.\nEach cell with 4 or more neighbors dies.\nEach cell with two or three neighbors survives.\nEach empty cell with three neighbors becomes populated.\n\nControls:\n\nClick to populate/depopulate a cell.\nClick start to begin model.\nClick stop to end model.\nClick reset to clear or choose preset simulations.\n\nCreated by:\n\nRyan Oliver Schenck & Steven Lee-Kramer\n\ngithub.com/rschenck/game_of_life.git"""

	# Headers
	smallText = pygame.font.Font(None,26)
	back_rect = pygame.Rect((x-x, y-y+60, x, y-50))
	rendered_text = render_textrect(text_info, smallText, back_rect, black, white, 1)
	display_surface.blit(rendered_text, back_rect)

	# Other Text
	smallText = pygame.font.Font(None,22)
	back_rect = pygame.Rect((x-x, y-y+80, x, y-50))
	rendered_text = render_textrect(text_info2, smallText, back_rect, black, white, 1)
	display_surface.blit(rendered_text, back_rect)


	# print str((pos[0],pos[1]))
	# if 40 > pos[0] > 0 and 18 > pos[1] > 0:
	# 	if mstate[0]:
	# 		show_i = False
	# 	else:
	# 		show_i = True
	# else:
	# 	show_i = True
	# return show_i
	show_i = not (mstate[0] and (40 > pos[0] > 0 and 18 > pos[1] > 0))
	return show_i


def reset_options(display_surface, x, y, pos=(0,0), mstate=(0,0,0)):
	xanchor = int(x/2.)
	yanchor = int(y/2.)
	top = yanchor-130
	s = 30
	# draw the reset menu in the middle of the display_surface
	pygame.draw.rect(display_surface, white, (xanchor-(yanchor/2.), top, yanchor, 260))
	# set labels
	labels = ["Blank", "Gun", "Ten", "Binary", "Face", "Maze", "Pulsar", "Gliders", "Random"]
	# draw the labels
	for i, item in enumerate(labels):
		draw_text(display_surface, item, ((xanchor),(top+10+s*i)), 18)

	option = ''
	if mstate[0]:
		for x, entry in enumerate(labels):
			if xanchor+30 > pos[0] > xanchor-30 and top+s*(x+1) > pos[1] > top+s*(x):
				option = entry
	return option


def click_creator(display_surface, x, y, click_option, pos=(0,0), mstate=(0,0,0)):
	xanchor = x - 55
	yanchor = y - 25
	w, h = 50, 20 # width and height of button
	if (xanchor+w) > pos[0] > (xanchor) and (yanchor+h) > pos[1] > yanchor:
		pygame.draw.rect(display_surface, (200,200,200), (xanchor, yanchor, w, h))
		if mstate[0]:
			click_option = (click_option + 1) % (Conway_Shape(1).max() + 1) or 1
	else:
		pygame.draw.rect(display_surface, (150,150,150), (xanchor, yanchor, w, h))

	draw_text(display_surface, Conway_Shape(click_option).name,((xanchor+(w/2)),(yanchor+(h/2))),12)


	return click_option
