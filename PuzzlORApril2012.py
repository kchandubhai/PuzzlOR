# PuzzlOR April 2012 McEverywhere
# 3

def generate_coordinate(value,alist):
    tempList = []
    tempVal = value[0]
    tempNum = int(value[1])
    tempVal1 = int(alist.index(tempVal)) + 1
    tempList.append([tempVal1,tempNum])
    return tempList
    

def generate_area(xVal,yVal):
    templist = []
    for x in xVal:
        for y in yVal:
            templist.append(str(x) + str(y))
    return templist

def euclidean_distance(a,b):
    c = [math.pow(a[i] - b[i],2) for i in range(len(a))]
    return math.sqrt(sum(c))


def main():
    xVal = ['A',"B","C","D","E","F","G","H","I"]
    yVal = [1,2,3,4,5,6,7,8,9,10]
    homeLocation = ["A4","A8","A9","A10","B4","B7",
    "C8","C9","D2","E1","F2","F5","F6","G5","G9",
    "H3","H5","I5","I9","J7"]
    #print(generate_area(xVal,yVal))
    #print(len(homeLocation))
    #print(generate_coordinate("B2",xVal))

main()
