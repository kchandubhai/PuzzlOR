#PuzzlOR February 2010 Planet Colonisation
# area 19

import operator

def calc_distance(alist,resourceData,resourceList):
    newresourceList = resourceList
    outputList = []
    for value in alist:
        if value in resourceData:
            if resourceData[value] not in newresourceList:
                outputList.append([resourceData[value],1])
                newresourceList.append(resourceData[value])
    return [outputList,newresourceList]

def generate_adjacent_position(position,positionData):
    return positionData[position]

def generate_distance(position,resourceData,positionData):
    distanceData = 0
    resourceList = []
    positionTraversed = []
    #check position
    if position in resourceData:
        resourceList.append(resourceData[position])

##    #first set of positions
##    adjacentPosition = generate_adjacent_position(position,positionData)
##    print(calc_distance(adjacentPosition,resourceData,resourceList))
##
##    #check left side






    print(resourceList)
    #print(adjacentPosition)
##    nextPosition = generate_adjacent_position(position,positionData)
##    nextPosition.insert(0,position)
##    #allPosition.append(nextPosition)
##    for i in nextPosition:
##        allPosition.append(generate_adjacent_position(i,positionData))
##    print(allPosition)
##
##    for alist in allPosition:
##        for i in alist:
##            if i not in positionTraversed:
##                positionTraversed.append(i)
##                if i in resourceData:
##                    resourceList.append(resourceData[i])
##    print(positionTraversed)
##    print(resourceList)
##                if i in resourceData:
##                    resourceList.append(resourceData[i])
##                    resourceList = list(set(resourceList))



##    startPosition = [position] + generate_adjacent_position(position,positionData)
##    #print(currentPosition)
##    for i in startPosition:
##        if i in resourceData and i not in positionTraversed and \
##        resourceData[i] not in resourceList:
##            positionTraversed.append(i)
##            resourceList.append(resourceData[i])
##    print(positionTraversed)
##    print(resourceList)





landingPosition = range(1,21)

resources = {
2:"energy",
7:"food",
8:"water",
12:"power",
14:"oxygen",
16:"water",
19:"oxygen",
20:"food",
}

positionData = {
1:[2,8,5],
2:[1,10,3],
3:[4,12,2],
4:[3,14,5],
5:[4,1,6],
6:[7,5,15],
7:[6,8,17],
8:[7,1,9],
9:[8,10,20],
10:[9,2,11],
11:[10,19,12],
12:[11,3,13],
13:[12,14,18],
14:[13,4,15],
15:[14,16,6],
16:[15,18,17],
17:[16,20,7],
18:[16,19,13],
19:[18,11,20],
20:[19,17,9]
}

generate_distance(9,resources,positionData)

##for i in [1, 2, 8, 5, 10, 3, 7, 9, 4, 6]:
##    if i in resources:
##        print(i)
##distanceCalc = [calc_distance(position, resources, positionData) for position in landingPosition]
##sorted_distance = sorted(distanceCalc,key=operator.itemgetter(1))
##print(sorted_distance[0])


