# PuzzlOR June 2013 Self Driving Cars

import math
import operator
import itertools

def checkVal(alist,blist):
    return [val for val in alist if val not in blist]

def euclidean_distance(a,b):
    c = [math.pow(a[i] - b[i],2) for i in range(len(b))]
    return math.sqrt(sum(c))

#insertion heuristics (closest route)
def find_closest(endpoint,area,startPositionList):
    distanceList = [[value,euclidean_distance(endpoint,value[0]),
    euclidean_distance(endpoint,value[1])] for value in area]
    distanceList2 =  sorted(distanceList,key=operator.itemgetter(1,2))
    distanceList3 = [val[0] for val in distanceList2]
    outputList = checkVal(distanceList3,startPositionList)
    return outputList[0]

def calc_distance(alist,areainfo):
    checkVal = False
    count = 0
    distance = 0
    while not checkVal:
        if count == len(alist)-1:
            output = areainfo[alist[count]]
            distance+=euclidean_distance(output[0],output[1])
            checkVal = True
            break
        elif count > 0 and count < len(alist)-1:
            output = areainfo[alist[count]]
            output2 = areainfo[alist[count-1]]
            distance += euclidean_distance(output[0],output[1]) + euclidean_distance(output2[1],output[0])
        else:
            output = areainfo[alist[count]]
            distance+=euclidean_distance(output[0],output[1])
        count+=1
        
    return(distance)
            
    
def main():
    area = [[[2,1],[5,2]],[[7,1],[9,4]],
    	   [[9,2],[6,6]],[[5,4],[2,3]],
    	   [[4,5],[7,9]],[[8,5],[2,4]],
    	   [[3,7],[7,7]],[[4,8],[1,10]],
    	   [[3,10],[10,7]],[[8,10],[9,8]]]
    
    areainfo = {"a":[[2,1],[5,2]],
                "b":[[7,1],[9,4]],
                "c":[[9,2],[6,6]],
                "d":[[5,4],[2,3]],
                "e":[[4,5],[7,9]],
                "f":[[8,5],[2,4]],
    	        "g":[[3,7],[7,7]],
                "h":[[4,8],[1,10]],
    	        "i":[[3,10],[10,7]],
                "j":[[8,10],[9,8]]
                }
    areavalues = ["a","b","c","d","e","f","g","h","i","j"]
    outputList = []
    for values in itertools.permutations(areavalues):
        outputList.append(calc_distance(list(values),areainfo))
    outputList.sort()
    print(outputList[0])
      

if __name__ == "__main__": 
    main()
