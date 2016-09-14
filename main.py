import pygame, sys
from pygame.locals import *
# import numpy as np
import math
import random
import time
from functionality import create_glider, random_color, gun

# Define global variables
width = 500
height = 500
cellsize = 10
fps = 60.0
# Catch if width and height are valid for board
assert width % cellsize == 0
assert height % cellsize == 0

black = (0,  0,  0)
white = (255,255,255)
darkgrey = (40, 40, 40)
red = (220,20,60)

# use these to track current cells and updates
gridDict = {}
otherDict = {}

class cell:
	def __init__(self, loc, stat):
		self.loc = loc
		self.stat = stat

# draw an empty grid for our cells to live in
def drawGrid():
	for x in range(0, width, cellsize):
		pygame.draw.line(display_surface, darkgrey, (x,0),(x,height))
	for y in range(0, height, cellsize):
		pygame.draw.line(display_surface, darkgrey, (0,y),(width,y))
	return None

# fill gridDict will cells, randomly assign cell.stat values
def blanks(gridDict):

	for y in range(0, height, cellsize):
		for x in range (0, width, cellsize):
			# stat = 1 if random.randint(0,12) > 10 else 0
			stat = 0
			gridDict[x,y] = cell((x,y), stat)

	gun(gridDict)

	return gridDict


def check_neighbors(item, gridDict):
	'''
		alive - number of neighboring cells that are alive
		dead - 1: current cell is alive, 0: its dead
		newStat - value to assign to the new cell object
	'''
	alive = 0
	dead = 0
	newStat = 0

	# cycle through neigbors and increment alive and assign dead
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
	# implement rules for conway's game of life
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

# update cells for next round
def tick(gridDict, otherDict):
	for item in gridDict:
		otherDict[item] = check_neighbors(item, gridDict)

	copyDict = otherDict.copy()
	otherDict = {}
	gridDict = copyDict.copy()
	# redraw cells
	color(gridDict)
	return gridDict, otherDict

# draw the cells
def color(gridDict):
	to_col = gridDict
	for item in to_col:
		# draw live cells as a colored rect
		if to_col[item].stat == 1:
			pygame.draw.rect(display_surface, random_color(), (to_col[item].loc[0],to_col[item].loc[1],cellsize,cellsize))
		# draw dead cells as black rect
		elif to_col[item].stat ==0:
			pygame.draw.rect(display_surface, black, (to_col[item].loc[0],to_col[item].loc[1],cellsize,cellsize))

def main(gridDict, otherDict):
	pygame.init()

	global display_surface

	fpsclock = pygame.time.Clock()
	display_surface = pygame.display.set_mode((width,height))
	display_surface.fill(black)
	pygame.display.set_caption('Game of Life')

	blanks(gridDict)
	color(gridDict)
	drawGrid()

	pygame.display.update()
	# time.sleep(40)
	x = width
	y = height
	while True: #main game loop
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		mouse = pygame.mouse.get_pressed()
		pos = pygame.mouse.get_pos()
		if mouse[0]:
			create_glider(gridDict,pos[0],pos[1])
		gridDict, otherDict = tick(gridDict, otherDict)


		drawGrid()
		pygame.display.update()
		fpsclock.tick(fps)


if __name__ == '__main__':
	main(gridDict, otherDict)