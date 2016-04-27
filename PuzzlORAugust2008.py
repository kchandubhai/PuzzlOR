# PuzzlOR August 2008 Markov Prison
#  0.4712

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
	return random.randint(0,len(alist)-1)
	
def prisoner_move(position,prison):
	nextMoves = prison[position]
	newMove = nextMoves[generate_random(nextMoves)]
	if newMove == 0:
		newMove = position
	return newMove

def guard_move(position,prison,guardData):
    weighted_choices = guardData
    population = [val for val, cnt in weighted_choices for i in range(cnt)]
    output = random.choice(population)
    if output == "North":
        tempval = 0
    elif output == "South":
        tempval = 1
    elif output == "East":
        tempval = 2
    else:
        tempval = 3
    nextMoves = prison[position]
    nextMove = nextMoves[tempval]
    if nextMove == 0:
        nextMove = position
    return nextMove


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

guardData1 = [("North",20),("South",40),("East",20),("West",20)]
guardData2 = [("North",40),("South",10),("East",20),("West",30)]


countval = 0
maxcountval = 10001
outcomeList = []

while countval < maxcountval:

    prisonerPositionlist = []
    caught = False
    prisonerPosition = 1
    guard1Position = 16
    guard2Position = 16

    while not caught:
        if prisonerPosition == guard1Position or prisonerPosition == guard2Position:
            outcomeList.append(["caught",prisonerPositionlist])
            caught = True
            break
        elif prisonerPosition == 16:
            outcomeList.append(["escaped",prisonerPositionlist])
            break
        else:
            prisonerPosition = prisoner_move(prisonerPosition,prison)
            guard1Position = guard_move(guard1Position,prison,guardData1)
            guard2Position = guard_move(guard2Position,prison,guardData2)
            prisonerPositionlist.append(prisonerPosition)
    countval +=1

escapeRoute = []
caughtCount = 0
for value in outcomeList:
    if value[0] == "escaped":
        escapeRoute.append(value[1])
    elif value[0] == "caught":
        caughtCount += 1
#print(escapeRoute)
print(caughtCount/len(outcomeList))
