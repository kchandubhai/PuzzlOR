# PuzzlOR June 2013 Self Driving Cars
# 64.347

import math
import operator

def checkVal(alist,blist):
    return [ val for val in alist if val not in blist]

def euclidean_distance(a,b):
    c = [math.pow(a[i] - b[i],2) for i in range(len(b))]
    return round(math.sqrt(sum(c)),3)

def find_closest(endpoint,area,startPositionList):

    distanceList = [[value,euclidean_distance(endpoint,value[0])] for value in area]
    distanceList2 =  sorted(distanceList,key=operator.itemgetter(1))
    distanceList3 = [val[0] for val in distanceList2]
    outputList = checkVal(distanceList3,startPositionList)
    return outputList[0]

def main():
    area = [[[2,1],[5,2]],[[7,1],[9,4]],
    	   [[9,2],[6,6]],[[5,4],[2,3]],
    	   [[4,5],[7,9]],[[8,5],[2,4]],
    	   [[3,7],[7,7]],[[4,8],[1,10]],
    	   [[3,10],[10,7]],[[8,10],[9,8]]]
    
    calcList = []
    for value in area:
       startPosition = value
       countval = 0
       startPositionList = []
       distanceCalc = 0
       while countval < len(area)-1:
           distanceCalc += euclidean_distance(startPosition[0],startPosition[1])
           startPositionList.append(startPosition)
           nextPosition = find_closest(startPosition[1],area,startPositionList)
           distanceCalc += euclidean_distance(startPosition[1],nextPosition[0])
           startPosition = nextPosition
           countval += 1
       print(startPositionList)
       finalDistance = distanceCalc + euclidean_distance(startPositionList[len(startPositionList)-1][1],startPosition[0]) 
       +  euclidean_distance(startPosition[0],startPosition[1])
       calcList.append(round(finalDistance,3))
       print(calcList)

        


main()
