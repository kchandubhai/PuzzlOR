# PuzzlOR April 2013 Subs and Battleship

import numpy as np
from scipy.optimize import linear_sum_assignment
import math
import itertools
from scipy.spatial.distance import pdist, squareform

def generate_coordinate(value,alist):
    tempList = []
    tempList.extend([int(alist.index(value[0])) + 1,int(value[1])])
    return tempList

def euclidean_distance(a,b):
    c = [math.pow(a[i] - b[i],2)
    for i in range(len(b))]
    return round(math.sqrt(sum(c)),2)

xVal = ["A","B","C","D","E","F","G","H","I","J"]

subs = ["A1","B2","B6","D2","D3","D7","F10",
        "G1","G4","I1","I5","I7","J2","J3","J6"]
ships = ["B1","C4","D9","F1","F2","F3","F5",
         "F8","G5","G6","G8","H7","J1","J4","J10"]

site_location = np.array([[4,6],[1,8],[2,3],[4,10],[5,2],[7,3],[7,6],[7,8],
                              [8,1],[8,4],[9,7]])             
site_score = [0,3,3,5,4,5,4,2,2,1,1]
site_euclidean_distance = (squareform(pdist(site_location,"euclidean")))
print(site_euclidean_distance)
#sub_position = [generate_coordinate(value,xVal) for value in subs]
#ship_position = [generate_coordinate(value,xVal) for value in ships]


#cost = np.array(sub_position,ship_position)
#print(cost)
#row_ind, col_ind = linear_sum_assignment(cost)
#print(row_ind)
#print(col_ind)
#print(cost[row_ind, col_ind].sum())

