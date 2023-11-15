import math

def hyp_calc(a,b):
	try:
		return math.sqrt(pow(a,2)+pow(b,2))
	except ValueError:
		print("No negative numbers allowed")
	except TypeError:
		print("That's not a number")

print(hyp_calc(3,"-2"))