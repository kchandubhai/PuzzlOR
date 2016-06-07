#PuzzlOR August 2011 Logical Hospital



import math
import random

test = [1, 2, 1]

def calc_time(patientData,station):
    for patient in patientData:
        c

print(calc_time(test))

def main():
    count = 0
    maxcount = 10000
    timelist = []
    while count < maxcount:
        #Patient Arrival
        patientInterArrival = 6
        numPatients = math.ceil(random.normalvariate(patientInterArrival,2))
        patientScreen = [0,0,0]

        #Patient Assignment
        for value in range(1,numPatients):
            patientType =  round(random.random()*100,2)
            if patientType <= 33.30:
                patientScreen[0]+=1
            elif patientType <= 66.60:
                patientScreen[1]+=1
            else:
                patientScreen[2]+=1

        #Prescreening
        patientER = []
        patientER.append(math.ceil(patientScreen[0] * 0.8))
        patientER.append(math.ceil(patientScreen[1] * 0.5))
        patientER.append(math.ceil(patientScreen[2] * 0.2))

        #ER station assignment
        station = 2
        #print(calc_time(patientER,station))
        timelist.append(calc_time(patientER,station))
        count+=1



if __name__ == '__main__':
    main()


