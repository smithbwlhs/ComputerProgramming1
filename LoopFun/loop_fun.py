user_height = int(input("Enter a box height (between 3 and 10): "))
while user_height < 3 or user_height > 10:
    user_height = int(input("That number is out of bounds: Try Again: "))

width_lower_bound = user_height + 1
print("Enter a box width (between " + str(width_lower_bound) + " and 20): ", end='')
user_width = int(input())
while user_width < (user_height + 1) or user_width > 20:
    user_width = int(input("That number is out of bounds: Try again: "))

print("The integers from", user_height, "to", user_width, "are:")
print('\t', end='')
for i in range(user_height, user_width + 1):
    print(str(i) + " ", end='')

# average section
sum = 0
for i in range(user_height, user_width + 1):
    sum += i

average = sum / (user_width - user_height + 1)
print("\nand the average of those numbers is", average)

# box
empty_space = ' ' * (user_width - 2)
for i in range(user_width):
    print('*', end='')
print('')
for i in range(user_height):
    print('*' + empty_space + '*')
for i in range(user_width):
    print('*', end='')
print('')
# triangle printer

# pythonic way
for i in range(user_height + 1):
    print('**' * i)

# nested loops - for and while
for i in range(user_height + 1):
    j = 0
    while j < 2 * i:
        print('*', end='')
        j += 1
    print('')

# nested loops - for in a for loop
for i in range(user_height + 1):
    for j in range(2 * i):
        print('*', end='')
    print('')
