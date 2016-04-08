# PuzzlOR April 2013 Subs and Battleship
# Subs vs. Battleships - 30.78

import itertools
import random
import math
import operator

def create_coordinate(alist,xval):
    coor = [generate_coordinate(value,xval) for value in alist]
    return coor

def generate_coordinate(value,alist):
    tempList = []
    tempVal = value[0]
    tempNum = int(value[1])
    tempVal1 = int(alist.index(tempVal)) + 1
    tempList.append([tempVal1,tempNum])
    return tempList

def euclidean_distance(a,b):
    c = [math.pow(a[i] - b[i],2) for i in range(len(a))]
    return round(math.sqrt(sum(c)),2)

def calc_min_distance(value,blist):
    temp = [euclidean_distance(value,val),val,val] for val in blist]
    sorted_temp = sorted(temp,key=operator.itemgetter(0))


def calc_distance(alist,blist):

def main():
    xVal = ["A","B","C","D","E","F","G","H","I","J"]
    subs = ["A1","B2","D2","D3","B6","D7","F10","G1","G4","I1",
            "I5","I7","J2","J3","J6"]
    battleships = ["B1","C4","D9","F1","F2","F3","F5","F8",
                   "G5","G6","G8","H7","J1","J4","J10"]

    subCoor = create_coordinate(subs,xval)
    battleshipCoor = create_coordinate(battleships,xval)
    calc_distance(subCoor,battleshipCoor)




main()
