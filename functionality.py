import math
import random

def round_up_nearest_ten(n):
	return int(math.ceil(n / 10.0)) * 10

# create a conway glider
def create_glider(gridDict, x, y):
	x = round_up_nearest_ten(x)
	y = round_up_nearest_ten(y)

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

# returns a random rgb() color tuple from a preset array
def random_color():
	colors = [(255,0,0),(255,0,255),(135,0,255),(0,0,255),(0,195,255),(0,255,0),(225,255,0),(255,155,0)]
	return colors[random.randint(0,7)]

def gun(gridDict):
	# far left four squares
	gridDict[390,200].stat = 1
	gridDict[400,200].stat = 1
	gridDict[390,210].stat = 1
	gridDict[400,210].stat = 1

	# middle left
	gridDict[470,210].stat = 1
	gridDict[470,220].stat = 1
	gridDict[480,220].stat = 1
	gridDict[480,200].stat = 1
	gridDict[490,200].stat = 1
	gridDict[490,210].stat = 1

	#middle-middle
	gridDict[550,220].stat = 1
	gridDict[550,230].stat = 1
	gridDict[550,240].stat = 1
	gridDict[560,220].stat = 1
	gridDict[570,230].stat = 1

	#middle-top
	gridDict[610,210-20].stat = 1
	gridDict[610,220-20].stat = 1
	gridDict[620,220-20].stat = 1
	gridDict[620,200-20].stat = 1
	gridDict[630,200-20].stat = 1
	gridDict[630,210-20].stat = 1

	#middle-bottom
	gridDict[630,210-20+110].stat = 1
	gridDict[630,220-20+110].stat = 1
	gridDict[640,210-20+110].stat = 1
	gridDict[650,210-20+110].stat = 1
	gridDict[640,210-20+130].stat = 1

	#right bottom
	gridDict[740,250].stat = 1
	gridDict[740,250+10].stat = 1
	gridDict[740,250+20].stat = 1
	gridDict[750,250].stat = 1
	gridDict[760,250+10].stat = 1

	#far right four squares
	gridDict[730,180].stat = 1
	gridDict[740,180].stat = 1
	gridDict[730,190].stat = 1
	gridDict[740,190].stat = 1




