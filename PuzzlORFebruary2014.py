#PuzzlOR February 2014 Pizza Delivery

import math
import random

def customerData():
    driverData = []
    countVal = 0
    maxCountVal = 10000
    while countVal < maxCountVal:
        mandateDelivery = 60
        orderInterArrivalTime = 6
        orderArrival = int(math.ceil(random.expovariate(1/orderInterArrivalTime)))
        orderCount = 0
        driverCount = 0
        while orderCount < orderArrival:
            pickupDelivery = math.ceil(random.uniform(20,61))
            if pickupDelivery < mandateDelivery:
                driverCount+=1
            orderCount+=1
        driverData.append(driverCount)
        countVal+=1
    print(math.ceil(round(sum(driverData)/maxCountVal,0)))

customerData()
