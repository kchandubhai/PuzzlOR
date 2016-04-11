# PuzzlOR February 2016 Toy Builder

import math
import random

def generate_random(alist):
    return (random.randint(0,len(alist)-1))

def update_part(parts,toy):
    return [parts[i] - toy[i] for i in range(len(parts))]

def check_availablity(parts,toy):
    if len(parts) < 1:
        return True
    output = []
    for i in range(len(parts)):
        if parts[i] - toy[i] < 1:
            output.append(parts[i] - toy[i])
    if len(output) > 1:
        return True
    return False

maxProfit = []
profit = 0
partAvailable = [25,29,30]
toyBuilder = [['airplane',[3,2,1],7],['helicopter',[2,4,1],8],['car',[1,2,4],5]]


checkAvailable = False
while not checkAvailable:
    toy = toyBuilder[generate_random(toyBuilder)]
    print(toy)
    if check_availablity(partAvailable,toy[1]):
        checkAvailable = True
    else:
        partsAvailable = update_part(partAvailable,toy[1])
        print(partAvailable)
        profit += toy[2]
        print(profit)
print(profit)




