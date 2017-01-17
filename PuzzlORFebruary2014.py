#PuzzlOR February 2014 Pizza Delivery

import math
import random
import timeit.Timer
import numpy as np
import scipy as sp

def calc_avg(alist):
    return sum(alist)/len(alist)




def main():
   deliveryTime = 60
   
   

if __name__ == "__main__":
    main()

#import math
#import random
#
#def calc_avg(alist):
#    return math.ceil(sum(alist)/len(alist))
#
#def customerData():
#    driverData = []
#    countVal = 0
#    maxCountVal = 60
#    mandateDelivery = 60
#    while countVal < maxCountVal:
#        orderInterArrivalTime = 6
#        orderArrival = math.ceil(random.expovariate(1/orderInterArrivalTime))
#        orderCount = 0
#        driverCount = 0
#        pickupDeliveryList = []
#        while orderCount < orderArrival:
#            pickupDelivery = math.ceil(random.uniform(19,60))
#            pickupDeliveryList.append(pickupDelivery)
#            if calc_avg(pickupDeliveryList) < mandateDelivery:
#                driverCount+=1
#            orderCount+=1
#        driverData.append(driverCount)
#        countVal+=1
#    return(calc_avg(driverData))
#
#
#def calc_val():
#    outputList = [customerData() for value in range(10000)]
#    print(calc_avg(outputList) + 1)
#calc_val()
