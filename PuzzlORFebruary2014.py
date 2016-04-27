#PuzzlOR February 2014 Pizza Delivery

import math
import random

outputList = []
countval = 1
maxcountval = 10001
while countval < maxcountval:
    interArrivalTime = 0.1
    maxDeliveryTime = 60
    deliveryTime = random.uniform(20,60)
    pizzaOrders = random.expovariate(interArrivalTime)
    if deliveryTime <= maxDeliveryTime:    
        numOfDrivers = pizzaOrders
        outputList.append(numOfDrivers)
    countval+=1
print(math.ceil(sum(outputList)/len(outputList)))

#print(deliveryTime)
#print(pizzaOrders)
#print(orderDeliveryTime)



