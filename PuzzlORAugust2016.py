# PuzzlOR Matchup August 2016

import itertools

manList = range(1,11)
womanList =range(1,11)

#Person    Politics    Hobby    Living Preference    Social
manInfo = {
1:["Liberal","Running","Rural","Introverted"],
2:["Liberal","Chess","Rural","Outgoing"],
3:["Conservative","Running","Urban","Introverted"],
4:["Liberal","Running","Rural","Introverted"],
5:["Conservative","Running","Rural","Introverted"],
6:["Conservative","Chess","Rural","Introverted"],
7:["Conservative","Chess","Urban","Introverted"],
8:["Liberal","Chess","Urban","Introverted"],
9:["Liberal","Running","Urban","Introverted"],
10:["Liberal","Running","Urban","Outgoing"]
}

womanInfo = {
1:["Conservative","Chess","Rural","Introverted"],
2:["Liberal","Running","Rural","Introverted"],
3:["Conservative","Chess","Rural","Outgoing"],
4:["Conservative","Running","Urban","Outgoing"],
5:["Conservative","Chess","Urban","Outgoing"],
6:["Liberal","Running","Urban","Introverted"],
7:["Conservative","Chess","Urban","Outgoing"],
8:["Conservative","Running","Urban","Outgoing"],
9:["Liberal","Chess","Urban","Introverted"],
10:["Liberal","Running","Rural","Introverted"]
}

def getScore(alist,blist):
    score = 0
    for value in range(len(alist)):
        if (alist[value] == blist[value]):
            score += 1
    return score

#def createCombination(manList,womanList):

def checkScore(alist)  

def main():
    #scoreValue = getScore(["Conservative","Chess","Rural","Introverted"],
             ["Liberal","Running","Rural","Introverted"])
    #print(scoreValue)
    #print(manInfo[1])
    #print(manList)

   
if __name__ == "__main__":
    main()



