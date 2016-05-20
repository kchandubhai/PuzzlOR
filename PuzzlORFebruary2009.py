# PuzzlOR February 2009 Supply & Demand
# $74,465 (or $90,000

import math
import operator

def find_closest(position,allPosition,positionUsed,xVal):
    positionData = []
    for value in allPosition:
        if value not in positionUsed:
            positionData.append([value,euclidean_distance(generate_coordinate(position,xVal),generate_coordinate(value,xVal))])
    sortedPosition = sorted(positionData,key=operator.itemgetter(0))   
    return sortedPosition[0]
                 
def euclidean_distance(a,b):
    return math.sqrt(sum([math.pow(a[i]-b[i],2) for i in range(len(a))]))

def manhattan_distance(a,b):
    return sum([abs(a[i] - b[i]) for i in range(len(b))])

def generate_coordinate(value,alist):
    return [int(alist.index(value[0])) + 1,int(value[1])]

def generate_area(xVal,yVal):
    return [str(x) + str(y) for x in xVal for y in yVal]

def assign(factories,towns,xVal):
    assigned = []
    townAssigned = []
    for factory in factories:
        checkVal = False
        while not checkVal:
            if len(townAssigned) == len(factories):
              return (assigned)
            closestTown = find_closest(factory,towns,townAssigned,xVal)
            townData = towns[closestTown[0]]
            factoryData = factories[factory]
            if factoryData >= abs(townData):
                townAssigned.append(closestTown[0])
                factories[factory]+=townData
                towns[closestTown[0]] = 0
                assigned.append([factory,closestTown[0]])
            elif factoryData <= abs(townData):
                towns[closestTown[0]] += factoryData
                factories[factory] = 0
                assigned.append([factory,closestTown[0]])
                checkVal = True
                break
    return (assigned)
                

def main():
    xVal = ["A","B","C","D","E"]
    yVal = [1,2,3,4,5]
    area = generate_area(xVal,yVal)

    factories = {"A1":500,"A5":1000,"C3":1500,"E2":1000}
    towns = {"A4":-500,"B2":-2000,"C4":-500,"E1":-1500,"E5":-500}
    factoryTownData = ["A1","A5","C3","E2","A4","B2","C4","E1","E5"]

    possibleArea = [i for i in area if i not in factoryTownData]
    possibleAreaCapacity = 1000


    outputList = []
    for area in possibleArea:
        temp = {}
        temp[area] = possibleAreaCapacity
        tempFactories = temp
        tempFactories.update(factories)             
        outputList.append(assign(tempFactories,towns,xVal))
    print(outputList)
        
main()        

        

   





