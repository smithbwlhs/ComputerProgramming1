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

#make a 5x5 multiplication table
# 1 2  3  4  5
# 2 4  6  8  10
# 3 6  9  12 15
# 4 8  12 16 20
# 5 10 15 20 25

for row in range(1,6):
    for column in range(1,6):
        print(row * column, end = '\t')
    print('')    