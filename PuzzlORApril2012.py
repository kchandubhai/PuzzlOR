# PuzzlOR April 2012 McEverywhere
# 3

import math
import itertools

def generate_coordinate(value,alist):
    tempList = []
    tempVal = value[0]
    tempNum = int(value[1])
    tempVal1 = int(alist.index(tempVal)) + 1
    tempList.extend([tempVal1,tempNum])
    return tempList

def generate_area(xVal,yVal):
    return [str(x) + str(y) for x in xVal for y in yVal]
    
def euclidean_distance(a,b):
    c = [math.pow(a[i] - b[i],2) for i in range(len(a))]
    return round(math.sqrt(sum(c)),2)

def calc_distance(position,homeinfo,xdata):
    if len(position) < 2:
        area =  [euclidean_distance(generate_coordinate(i,xdata), \
        generate_coordinate(position[0],xdata)) for  i in homeinfo]
    else:
        outputData = []
        for i in position:
            tempOutput = [euclidean_distance(generate_coordinate(i,xdata),generate_coordinate(home,xdata)) \
            for home in homeinfo]
            outputData.append(tempOutput)
        print(outputData)


    #outputList = [i for i in area if i <= 4]

    #if len(outputList) == len(homeinfo):
    #    return position
    #return None



def main():
    xVal = ['A',"B","C","D","E","F","G","H","I","J"]
    yVal = [1,2,3,4,5,6,7,8,9,10]
    homeLocation = ["A4","A8","A9","A10","B4","B7",
    "C8","C9","D2","E1","F2","F5","F6","G5","G9",
    "H3","H5","I5","I9","J7"]

    outputData = []
    area = generate_area(xVal,yVal)
    position = ['J4', 'J10']
    outputData.append(calc_distance(position,homeLocation,xVal))

    #for val in itertools.combinations(area,2):
    #    position = list(val)
    #    outputData.append(calc_distance(position,homeLocation,xVal))
    #print(outputData)
    #print(min(outputData))



main()
