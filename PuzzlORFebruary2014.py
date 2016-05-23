#PuzzlOR February 2014 Pizza Delivery

import math
import random


def customerData():
    customerInterArrivalTime = 6 #hrs
    customerAverage = 1/customerInterArrivalTime
    customerVariance = math.pow(customerAverage,2)
    return [customerInterArrivalTime,customerAverage,customerVariance]

def PickupData():
    pickupDelivery = random.uniform(20,60) 
    pickupDeliveryAverage = (20+60)/2
    pickupDeliveryVariance = math.pow(60-20,2)/12
    return [pickupDelivery,pickupDeliveryAverage,pickupDeliveryVariance]
    
    
#assumption - a driver can only deliver one order per round trip

#How many drivers are needed in order to keep average delivery times under one hour?

countVal = 0
maxCountVal = 10000
while countVal < 10000:
    mandateDelivery = 60
    countVal+=1