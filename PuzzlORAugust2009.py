# PuzzlOR August 2009 Bridges

# goal: Which two bridges should be built in order to minimize the total commuting distance of all residents?
import itertools
import random
import math
import operator

def calculate_distance(homeWorkData,bridgeData,chosenBridges):
    firstBridge = bridgeData[chosenBridges[0]]
    secondBridge = bridgeData[chosenBridges[1]]
    return (firstBridge,secondBridge)

def manhattan_distance(a,b):
    c = [abs(a[i] - b[i]) for i in range(len(a))]
    return sum(c)

def main():

    bridges = ["one","two","three","four"]
    bridgeData = {
    "one":[[6,12],[8,12]],
    "two":[[6,7],[8,7]],
    "three":[[6,4],[8,4]],
    "four":[[6,2],[8,2]]
    }


    homeWorkData = [[[4,12],[12,8]],[[2,11],[10,12]],
    [[3,8],[10,5]],[[2,7],[12,2]],[[2,4],[10,2]]]

    chosenBridges = ["one","two"]
    print(calculate_distance(homeWorkData,bridgeData,chosenBridges))

##    for value in itertools.combinations(bridgeData,2):
##        print(list(value))
##    print(homeWorkData[4])
##    print(manhattan_distance(homeWorkData[4][0],homeWorkData[4][1]))


main()
