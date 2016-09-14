import pygame, sys
from pygame.locals import *
import numpy as np
import random

# Define global variables
width = 1200
height = 600
cellsize = 10
fps = 1.0

# Catch if width and height are valid for board
assert width % cellsize == 0
assert height % cellsize == 0

black = (0,  0,  0)
white = (255,255,255)
darkgrey = (40, 40, 40)
red = (220,20,60)

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

def blanks(gridDict):
	for y in range(0, height, cellsize):
		for x in range (0, width, cellsize):
				gridDict[x,y] = cell((x,y), random.randint(0,1))
	return gridDict

def check_neighbors(item, gridDict):
	alive = 0
	dead = 0
	newStat = 0

	# passes x,y of the cell looked up from blanks and returns 0 or 1
	for x in [10, -10, 0]:
		for y in [10, -10, 0]:
			if (x,y) != (0,0):
					try: 
						alive += gridDict[(item[0]+x,item[1]+y)].stat
					except KeyError: 
						pass
			else:
				try: 
					dead += gridDict[(item[0]+x,item[1]+y)].stat
				except KeyError: 
					pass

	# print('%s %s') % (alive, dead)
	if dead == 1:
		# print("ALIVE")
		if alive < 2 or alive > 3:
			newStat = 0
		else:
			newStat = 1
	elif dead == 0:
		# print("DEAD")
		if alive == 3:
			newStat = 1
		else:
			pass

	return cell(item, newStat)

# cycles through
def tick(gridDict):
	newDraw = {}
	for item in gridDict:
		newDraw[item] = check_neighbors(item, gridDict)
	gridDict = newDraw.copy()
	count = 0
	for item in gridDict:
		count += gridDict[item].stat
	print count

	color(newDraw)

def color(gridDict):
	to_col = gridDict
	for item in to_col:
		if to_col[item].stat == 1:
			pygame.draw.rect(display_surface, white, (to_col[item].loc[0],to_col[item].loc[1],cellsize,cellsize))
		elif to_col[item].stat ==0:
			pygame.draw.rect(display_surface, black, (to_col[item].loc[0],to_col[item].loc[1],cellsize,cellsize))


def main():
	pygame.init()

	global display_surface

	fpsclock = pygame.time.Clock()
	display_surface = pygame.display.set_mode((width,height)) 
	display_surface.fill(black)
	pygame.display.set_caption('Game of Life') 

	blanks(gridDict)
	color(gridDict)
	# for item in gridDict:
	# 	print(item)
	# 	print(gridDict[item])
	# 	sys.exit()

	drawGrid()

	pygame.display.update()
	x = width
	y = height
	while True: #main game loop
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		tick(gridDict)
		# try:
		pygame.draw.rect(display_surface, red, (x,y,cellsize,cellsize))
		# except:
		# 	pass
		x -= 10
		y -= 10
		pygame.display.update()
		fpsclock.tick(fps)


if __name__ == '__main__':
	main()