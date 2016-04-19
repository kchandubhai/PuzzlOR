#PuzzlOR February 2010 Planet Colonisation
# area 19

import math
import operator

def calc_distance(position,area):
    resources = []


landingPosition = range(1,21)

distanceCalc = []
positionData = {
1:[2],
2:[3,10],
3:[2,4,12],
4:[3,5,14],
5:[4,6],
6:[5,7,15],
7:[6,8,17],
8:[7,9],
9:[8,10,20],
10:[2,9,11],
11:[10,12,19],
12:[3,11,13],
13:[12,14,18],
14:[4,13,15],
15:[6,14,16],
16:[15,17,18],
17:[7,16,19,20],
18:[13,16,19],
19:[11,17,18,20],
20:[9,17,19],
}
for position in landingPosition
