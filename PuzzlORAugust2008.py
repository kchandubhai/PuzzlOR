# PuzzlOR August 2008 Markov Prison

import random

def generate_random(alist):
	return random.randint(0,len(alist)-1)

def prisoner_move(position,prison):
    tempList = prison[position]
    tempValue = generate_random(tempList)
    ##if tempList[tempValue] == 0:
    ##    return position
    return tempList[tempValue]

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
    16:[12,0,0,15]
    }
    
    prisonRoute = {
    1:[5,2],
    2:[6,3,1],
    3:[7,4,2],
    4:[8,3],
    5:[1,9,6],
    6:[2,10,7,5],
    7:[3,11,8,6],
    8:[4,12,7],
    9:[5,13,10],
    10:[6,14,11,9],
    11:[7,15,12,10],
    12:[8,16,11],
    13:[9,14],
    14:[10,15,13],
    15:[11,16,14],
    16:[12,15]
    }
    
    guardData1 = [("North",2),("South",4),("East",2),("West",2)]
    guardData2 = [("North",4),("South",1),("East",2),("West",3)]
    
    countval = 0
    maxcountval = 10
    outcomeList = []
    escapeRoute = []
    while countval < maxcountval:
        prisonerPositionlist = []
        guard1PositionList = []
        guard2PositionList = []
        chaseEnd = False
        prisonerPosition = 1
        guard1Position = 16
        guard2Position = 16
        while not chaseEnd:
            if prisonerPosition == guard1Position or prisonerPosition == guard2Position:
                outcomeList.append("caught")
                chaseEnd = True
                break
            elif prisonerPosition == 16:
                prisonerPositionlist.append(16)
                escapeRoute.append(prisonerPositionlist)
                outcomeList.append("escaped")
                chaseEnd = True
                break
            else:
                if prisonerPosition not in prisonerPositionlist:
                    prisonerPositionlist.append(prisonerPosition)
                    prisonerPosition = prisoner_move(prisonerPosition,prisonRoute)
                if guard1Position not in guard1PositionList:
                    guard1Position = guard_move(guard1Position,prison,guardData1)
                if guard2Position not in guard2PositionList:
                    guard2Position = guard_move(guard2Position,prison,guardData2)
        countval +=1
    print(len([value for value in outcomeList if value == "caught"]))
    print(len([value for value in outcomeList if value == "escaped"]))
    print(escapeRoute[0:5])



if __name__ == "__main__":
    main()













