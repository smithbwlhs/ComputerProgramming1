a = int(input())
b = int(input())
c = int(input())

sum1 = a + b
sum2 = a + c
sum3 = b + c

if sum1 <= c:
	print("No")
elif sum2 <= b:
	print("No")
elif sum3 <= a:
	print("No")
else:
	print("Yes")