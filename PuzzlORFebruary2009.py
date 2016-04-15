#PuzzlOR February 2009 Supply & Demand

import sys
import math
import operator
import itertools

def manhattan_distance(a,b):
    return sum([abs(a[i] - b[i]) for i in range(len(b))])

def generate_coordinate(value,alist):
    tempList = []
    tempVal = value[0]
    tempNum = int(value[1])
    tempVal1 = int(alist.index(tempVal)) + 1
    tempList.extend([tempVal1,tempNum])
    return tempList

def generate_area(xVal,yVal):
    return [str(x) + str(y) for x in xVal for y in yVal]

def main():
    xVal = ["A","B","C","D","E"]
    yVal = [1,2,3,4,5]
    area = generate_area(xVal,yVal)
    #1 km = $10, distance is in km

    factories = ["A1","A5","C3","E2"]
    towns = ["A4","B2","C4","E1","E5"]

    supplyData = {
    "A1":500,"A5":1000,"C3":1500,"E2":1000,"A4":-500,
    "B2":-2000,"C4":-500,"E1":-1500,"E5":-500
    }



main()
