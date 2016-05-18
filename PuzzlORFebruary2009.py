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
    distanceCalc = 0
    for factory in factories:
        townAssigned = []
        checkVal = False
        while not checkVal:
            townData = find_closest(factory,towns,townAssigned,xVal) #find closest town
            townDataTemp = factories[factory]
            factoryDataTemp = towns[townData[1]]
            if factoryDataTemp <= abs(townDataTemp):
                towns[townData[1]] += factoryDataTemp
                checkVal = True
                break
            elif factoryDataTemp >= abs(townDataTemp):
                townAssigned.append(townData[1])
                factories[factory] += towns[townData[1]]                
                towns[townData[1]] = 0
                        								
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
        #print(tempFactories)        
        #sortedFactories = sorted(tempFactories.items(),key=operator.itemgetter(1,0))
        #print(dict(sortedFactories))
              
        #outputList.append(assign(tempFactories,towns,xVal))
    print(outputList)
        
main()        

        

   





