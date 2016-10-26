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

def calc_score(alist,blist):
    score = 0
    for a,b in zip(alist,blist):
        score+=euclidean_distance(a,b)
    return score
    
    

def euclidean_distance(a,b):
    c = [math.pow(a[i] - b[i],2) for i in range(len(b))]
    return round(math.sqrt(sum(c)),2)

def main():
    minScore = [100]
    subs = [[1, 1], [2, 2], [2, 6], [4, 2], [4, 3], 
            [4, 7], [6, 1], [7, 1], [7, 4], [9, 1], 
            [9, 5], [9, 7], [10, 2], [10, 3], [10, 6]]    
    ships = [[2, 1], [3, 4], [4, 9], [6, 1], [6, 2], 
             [6, 3], [6, 5], [6, 8], [7, 5], [7, 6], [7, 8], 
                [8, 7], [10, 1], [10, 4], [10, 1]]  
 
   
    
    for sub in itertools.permutations(subs):
        currentScore = calc_score(sub,ships)
        if  currentScore < minScore:
            minScore[0] = currentScore
    print(minScore)
            
    
   
  
        

if __name__ == "__main__": 
    main()          
#site_location = np.array([[4,6],[1,8],[2,3],[4,10],[5,2],[7,3],[7,6],[7,8],
#                              [8,1],[8,4],[9,7]])             
#site_score = [0,3,3,5,4,5,4,2,2,1,1]
#site_euclidean_distance = (squareform(pdist(site_location,"euclidean")))
#print(site_euclidean_distance)
#sub_position = [generate_coordinate(value,xVal) for value in subs]
#ship_position = [generate_coordinate(value,xVal) for value in ships]


#cost = np.array(sub_position,ship_position)
#print(cost)
#row_ind, col_ind = linear_sum_assignment(cost)
#print(row_ind)
#print(col_ind)
#print(cost[row_ind, col_ind].sum())

