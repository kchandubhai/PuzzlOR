# PuzzlOR April 2013 Subs and Battleship
import itertools
import random
import math
import operator

def generate_random(alist):
    return 

def generate_coordinate(value,alist):
    tempList = []
    tempList.extend([int(alist.index(value[0])) + 1,int(value[1])])
    return tempList

def euclidean_distance(a,b):
    c = [math.pow(a[i] - b[i],2) for i in range(len(b))]
    return round(math.sqrt(sum(c)),2)

def update_battleship(alist,blist):
    if len(blist) < 1:
        return alist
    else:
        templist = [value for value in alist if value not in blist]    
        return templist

def assign_sub(value,alist,blist):
    calcList = [[euclidean_distance(generate_coordinate(val,blist),generate_coordinate(value,blist)),val] for val in alist]   
    sorted_calcList = sorted(calcList,key=operator.itemgetter(1))
    return sorted_calcList[0]

def main():
    xVal = ["A","B","C","D","E","F","G","H","I","J"]
    #subs = ["A1","B2","D2","D3","B6","D7","F10","G1","G4","I1","I5","I7","J2","J3","J6"]
    subs = ["A1","B2","B6","D2","D3","D7","F10","G1","G4","I1","I5","I7","J2","J3","J6"]
    
    battleships = ["B1","C4","D9","F1","F2","F3","F5","F8",
                   "G5","G6","G8","H7","J1","J4","J10"]


    tempBattleShips = battleships
    assignedSub = []
    distance_calc = 0
    for sub in subs:
        tempBattleShips = update_battleship(tempBattleShips,assignedSub)
        temp = assign_sub(sub,tempBattleShips,xVal)
        assignedSub.append(temp[1])
        distance_calc += temp[0]
    print(distance_calc)

   
main()
