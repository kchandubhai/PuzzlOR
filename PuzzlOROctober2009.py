## puzzlOR October 2009
## Connected and infected
## 21

def update_population(area,areaList):
    for areas in areaList:
        for value in areas[0]:


def disease_spread(areaData,infectedArea):
    output = []
    for value in infectedArea:
        update_populationp(value,areaData[value])











areaData = {
"blue":[["blue","violet","red"],10000],
"violet":[["violet","blue","green","yellow"],0],
"red":[["red","blue"],0],
"yellow":[["yellow","violet"],0],
"green":[["green","violet"],0]
}

constval = 10**9
currentBlue = 0.5 * constval
currentRed = 0.5 * constval
currentViolet = 4 * constval
currentYellow = 1 * constval
currentGreen = 0.5 * constval
currentPopulation = currentBlue + currentRed + currentViolet + currentYellow
+ currentGreen

infectedArea = ["blue"]

monthCount = 0
populationInfected = 0


while populationInfected < 0.5*currentPopulation:

    disease_spread(areaData,infectedArea)

    break
print(monthCount)
