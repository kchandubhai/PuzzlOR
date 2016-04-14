# PuzzlOR October 2015
# BABC
import math
import operator
import itertools


def euclidean_distance(a,b):
    c = [math.pow(a[i] - b[i],2) for i in range(len(a))]
    return round(math.sqrt(sum(c)),2)


sampleRaceCar = [
[['AE','AT','ATR','CB'],12],
[['CE','BT','ATR','CB'],17],
[['CE','AT','BTR','BB'],14],
[['BE','BT','ATR','CB'],13],
[['AE','BT','BTR','AB'],15],
[['AE','CT','BTR','CB'],11],
[['BE','CT','CTR','AB'],16],
[['BE','BT','ATR','BB'],19],
[['CE','AT','CTR','AB'],18],
[['CE','CT','CTR','BB'],20]
]

configurationData = {
"AE":1,
"BE":2,
"CE":3,
"AT":1,
"BT":2,
"CT":3,
"ATR":1,
"BTR":2,
"CTR":3,
"AB":1,
"BB":2,
"CB":3
}

allConfiguration = ["AE","BE","CE","AT","BT","CT","ATr","BTr","CTr","AB","BB","CB"]
for configuration in itertools.combinations(allConfiguration,4):
    config = list(configuration)
    
