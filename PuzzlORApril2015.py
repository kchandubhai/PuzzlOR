# PuzzlOR April 2015 - Desert Island
import random
import math
import sys

def main():
	
	try:
		WATER = {"COMPLETION":0.2,"DEATH":0.15}
		SHELTER = {"COMPLETION":0.15,"DEATH":0.10}
		FOOD = {"COMPLETION":0.1,"DEATH":0.05}
		outcome = []
		day = 0
		maxDay = 100

		while day < maxDay:
			event_outcome = True
			survival = 0
			death = 0
			water_complete = 0
			shelter_complete = 0
			food_complete = 0
			while(event_outcome):
				water_task = random.uniform(0.0,1.0)
				food_task = random.uniform(0.0,1.0)
				shelter_task = random.uniform(0.0,1.0)
				if(survival >= 1):
					outcome.append("survival")
					event_outcome = False
					break
				if(death >= 1):
					outcome.append("death")
					event_outcome = False
					break
				if (water_task > WATER["COMPLETION"]):
					if shelter_task > SHELTER["COMPLETION"]:
						if(food_task) > FOOD["COMPLETION"]:
							survival+=water_task + shelter_task + food_task
				elif (water_task <= WATER["COMPLETION"]):
					death+= WATER["DEATH"] + SHELTER["DEATH"]+FOOD["DEATH"]
				elif (water_task > WATER["COMPLETION"]):
					if shelter_task <= SHELTER["COMPLETION"]:
						death+=SHELTER["DEATH"]+FOOD["DEATH"]
						survival+= water_task
				elif (water_task > WATER["COMPLETION"]):
					if shelter_task > SHELTER["COMPLETION"]:
						if(food_task) <= FOOD["COMPLETION"]:
							death+=FOOD["DEATH"]
							survival+=water_task + shelter_task


				

			day+=1
		surv_count = 0
		for item in outcome: 
			if item == "survival":
				surv_count+=1
		print(surv_count)
			#if water_task <= WATER["COMPLETION"] or water_complete == false:
			#	death+= WATER["DEATH"] + SHELTER["DEATH"]+FOOD["DEATH"]
			#else:
			#	water_complete = true



	except:
		e = sys.exc_info()
		print(e)
		sys.exit(1)


if __name__ == "__main__":
    main()


"""
		#do something
		# for x in range(0, 9):
		# 	if (random.uniform(0.0, 1.0) < 0.416667):
		# 		print ("A wins")
	 #    	else:
	 #        	print ("B wins")
"""