# PuzzlOR December 2014 Electrifying
# Electrifying - 35.63M
import random
import math

def generate_distance(substation, neighborhood,yVal):
    distanceCalc = 0
    templist = []
    substation0 = substation[0]
    substation1 = substation[1]
    substation2 = substation[2]
    substation0position = generate_coordinate(substation0,yVal)
    substation1position = generate_coordinate(substation1,yVal)
    substation2position = generate_coordinate(substation2,yVal)
    for area in neighborhood:
        templist.extend([euclidean_distance(substation0position,generate_coordinate(area,yVal)),
        euclidean_distance(substation1position,generate_coordinate(area,yVal)),
        euclidean_distance(substation2position,generate_coordinate(area,yVal))])
        distanceCalc += min(templist)
    return distanceCalc

def generate_random(alist):
    return random.randint(0,len(alist)-1)

def generate_position(alist,numOfPositions):
    templist = []
    count = 0
    while count < numOfPositions:
        temp = alist[generate_random(alist)]
        if temp not in templist:
            templist.append(temp)
            count += 1
    return templist


def generate_coordinate(value,alist):
    tempList = []
    tempVal = value[0]
    tempNum = int(value[1])
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
    return math.sqrt(sum(c))

def main():
    xVal = [1,2,3,4,5,6,7,8,9,10]
    yVal = ["A","B","C","D","E","F","G","H","I","J"]
    neighborhoods = ["A6","B2","B4","B5","B7"
                     "C5","C10","D9","E2","E6"
                     "E8","F3","F5","G8","G9"
                     "H3","H5","H7","H8","J4"]
    allList = generate_area(xVal,yVal)
    cost = 10**6
    substations = generate_position(generate_area(xVal,yVal),3)
    print(substations)
    tempval = round(generate_distance(substations, neighborhoods,yVal),2)
    print(tempval)
    countval = 0
    maxval = 50
    costlist = []
    while countval < maxval:
        substations = generate_position(generate_area(xVal,yVal),3)
        tempval = round(generate_distance(substations, neighborhoods,yVal),2)
        if tempval not in costlist and tempval != 0.0:
            costlist.append([tempval,substations])
        countval +=1
    costlist.sort()
    print(costlist)


main()
