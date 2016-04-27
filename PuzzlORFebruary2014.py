#PuzzlOR February 2014 Pizza Delivery

import math
import random
interArrivalTime = 0.1
deliveryTime = random.uniform(20,60)
pizzaOrders = random.expovariate(1/interArrivalTime)
orderDeliveryTime = random.normalvariate(60,40/math.sqrt(12))




