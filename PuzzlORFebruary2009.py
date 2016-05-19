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
    assigned2 = []
    for factory in factories:
        townAssigned = []
        checkVal = False
        while not checkVal:
            townData = find_closest(factory,towns,townAssigned,xVal)
            townDataTemp = towns[townData[0]]
            factoryDataTemp = factories[factory]
            if factoryDataTemp <= abs(townDataTemp):
                factories[factory] = 0
                towns[townData[0]] += factoryDataTemp
                checkVal = True
                assigned2.append([factory,townData[0]])
                break
            elif factoryDataTemp >= abs(townDataTemp):
                townAssigned.append(townData[0])
                factories[factory] += towns[townData[0]]                
                towns[townData[0]] = 0
                assigned.append([factory,townData[0]])
    return (assigned,assigned2)
                        								
def main():
    xVal = ["A","B","C","D","E"]
    yVal = [1,2,3,4,5]
    area = generate_area(xVal,yVal)

    factories = {"A1":500,"A5":1000,"C3":1500,"E2":1000}
    towns = {"A4":-500,"B2":-2000,"C4":-500,"E1":-1500,"E5":-500}
    factoryTownData = ["A1","A5","C3","E2","A4","B2","C4","E1","E5"]

    possibleArea = [i for i in area if i not in factoryTownData]
    possibleAreaCapacity = 1000

    tempFactories = {'A2': 1000, 'A5': 1000, 'C3': 1500, 'A1': 500, 'E2': 1000}
    print(assign(tempFactories,towns,xVal))
#    outputList = []
#    for area in possibleArea:
#        temp = {}
#        temp[area] = possibleAreaCapacity
#        tempFactories = temp
#        tempFactories.update(factories)        
#        print(assign(tempFactories,towns,xVal))     
#        #outputList.append(assign(tempFactories,towns,xVal))
#   # print(outputList)
        
main()        

        

   





