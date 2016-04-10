# PuzzlOR April 2013 Subs and Battleship
import itertools
import random
import math
import operator

def generate_coordinate(value,alist):
    tempList = []
    tempVal = value[0]
    tempNum = int(value[1])
    tempVal1 = int(alist.index(tempVal)) + 1
    tempList.extend([tempVal1,tempNum])
    return tempList

def euclidean_distance(a,b):
    c = [math.pow(a[i] - b[i],2) for i in range(len(b))]
    return round(math.sqrt(sum(c)),2)

def update_battleship(alist,blist):
    if len(blist) < 1:
        return alist
    else:
        for value in alist:
            if value in blist:
                alist.remove(value)
        return alist

def assign_sub(value,alist,blist):
    calcList = []
    for val in alist:
        calcList.append([euclidean_distance(generate_coordinate(val,blist),generate_coordinate(value,blist)),val])
    sorted_calcList = sorted(calcList,key=operator.itemgetter(1))
    return sorted_calcList[0]

def main():
    xVal = ["A","B","C","D","E","F","G","H","I","J"]
    subs = ["A1","B2","D2","D3","B6","D7","F10","G1","G4","I1",
            "I5","I7","J2","J3","J6"]
    battleships = ["B1","C4","D9","F1","F2","F3","F5","F8",
                   "G5","G6","G8","H7","J1","J4","J10"]

    calc_distance = []
    for ship in itertools.permutations(battleships):
        tempBattleShips = list(ship)
        assignedSub = []
        distance_calc = 0
        for sub in subs:
          tempBattleShips = update_battleship(tempBattleShips,assignedSub)
          temp = assign_sub(sub,tempBattleShips,xVal)
          assignedSub.append(temp[1])
          distance_calc += temp[0]
        calc_distance.append(distance_calc)
    calc_distance.sort()
    print(calc_distance)
    print(calc_distance[0])
   
main()
