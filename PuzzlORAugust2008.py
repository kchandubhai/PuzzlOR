# PuzzlOR August 2008 Markov Prison
import random

def generate_random(alist):
	return random.randint(0,len(alist)-1)

def prisoner_move(position,prison):
    nextMoves = prison[position]
    newMove = nextMoves[generate_random(nextMoves)]
    if newMove == 0:
        return position
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

guardData1 = [("North",2),("South",4),("East",2),("West",2)]
guardData2 = [("North",4),("South",1),("East",2),("West",3)]

countval = 0
maxcountval = 10
outcomeList = []

while countval < maxcountval:

    prisonerPositionlist = []
    caught = False
    prisonerPosition = 1
    guard1Position = 16
    guard2Position = 16

    while not caught:
        if prisonerPosition == guard1Position or prisonerPosition == guard2Position:
            outcomeList.append(["caught"])
            caught = True
        elif prisonerPosition == 16:
            prisonerPositionlist.append(16)
            outcomeList.append(["escaped",prisonerPositionlist])
            caught = True
        else:
            if prisonerPosition not in prisonerPositionlist:
                prisonerPositionlist.append(prisonerPosition)
            prisonerPosition = prisoner_move(prisonerPosition,prison)
            guard1Position = guard_move(guard1Position,prison,guardData1)
            guard2Position = guard_move(guard2Position,prison,guardData2)
    countval +=1

escapeRoute = []
caughtCount = 0
for value in outcomeList:
    if value[0] == "escaped":
        escapeRoute.append(value[1])
    elif value[0] == "caught":
        caughtCount += 1
print(escapeRoute)
print(caughtCount/len(outcomeList))
