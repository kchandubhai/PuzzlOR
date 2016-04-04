# PuzzlOR August 2008 Markov Prison

import random
def generate_guard1():
	val = round(random.random(),1)
	if val < 0.2:
		return 0
	elif val < 0.6:
		return 1
	elif val < 0.8:
		return 2
	return 3

def generate_guard2():
	val = round(random.random(),1)
	if val < 0.4:
		return 0
	elif val < 0.5:
		return 1
	elif val < 0.7:
		return 2
	return 3

def generate_random(alist):
	randomval = random.randint(0,len(alist)-1)
	return randomval

def prisoner_move(position,prison):
	nextMoves = prison[position]
	newMove = nextMoves[generate_random(nextMoves)]
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

	prisonerPosition = []
	caught = False
	prisonerStartPosition = 1
	guard1Position = 16
	guard2Position = 16

	while not caught:
		nextPrisonerPosition = prisoner_move(prisonerStartPosition)
		if nextPrisonerPosition == 16:
			prisonerPosition.append(nextPrisonerPosition)
			print("Escaped")
			break
		elif nextPrisonerPosition not in prisonerPosition and nextPrisonerPosition != 0:
			prisonerPosition.append(nextPrisonerPosition)
			prisonerStartPosition = prisoner_move(nextPrisonerPosition)
	print(prisonerPosition)	


#main
print(generate_guard1())