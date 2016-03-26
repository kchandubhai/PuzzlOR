# PuzzlOR August 2015 Moon Rover

import math
import random
import itertools
import operator
from collections import Counter
from operator import itemgetter

def euclidean_distance(a,b):
    c = [math.pow(a[i] - b[i],2) for i in range(len(a))]
    return math.sqrt(sum(c))

def calc_distance(alist,valueLookUp,distance):
    sumval = 0
    countval = 0
    templist = []
    scoreval = 0
    while countval < len(alist)-1:
        val1 = valueLookUp[alist[countval]]
        val2 = valueLookUp[alist[countval + 1]]
        tempval = sumval + euclidean_distance(val1[0],val2[0])
        scoreval += val1[1]
        if tempval >= distance:
            break
        sumval += euclidean_distance(val1[0],val2[0])
        templist.append(alist[countval])
        countval += 1
    return [sumval,templist,scoreval]

def main():
    values = ["A8","B3","D10","E2","G3","G6","G8","H1",'H4',"I7"]
    moonPosition = {
    "A8":[[1,8],3],"B3":[[2,3],3],"D6":[[4,6],0],"D10":[[4,10],5],
    "E2":[[5,2],4],"G3":[[7,3],5],"G6":[[7,6],4],"G8":[[7,8],2],
    "H1":[[8,1],2],'H4':[[8,4],1],"I7":[[9,7],1]
    }

    finalist = []
    distance = 25
    maxDistance = 0
    maxScore = 0
    for arrangement in itertools.permutations(values):
        temp = list(arrangement)
        temp.insert(0,"D6")
        temp1 = calc_distance(temp,moonPosition,distance)
        if temp1[2] > maxScore:
            del finalist[:]
            maxScore = temp1[2]
            finalist.append(temp1)        
    print (finalist[2])


main()
