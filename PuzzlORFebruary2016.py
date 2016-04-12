# PuzzlOR February 2016 Toy Builder

import math
import random

def generate_random(alist):
    return (random.randint(0,len(alist)-1))

def update_part(parts,toy):
    return [parts[i] - toy[i] for i in range(len(parts))]

def check_valid(parts,toy):
    output = []
    for i in range(len(parts)):
        if parts[i] < toy[i]:
            output.append(i)
    if len(output) > 0:
        return True
    return False

maxProfit = []
countval = 0
maxcount = 10000
while countval < maxcount:
    profit = 0
    partAvailable = [25,29,30]
    toyBuilder = [['airplane',[3,2,1],7],['helicopter',[2,4,1],8],['car',[1,2,4],5]]
    checkAvailable = False
    while not checkAvailable:
        toy = toyBuilder[generate_random(toyBuilder)]
        if check_valid(partAvailable,toy[1]):
            checkAvailable = True
            break
        partAvailable = update_part(partAvailable,toy[1])
        profit += toy[2]
    maxProfit.append(profit)
    countval += 1
maxProfit.sort()
print(max(maxProfit))
