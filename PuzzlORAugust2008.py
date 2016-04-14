# PuzzlOR August 2008 Markov Prison
# Markov’s Prison - 1,5,6,10,11,12,16, 0.4712  

import random
def generate_guard1(position,prison):
	val = round(random.random(),1)
	if val < 0.2:
		tempval =  0
	elif val < 0.6:
		tempval = 1
	elif val < 0.8:
		tempval = 2
	tempval = 3
	nextMoves = prison[position]
	nextMove = nextMoves[tempval]
	if nextMove == 0:
		nextMove = position
	return nextMove

def generate_guard2(position,prison):
	val = round(random.random(),1)
	if val < 0.4:
		tempval = 0
	elif val < 0.5:
		tempval = 1
	elif val < 0.7:
		tempval = 2
	tempval = 3
	nextMoves = prison[position]
	nextMove = nextMoves[tempval]
	if nextMove == 0:
		nextMove = position
	return nextMove

def generate_random(alist):
	randomval = random.randint(0,len(alist)-1)
	return randomval

def prisoner_move(position,prison):
	nextMoves = prison[position]
	newMove = nextMoves[generate_random(nextMoves)]
	if newMove == 0:
		newMove = position
	return newMove

def main():
	prison = {
	1:[0,5,0,2],
	2:[0,6,3,1],
	3:[0,7,4,2],
	4:[0,8,0,3],
	5:[1,9,6,0],
	6:[2,10,7,5],
	7:[3,11,8,6],
	8:[4,12,0,7],
	9:[5,13,10,0],
	10:[6,14,11,9],
	11:[7,15,12,10],
	12:[8,16,0,11],
	13:[9,0,14,0],
	14:[10,0,15,13],
	15:[11,0,16,14],
	16:[12,0,0,15],
	}

	prisonerPositionlist = []
	caught = False
	prisonerPosition = 1
	guard1Position = 16
	guard2Position = 16
	countval = 0

	while not caught:
		# check prisoner and guards position
		# check if prisoner is at position 16
		# move guards
		# move prisoner
	# 	prisonerPosition = prisoner_move(prisonerPosition)
	# 	guard1Position = generate_guard1(guard1Position,prison)
	# 	guard2Position = generate_guard2(guard2Position,prison)
	# 	#check if prisoner has been caught
	# 	if prisonerPosition == guard1Position or prisonerPosition == guard2Position:
	# 		caught = True
	# 		break
	# 	#check if prisoner is at position 16
	# 	elif prisonerPosition == 16:
	#  		prisonerPositionlist.append(prisonerPosition)
	#  		print("Escaped")
	#  		break
	#  	else:


	# 	elif nextPrisonerPosition not in prisonerPosition and nextPrisonerPosition != 0:
	# 		prisonerPosition.append(nextPrisonerPosition)
	# 		prisonerStartPosition = prisoner_move(nextPrisonerPosition)
	# print(prisonerPosition)	


#main

# Guard #1:
# 20% of the time he moves North
# 40% of the time he moves South
# 20% of the time he moves West
# 20% of the time he moves East
# Guard #2:
# 40% of the time she moves North
# 10% of the time she moves South
# 20% of the time she moves West
# 30% of the time she moves East
