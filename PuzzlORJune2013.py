# PuzzlOR June 2013 Self Driving Cars

import itertools
import random
import math
import operator


def euclidean_distance(a,b):
    c = [math.pow(a[i] - b[i],2) for i in range(len(a))]
    return math.sqrt(sum(c))

def find_closest(endpoint,area,startPositionList):
    tempDistanceList = []
    for value in area:
        tempDistanceList.append([value,euclidean_distance(endpoint,value[0])])
    tempDistanceList2 =  sorted(tempDistanceList,key=operator.itemgetter(1))
    return tempDistanceList2[0][0]

def main():
    area = [[[2,1],[5,2]],
	[[7,1],[9,4]],[[9,2],[6,6]],
	[[5,4],[2,3]],[[4,5],[7,9]],
    [[8,5],[2,4]],[[3,7],[7,7]],
    [[4,8],[1,10]],[[3,10],[10,7]],
    [[8,10],[9,8]]]

    #print(find_closest([5,2],area,[[5,4],[4,8]]))

    calcList = []
    for value in area:
        startPosition = value
        countval = 0
        maxcount = 10
        startPositionList = []
        distance_calc = 0
        while countval < maxcount:
            startPositionList.append(startPosition)
            distance_calc += euclidean_distance(startPosition[0],startPosition[1])
            nextPosition = find_closest(startPosition[1],area,startPositionList)
            startPosition = nextPosition
            countval += 1
        calcList.append(distance_calc)
    calcList.sort()
    print(calcList)
