#PuzzlOR February 2014 Pizza Delivery

import math
import random

def customerData():  
    driverData = []
    countVal = 0
    maxCountVal = 100
    while countVal < maxCountVal:
        mandateDelivery = 60
        customerInterArrivalTime = int(math.ceil(random.expovariate(0.1)))
        customerCount = 0
        driverCount = 0
        while customerCount < customerInterArrivalTime:
            pickupDelivery = int(math.ceil(random.uniform(20,60)))
            if pickupDelivery <= mandateDelivery:
                driverCount+=1
            customerCount+=1
        driverData.append(driverCount)
        countVal+=1
    print(round(sum(driverData)/maxCountVal,0))

customerData()

