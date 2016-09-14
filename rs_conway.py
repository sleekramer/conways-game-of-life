import pygame, sys
from pygame.locals import *
import numpy as np

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

gridDict = {}

class cell:
	def __init__(self, loc, stat):
		self.loc = loc
		self.stat = stat

def drawGrid():
	for x in range(0, width, cellsize):
		pygame.draw.line(display_surface, darkgrey, (x,0),(x,height))
	for y in range(0, height, cellsize):
		pygame.draw.line(display_surface, darkgrey, (0,y),(width,y))
	return None

def blanks():
	for y in range(0, height, cellsize):
		for x in range (0, width, cellsize):
				gridDict[x,y] = cell((x,y), 1)
	return gridDict

def check_neighbors(item):
	alive = 0
	dead = 0
	newStat = 0

	# passes x,y of the cell looked up from blanks and returns 0 or 1
	for x in [10, -10, 0]:
		for y in [10, -10, 0]:
			if x != 0 and y != 0:
				alive += gridDict[(item[0]+x,item[1]+y)].stat
			else:
				dead += gridDict[(item[0]+x,item[1]+y)].stat

	if dead == 1:
		if alive < 2 or alive > 3:
			newStat = 0
		else:
			newStat = 1
	elif dead == 0:
		if alive == 3:
			newStat = 1
		else:
			pass

	return cell(item, newStat)

# cycles through
def tick():
	newDraw = {}
	for item in gridDict:
		newDraw[item] = check_neighbors(item)
	gridDict = newDraw
	color()

def color():
	to_col = gridDict
	for item in to_col:
		if to_col[item].stat == 1:
			pygame.draw.rect(display_surface, white, (to_col[item].loc[0],to_col[item].loc[1],cellsize,cellsize))

def main():
	pygame.init()

	global display_surface

	display_surface = pygame.display.set_mode((width,height)) 
	display_surface.fill(black)
	pygame.display.set_caption('Game of Life') 

	blanks()
	color()
	# for item in gridDict:
	# 	print(item)
	# 	print(gridDict[item])
	# 	sys.exit()

	drawGrid()
	while True: #main game loop
		for event in pygame.event.get():
			print(gridDict[0,0])
			tick()
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		
		pygame.display.update()


if __name__ == '__main__':
	main()