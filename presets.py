import random

def blank(gridDict):
	for item in gridDict:
		gridDict[item].stat = 0

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

def tens(gridDict):
	for i in range(0,100, 10):
		gridDict[200+i,240].stat = 1

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