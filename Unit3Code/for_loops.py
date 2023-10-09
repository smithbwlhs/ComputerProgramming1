#print "Hello" 3 times

i = 0
while i < 3:
    print("Hello")
    i = i + 1

#alternative for when I know the number of times
#something runs

for i in range(3):
    print("Hello")

#prints 0 up to but not including 3
for i in range(3):
    print(i)

#prints 10 up to but not including 18
for i in range(10,18):
    print(i)

#prints 5 up to 20, adding 7 every time
for i in range(5,20,7):
    print(i)

num_runs = int(input("How many times should this run? "))
for i in range(num_runs):
    print("Run",i+1)

#for loops can keep a running tally

#average for 3 exams
sum = 0
for i in range(3):
    score = int(input("Enter a test score: "))
    sum = sum + score

average = sum / 3
print(average)

#average for n exams
sum = 0
num_exams = int(input("How many exams are you entering? "))
for i in range(num_exams):
    score = int(input("Enter a test score: "))
    sum = sum + score

average = sum / num_exams
print(average)