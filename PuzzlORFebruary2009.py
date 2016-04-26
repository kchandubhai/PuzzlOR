# PuzzlOR February 2009 Supply & Demand
# $74,465 (or $90,000

import math

def euclidean_distance(a,b):
    return math.sqrt(sum([math.pow(a[i]-b[i],2) for i in range(len(a))]))

def manhattan_distance(a,b):
    return sum([abs(a[i] - b[i]) for i in range(len(b))])

def generate_coordinate(value,alist):
    return [int(alist.index(value[0])) + 1,int(value[1])]

def generate_area(xVal,yVal):
    return [str(x) + str(y) for x in xVal for y in yVal]

#def assign_factory_town(factories,towns,xval):
#    distanceCalc = []
#    countval = 0
#    maxcount = 1##len(factories) - 1
#    assignedTown = []
#    while countval < maxcount:
#        checkVal = False
#        distanceList = []
#        while not checkVal:
#            for town in towns:
#                if town[0] not in assignedTown:
#                    factoryData = factories[countval]
#                    distanceList.append([euclidean_distance(generate_coordinate(factoryData[0],xval),generate_coordinate(town[0],xval)),factoryData,town])
#            distanceListsorted = sorted(distanceList,key=operator.itemgetter(0))
#
#            if distanceListsorted[0][1][1] <= abs(distanceListsorted[0][2][1]):
#                indexinfo = towns.index(distanceListsorted[0][2])
#                towns[towns.index(distanceListsorted[0][2])] = [distanceListsorted[0][2][0], distanceListsorted[0][1][1] + distanceListsorted[0][2][1]]
#                distanceCalc.append(distanceListsorted[0][0])
#                if towns[indexinfo][1] >= 0:
#                    assignedTown.append(towns[towns.index(distanceListsorted[0][2])])
#                    checkVal = True
#                    break
#        countval+=1
#    print(distanceCalc)
        

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
    
    #outputList.append(assign_factory_town(tempFactories,towns,xVal))
##    for area in possibleArea:
##        tempFactories = []
##        tempFactories.append([area,possibleAreaCapacity])
##        tempFactories.extend(factories)
##        tempFactories.sort()
##        outputList.append(assign_factory_town(tempFactories,towns))
    #print(outputList)


        
    




main()

##[['A1', 500], ['A2', 1000], ['A5', 1000], ['C3', 1500], ['E2', 1000]]
##[['A1', 500], ['A3', 1000], ['A5', 1000], ['C3', 1500], ['E2', 1000]]
##[['A1', 500], ['A5', 1000], ['B1', 1000], ['C3', 1500], ['E2', 1000]]
##[['A1', 500], ['A5', 1000], ['B3', 1000], ['C3', 1500], ['E2', 1000]]
##[['A1', 500], ['A5', 1000], ['B4', 1000], ['C3', 1500], ['E2', 1000]]
##[['A1', 500], ['A5', 1000], ['B5', 1000], ['C3', 1500], ['E2', 1000]]
##[['A1', 500], ['A5', 1000], ['C1', 1000], ['C3', 1500], ['E2', 1000]]
##[['A1', 500], ['A5', 1000], ['C2', 1000], ['C3', 1500], ['E2', 1000]]
##[['A1', 500], ['A5', 1000], ['C3', 1500], ['C5', 1000], ['E2', 1000]]
##[['A1', 500], ['A5', 1000], ['C3', 1500], ['D1', 1000], ['E2', 1000]]
##[['A1', 500], ['A5', 1000], ['C3', 1500], ['D2', 1000], ['E2', 1000]]
##[['A1', 500], ['A5', 1000], ['C3', 1500], ['D3', 1000], ['E2', 1000]]
##[['A1', 500], ['A5', 1000], ['C3', 1500], ['D4', 1000], ['E2', 1000]]
##[['A1', 500], ['A5', 1000], ['C3', 1500], ['D5', 1000], ['E2', 1000]]
##[['A1', 500], ['A5', 1000], ['C3', 1500], ['E2', 1000], ['E3', 1000]]
##[['A1', 500], ['A5', 1000], ['C3', 1500], ['E2', 1000], ['E4', 1000]]




