# PuzzlOR October 2015 Racecar design

import math
import operator
import itertools






#def euclidean_distance(a,b):
#    c = [math.pow(a[i] - b[i],2) for i in range(len(a))]
#    return round(math.sqrt(sum(c)),2)
#
#def generate_data(config,configData):
#    return [configData[i] for i in config]
#
#def find_closest(config,sampleList,configData):
#    output = [[euclidean_distance(generate_data(value[0],configData),generate_data(config,configData)),value[1],config] for value in sampleList]
#    sorted_output = sorted(output, key=operator.itemgetter(0))
#    return sorted_output[0]
#
#sampleRaceCar = [
#[['AE','AT','ATR','CB'],12],
#[['CE','BT','ATR','CB'],17],
#[['CE','AT','BTR','BB'],14],
#[['BE','BT','ATR','CB'],13],
#[['AE','BT','BTR','AB'],15],
#[['AE','CT','BTR','CB'],11],
#[['BE','CT','CTR','AB'],16],
#[['BE','BT','ATR','BB'],19],
#[['CE','AT','CTR','AB'],18],
#[['CE','CT','CTR','BB'],20]
#]
#
#configurationData = {
#"AE":1,
#"BE":2,
#"CE":3,
#"AT":1,
#"BT":2,
#"CT":3,
#"ATR":1,
#"BTR":2,
#"CTR":3,
#"AB":1,
#"BB":2,
#"CB":3
#}
#
##config = ["AE","BE","AE","AT"]
##print(find_closest(config,sampleRaceCar,configurationData))
#

def calc_parts(config,scores):
    distanceCalc = 0
    for value in config:
        distanceCalc += scores[value]
    return distanceCalc

outputList = []
engines = ["AE","BE","CE"]
tires = ["AT","BT","CT"]
transmissions = ["ATR","BTR","CTR"]
brakes = ["AB","BB","CB"]
allConfiguration = ["AE","BE","CE","AT","BT","CT","ATR","BTR","CTR","AB","BB","CB"]

scores = {
"AE": 8,
"BE": 6,
"CE": 7,
"AT": 2,
"BT": 5,
"CT": 1,
"ATR": 1,
"BTR": 1,
"CTR": 8,
"AB": 1,
"BB": 4,
"CB": 1
}
#
for engine in engines:
    for tire in tires:
        for transmission in transmissions:
            for brake in brakes:
                config = [engine,tire,transmission,brake]
                outputList.append([config,calc_parts(config,scores)])
outputListSorted = sorted(outputList,key=operator.itemgetter(1))
print(outputListSorted)
#                outputList.append(find_closest(config,sampleRaceCar,configurationData))
#sorted_outputList = sorted(outputList,key=operator.itemgetter(1))
#
#print(sorted_outputList)
