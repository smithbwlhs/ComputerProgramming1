total_tests = int(input("Number of tests: "))

score = 0
total_score = 0

for i in range(total_tests):
	score = int(input("Test score " + str(i + 1) + ": "))
	#total_score = total_score + score
	total_score += score


average = total_score / total_tests

print(average)