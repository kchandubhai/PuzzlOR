# PuzzlOR June 2013 Self Driving Cars

def euclidean_distance(a,b):
    c = [math.pow(a[i] - b[i],2) for i in range(len(a))]
    return math.sqrt(sum(c))

def generate_coordinate(value,alist):
    tempList = []
    tempVal = value[0]
    tempNum = int(value[1])
    tempVal1 = int(alist.index(tempVal)) + 1
    tempList.extend([tempVal1,tempNum])
    return tempList

#find closest pick up
def find_next():



def main():
	area = [
	[,],
	[,],
	[,],
	[,],
	[,],
	[,],
	[,],
	[,],
	[,],
	[,]
	]

	#generate starting position

	#find next position

	#delete old destination

	#calculate distance and store the distance

main()