## puzzlOR October 2009
## Connected and infected
# 21
def main():
    world = {
    "blue":["blue","violet","red"],
    "violet":["violet","blue","green","yellow"],
    "red":["red","blue"],
    "yellow":["yellow","violet"],
    "green":["green","violet"]
    }

    constval = 10**9
    currentBlue = 0.5 * constval
    currentRed = 0.5 * constval
    currentViolet = 4 * constval
    currentYellow = 1 * constval
    currentGreen = 0.5 * constval
    currentPopulation = currentBlue + currentRed + currentViolet + currentYellow
    + currentGreen

##    print(currentPopulation)
##    infectionCount = 0
##    monthCount = 0
##    while infectionCount < 0.5*currentPopulation:
##        dosomething

main()
