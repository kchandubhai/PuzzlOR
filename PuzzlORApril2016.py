# PuzzlOR April 2016 Cell Towers

import itertools
import sys

def get_tower_surrounding(positionData,positionInfo):
    output = []
    for i in positionData:
        output.extend(get_surrouding_position(i,positionInfo))
    return list(set(output))

def generate_area(xVal,yVal):
    return [str(x) + str(y) for x in xVal for y in yVal]

def get_surrouding_position(position, positionInfo):
    tempval = position[0]
    tempnum = int(position[1:])
    templistnum = []
    finallist = []
    templistval = positionInfo[tempval]
    if tempnum == 1:
        templistnum.extend([tempnum,tempnum+1])
    elif tempnum in [2,3,4,5,6,7,8,9]:
        templistnum.extend([tempnum-1,tempnum,tempnum+1])
    elif tempnum == 10:
        templistnum.extend([tempnum-1,tempnum])
    for val in templistval:
        for num in templistnum:
            finallist.append(val + str(num))
    return finallist

def main():
    xVal = ['A',"B","C","D","E","F","G","H","I","J"]
    yVal = [1,2,3,4,5,6,7,8,9,10]
    
    area = generate_area(xVal,yVal)
    
    positionInfo = {
    "A":["A","B"],
    "B":["A","B","C"],
    "C":["B","C","D"],
    "D":["C","D","E"],
    "E":["D","E","F"],
    "F":["E","F","G"],
    "G":["F","G","H"],
    "H":["G","H","I"],
    "I":["H","I","J"],
    "J":["I","J"]
    }
    neighborhoods = ["A1","A2","A4","A5","A9",
    "B4","C2","C4","C6","C10","D4","D5","D8",
    "E1","E3","E4","E5","E7","E9","E10",
    "F1","F6","F8","F10","G2","G3","G5","G6",
    "G7","G8","H2","H6","H10","I1","I6",
    "I7","I8","J1","J2","J4","J8"]
    
    towerData = range(2,10)
    checkData = 0.7 * len(neighborhoods)
    print(checkData)
#    for value in itertools.combinations(area,2):
#        positionData = list(value):
            
    
 


    
    
main()