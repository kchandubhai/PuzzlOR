# PuzzlOR June 2013 Self Driving Cars
import itertools
import random
import math
import operator

def checkVal(alist,blist):
    templist = []
    for val in alist:
        if val not in blist:
            templist.append(val)
    return templist

def euclidean_distance(a,b):
    c = [math.pow(a[i] - b[i],2) for i in range(len(a))]
    return math.sqrt(sum(c))

def find_closest(endpoint,area,startPositionList):
    tempDistanceList = []
    tempDistanceList3 = []
    for value in area:
        tempDistanceList.append([value,euclidean_distance(endpoint,value[0])])
    tempDistanceList2 =  sorted(tempDistanceList,key=operator.itemgetter(1))
    for val in tempDistanceList2:
        tempDistanceList3.append(val[0])
    tempval2 = checkVal(tempDistanceList3,startPositionList)
    return tempval2[0]

def main():
    area = [[[2,1],[5,2]],
	[[7,1],[9,4]],[[9,2],[6,6]],
	[[5,4],[2,3]],[[4,5],[7,9]],
    [[8,5],[2,4]],[[3,7],[7,7]],
    [[4,8],[1,10]],[[3,10],[10,7]],
    [[8,10],[9,8]]]

    calcList = []
    countval = 0
    startPositionList = []
    distance_calc = 0
    
    calcList = []
    for value in area:
       startPosition = value
       countval = 0
       startPositionList = []
       distance_calc = 0
       while countval < len(area)-1:
           startPositionList.append(startPosition)
           distance_calc += euclidean_distance(startPosition[0],startPosition[1])
           nextPosition = find_closest(startPosition[1],area,startPositionList)
           distance_calc += euclidean_distance(startPosition[1],nextPosition[0])
           startPosition = nextPosition
           countval += 1
       calcList.append(distance_calc)
       print(startPositionList)
       print(distance_calc)
    calcList.sort()
    print(calcList)

main()