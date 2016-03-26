# PuzzlOR October 2014 - Fighters
#http://www.puzzlor.com/2014-10_Fighters.html
import random
from collections import Counter
import operator

def generate_fighter(alist):
    return random.randint(0,len(alist)-1)

def chooseFighter(alist):
    templist = []
    attacker = alist[generate_fighter(alist)]
    defender = alist[generate_fighter(alist)]
    while attacker == defender:
        defender = alist[generate_fighter(alist)]
    templist.extend([attacker,defender])
    return templist

def checkHealth(fighterName,fighterInfo):
    if fighterInfo[fighterName][0] < 1:
        return True
    return False

winData = []
countval = 0
maxval = 10000
while countval < maxval:
    fighterNames = ["Allan","Barry","Charles","Dan"]
    #[health, attack]
    fighterData  = {
    "Allan":[10,4],
    "Barry":[12,3],
    "Charles":[16,2],
    "Dan":[18,1]
    }
    while len(fighterNames) != 1:
        fighters = chooseFighter(fighterNames)
        tempfighters = fighters
        attackerinfo = fighterData[tempfighters[0]]
        defenderinfo = fighterData[tempfighters[1]]
        fighterData[tempfighters[1]] = [defenderinfo[0]-attackerinfo[1],defenderinfo[1]]

        if checkHealth(tempfighters[0],fighterData):
            fighterNames.remove(tempfighters[0])
    winData.append(fighterNames[0])
    countval+=1
a = dict(Counter(winData))
sorted_a = sorted(a.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_a)
print(sorted_a[0][0],round(sorted_a[0][1]/maxval,2))
