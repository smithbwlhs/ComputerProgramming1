"""
Name: Brandon Smith
Date: 10/12/23
File name: nested_loops.py
Description: Lesson on nested loops
"""
##write a while loop that prints the numbers 1-10 on a single line
#with spaces inbetween
number = 1
while number <= 10:
    print(number, end = " ")
    number = number + 1

print('')
#write a for loop that prints the numbers 1-10 on a single line
#with spaces inbetween

for i in range(1,11):
    print(i, end = " ")

print('')
#write a for loop that prints "elephant" twelve times
#each on a new line

for i in range(6):
    for j in range(2):
        print("*", end = ' ')
    print(' ')
print('\n')
num = 0
while num < 6:
    for j in range(2):
        print("*",end = ' ')
    num = num + 1
    print('')
    