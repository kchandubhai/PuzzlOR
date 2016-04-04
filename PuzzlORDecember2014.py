# PuzzlOR December 2014 Electrifying
# Electrifying - 35.63M
import random
import math
import itertools

def find_min(alist):
    minval = min(alist)
    val = alist.index(minval)
    return val

def testgenerate_distance(substation,neighborhood,yVal):
    distanceCalc = 0
    templist = []
    templist2 = []
    
    substation0 = substation[0]
    # substation1 = substation[1]
    # substation2 = substation[2]
    substation0position = generate_coordinate(substation0,yVal)
    # substation1position = generate_coordinate(substation1,yVal)
    # substation2position = generate_coordinate(substation2,yVal)
    #print(substation0position)
    for area in neighborhood:
        #print(area)
        areaCalc = generate_coordinate(area,yVal)
        templist = [euclidean_distance(areaCalc,substation0position)]
        print(templist,area)
        # ,
        # euclidean_distance(areaCalc,substation1position),
        # euclidean_distance(areaCalc,substation2position)
        # print("")
        # templist2 = [
        # euclidean_distance(substation0position,areaCalc)]
        # print(templist2)
    #     templist2.append(find_min(templist))
    #     distanceCalc += min(templist)
    # if len(set(templist2)) != 3:
    #     distanceCalc = 10000
    # return round(distanceCalc,2)

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
        euclidean_distance(areaCalc,substation0position),
        euclidean_distance(areaCalc,substation1position),
        euclidean_distance(areaCalc,substation2position)
        ]
        templist2.append(find_min(templist))
        distanceCalc += min(templist)
    if len(set(templist2)) != 3:
        distanceCalc = 10000
    return round(distanceCalc,2)

def generate_coordinate(value,alist):
    tempList = []
    tempVal = value[0]
    tempNum = int(value[1])
    #tempVal1 = int(alist.index(tempVal))
    tempVal1 = int(alist.index(tempVal)) + 1
    tempList.extend([tempVal1,tempNum])
    return tempList

def generate_area(xVal,yVal):
    templist = []
    for x in xVal:
        for y in yVal:
            templist.append(str(y) + str(x))
    return templist

def euclidean_distance(a,b):
    c = [math.pow(a[i] - b[i],2) for i in range(len(a))]
    return round(math.sqrt(sum(c)),2)

def main():
    xVal = [1,2,3,4,5,6,7,8,9,10]
    yVal = ["A","B","C","D","E","F","G","H","I","J"]
    neighborhoods = ["A6","B2","B4","B5","B7",
                     "C5","C10","D9","E2","E6",
                     "E8","F3","F5","G8","G9",
                     "H3","H5","H7","H8","J4"]
    
    allList = generate_area(xVal,yVal)
    countlist = []
    # testval = ["B2","E5","B2", "A6", "H3"]
    # tempval = testgenerate_distance(testval, neighborhoods, yVal)
    
    for substations in itertools.combinations(allList,3):
         tempval = generate_distance(list(substations), neighborhoods, yVal)
         countlist.append(tempval)
    output = list(set(countlist))
    output.sort()
    print(output)

main()
