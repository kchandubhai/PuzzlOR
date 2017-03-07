#PuzzlOR February 2017 Any Port In A Storm
#minimum possible total distance traveled by all boats
import sys


def main():
	try:
		cluster_check = [0,0,0]
		distance = 0
		dock_size = [4,7,9]
		#ships, distance
		cluster_info = {
			1:[8,[1,3,2]],
			2:[5,[2,2,1]],
			3:[7,[3,2,1]]
		}


		
	except:
		e = sys.exc_info()
		print(e)
		sys.exit()

if __name__ == "__main__":
	main()


"""
#PuzzlOR February 2017 Any Port In A Storm
#minimum possible total distance traveled by all boats
import sys


def main():
	try:
		dockSize =  [4,7,9]
		clusterSize = [8,5,7]

		#cluster distance w.r.t docks
		cluster1distance = [1,2,3]
		cluster2distance = [2,1,2]
		cluster3distance = [3,2,1]

		distance  = 0
		

		#initial cluster assignment
		clusterCheck  = [clusterSize[i] - dockSize[i] for i in range(len(clusterSize))]

		positionData = []
		count = 0
		for check in clusterCheck:
			if check < 0:
				positionData.append(count)
			count+=1
		
		distance = clusterSize[positionData[0]] + clusterSize[positionData[1]] + clusterSize[0]-4
		+ 2*(cluster1distance[positionData[0]] + cluster1distance[positionData[1]])


		print distance
	except:
		e = sys.exc_info()
		print(e)
		sys.exit()

if __name__ == "__main__":
	main()

"""