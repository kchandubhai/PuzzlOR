# PuzzlOR February 2008 - decision trees

import sys
import math

COLD = {"Cost_treated":0,"Cost_untreated":500,"Prob_occurrence":0.5,"Prob_test":0.5,"Prob_test_correct":0.8,"Prob_test_incorrect":0.1}
FLU = {"Cost_treated":0,"Cost_untreated":800,"Prob_occurrence":0.2,"Prob_test":0.2,"Prob_test_correct":0.9,"Prob_test_incorrect":0.05}
BACTERIA = {"Cost_treated":200,"Cost_untreated":1200,"Prob_occurrence":0.3,"Prob_test":0.3,"Prob_test_correct":0.95,"Prob_test_incorrect":0.025}
DOCTOR_TEST_COST = 200
PENICILLIN_COST = 50

def main():
	try:
		
		# Pencillin expense is comprised of probability of occurrence of each ailment multipled by the corresponding costs. For Cold and Flu, the costs are for being untreated as Pencillin won't treat them. For Bacteria, it would be cost of being treated correctly as pencillin dosage would cure the ailment in 2 days.
		
		PENICILLIN_EXPENSE = PENICILLIN_COST + COLD["Prob_occurrence"]*COLD["Cost_untreated"]+ FLU["Prob_occurrence"]*FLU["Cost_untreated"]+BACTERIA["Prob_occurrence"]*BACTERIA["Cost_treated"]
		
		print("PENICILLIN_EXPENSE : {}").format(PENICILLIN_EXPENSE)
		
		# Each ailment cost is comprised of three probabilities. 1) Probability of ailment occurence 2) Probability of Test result output for that ailment 3) Probability of test result being accurate. Multiplying all three with the cost of treated (where ailment occurrence & Test result ouptut are for the same ailment) and cost of untreated (where ailment occurrence and test result output are for different ailment) gives total ailment cost
		
		COLD_TEST_COST = COLD["Prob_occurrence"]*(COLD["Prob_test"]*COLD["Prob_test_correct"]*COLD["Cost_treated"]+FLU["Prob_test"]*FLU["Prob_test_incorrect"]*COLD["Cost_untreated"]+BACTERIA["Prob_test"]*BACTERIA["Prob_test_incorrect"]*COLD["Cost_untreated"])

		print("COLD_TEST_COST : {}").format(COLD_TEST_COST)
		
		FLU_TEST_COST = FLU["Prob_occurrence"]*(COLD["Prob_test"]*COLD["Prob_test_incorrect"]*FLU["Cost_untreated"]+FLU["Prob_test"]*FLU["Prob_test_correct"]*FLU["Cost_treated"]+BACTERIA["Prob_test"]*BACTERIA["Prob_test_incorrect"]*FLU["Cost_untreated"])
		
		print("FLU_TEST_COST : {}").format(FLU_TEST_COST)
		
		BACTERIA_TEST_COST = BACTERIA["Prob_occurrence"]*(COLD["Prob_test"]*COLD["Prob_test_incorrect"]*BACTERIA["Cost_untreated"]+FLU["Prob_test"]*FLU["Prob_test_incorrect"]*BACTERIA["Cost_untreated"]+BACTERIA["Prob_test"]*BACTERIA["Prob_test_correct"]*BACTERIA["Cost_treated"])        
        
		print("BACTERIA_TEST_COST : {}").format(BACTERIA_TEST_COST)
		
		#Adding the doctor & test cost with all the ailment costs gives the expense of visiting doctor & getting the test done
		DOCTOR_TEST_EXPENSE = DOCTOR_TEST_COST + COLD_TEST_COST+ FLU_TEST_COST + BACTERIA_TEST_COST
		
		print("DOCTOR_TEST_EXPENSE : {}").format(DOCTOR_TEST_EXPENSE)
				
		if (DOCTOR_TEST_EXPENSE <= PENICILLIN_EXPENSE):
			print("Yes, go to the doctor and have a test done")
		else:
			print("No, don't get the test and take pencillin prescription")
	except:
		e = sys.exc_info()
		print(e)
		sys.exit()


if __name__ == "__main__":
	main()
