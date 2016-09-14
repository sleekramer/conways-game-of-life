import pygame, sys
from pygame.locals import *

# Define global variables
width = 1200
height = 600
cellsize = 10

# Catch if width and height are valid for board
assert width % cellsize == 0
assert height % cellsize == 0

black = (0,  0,  0)
white = (255,255,255)
darkgrey = (40, 40, 40)

def drawGrid():
	for x in range(0, width, cellsize):
		pygame.draw.line(display_surface, darkgrey, (x,0),(x,height))
	for y in range(0, height, cellsize):
		pygame.draw.line(display_surface, darkgrey, (0,y),(width,y))
	return None


def main():
	pygame.init()

	global display_surface

	display_surface = pygame.display.set_mode((width,height)) 
	display_surface.fill(black)
	pygame.display.set_caption('Game of Life') 

	while True: #main game loop
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		drawGrid()
		pygame.display.update()


if __name__ == '__main__':
	main()