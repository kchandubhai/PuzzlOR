# PuzzlOR October 2009 Connected and Infected


def update_infected_pop(infectionArea,infectionData,currentInfectionArea):    

##population info
constval = 10**9		
currentBlue = 0.5 * constval		
currentRed = 0.5 * constval		
currentViolet = 4 * constval		
currentYellow = 1 * constval		
currentGreen = 0.5 * constval		
currentPopulation = currentBlue + currentRed + currentViolet + currentYellow		
+ currentGreen



infectionData = {		
 "blue":10000,		
 "violet":0,		
 "red":0,		
 "yellow":0,		
 "green":0		
 }
 
infectionArea = {
 "blue":["blue","violet","red"],		
 "violet":["violet","blue","green","yellow"],		
 "red":["red","blue"],		
 "yellow":["yellow","violet"],		
 "green":["green","violet"]	
 }

currentInfectedArea = ["blue"]
checkVal = False
populationInfected = 0
monthCount = 0

while not checkVal:
    if populationInfected >= 0.5*currentPopulation:
        checkVal = True
        break
    else:
        monthCount+=1
        currentInfectedArea = update_infected_pop(infectionArea,infectionData,currentInfectionArea)[0]
        populationInfected = update_infected_pop(infectionArea,infectionData,currentInfectionArea)[1]
        infectionArea = update_infected_pop(infectionArea,infectionData,currentInfectionArea)[2]
        infectionData = update_infected_pop(infectionArea,infectionData,currentInfectionArea)[3] 
print(monthCount)



