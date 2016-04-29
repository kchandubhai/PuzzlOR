## puzzlOR October 2009
## Connected and infected
## 21

def update_area(areaData,areaScore,infectedArea):
    areaInfo = []
    for value in infectedArea:
        areaInfo.extend(areaData[value])
    areaInfo = list(set(areaInfo))
    for value in areaScore:
        if value[0] in areaInfo:










# add areascore to area data
areaData = {
"blue":["blue","violet","red"],
"violet":["violet","blue","green","yellow"],
"red":["red","blue"],
"yellow":["yellow","violet"],
"green":["green","violet"]
}

areaScore = [["blue",10000],["violet",0],["red",0],["yellow",0],["green",0]]

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

print(update_area(areaData,areaScore,infectedArea))

while populationInfected < 0.5*currentPopulation:

    output = update_area(areaData,areaScore,infectedArea)
    populationInfected = output[0]
    infectedArea = output[1]
    print(populationInfected)
    monthCount+=1
    break
print(monthCount)





