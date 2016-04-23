# PuzzlOR December 2014 Electrifying

import random
import math
import itertools
import string

def find_min(alist):
    minval = min(alist)
    val = alist.index(minval)
    return val

def generate_distance(substation,neighborhood,yVal):
    distanceCalc = 0
    templist = []
    templist2 = []
    substation0 = substation[0]
    substation1 = substation[1]
    substation2 = substation[2]
    substation0position = generate_coordinate(substation0,yVal)
    substation1position = generate_coordinate(substation1,yVal)
    substation2position = generate_coordinate(substation2,yVal)
    for area in neighborhood:
        areaCalc = generate_coordinate(area,yVal)
        templist = [
        round(euclidean_distance(areaCalc,substation0position),2),
        round(euclidean_distance(areaCalc,substation1position),2),
        round(euclidean_distance(areaCalc,substation2position),2)
        ]
        templist2.append(find_min(templist))
        print(templist)
        #print(templist2)
        distanceCalc += min(templist)
        #print(distanceCalc)
    print(templist2)
    if len(set(templist2)) != 3:
        distanceCalc = 10000
    return round(distanceCalc,2)

def generate_coordinate(value,alist):
    tempList = []
    tempVal = value[0]
    tempNum = int(value[1]) - 1
    tempVal1 = int(alist.index(tempVal)) + 1
    tempList.extend([tempVal1,tempNum])
    return tempList

def generate_area(xVal,yVal):
    return [str(y) + str(x) for x in xVal for y in yVal]

def euclidean_distance(a,b):
    c = [math.pow(a[i] - b[i],2) for i in range(len(a))]
    return math.sqrt(sum(c))

def main():
    xVal = range(1,11)
    yVal = [i for i in string.ascii_uppercase[:10]]
    neighborhoods = ["A6","B2","B4","B5","B7",
                     "C5","C10","D9","E2","E6",
                     "E8","F3","F5","G8","G9",
                     "H3","H5","H7","H8","J4"]
    #print(generate_coordinate("E6",yVal))
    #[(1, 2), (0, 6), (8, 3)]
#    ["C2","G1","D9"]
    allList = generate_area(xVal,yVal)
    countlist = []
    tempval = generate_distance(["B1","F1","H4"], neighborhoods, yVal)
    countlist.append(tempval)
    output = list(set(countlist))
    output.sort()
    print(output[0])
    
#    for substations in itertools.combinations(allList,3):
#         tempval = generate_distance(list(substations), neighborhoods, yVal)
#         countlist.append(tempval)
#    output = list(set(countlist))
#    output.sort()
#    print(output[0])

main()
