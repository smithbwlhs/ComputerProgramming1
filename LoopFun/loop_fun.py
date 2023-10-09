user_height = int(input("Enter a box height (between 3 and 10): "))
while user_height < 3 or user_height > 10:
    user_height = int(input("That number is out of bounds: Try Again: "))


user_width = int(input("Enter a box width (between 6 and 20): "))
while user_width < 6 or user_width > 20:
    user_width= int(input("That number is out of bounds: Try again: "))

print("The integers from",user_height,"to",user_width,"are:")
print('\t',end='')
for i in range(user_height,user_width):
    print(str(i) + " ",end='')

#average section
sum = 0
for i in range(user_height,user_width+1):
    sum+=i
average = sum / (user_width - user_height + 1)
print("and the average of those numbers is",average)

#box
empty_space = ' '*(user_width - 2)
for i in range(user_width):
    print('*',end='')
print('')
for i in range(user_height):
    print('*'+empty_space+'*')
for i in range(user_width):
    print('*',end='')

#triangle printer

#pythonic way
for i in range(user_height+1):
    print('**'*i)

#nested loops - for and while
for i in range(user_height+1):
    j = 0
    while j < 2*i:
        print('*',end = '')
        j += 1
    print('')

#nested loops - for in a for loop
for i in range(user_height+1):
    for j in range(2*i):
        print('*',end='')
    print('')