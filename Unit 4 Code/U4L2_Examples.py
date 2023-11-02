'''Example 1 - write a function that takes two numbers and 
returns the floor division (//) of them'''

def floor_division(a,b):
    return a//b



'''Example 2 - Write a program that will calculate and 
print the perimeter of a rectangle where its length and
width is given by the user.

To compute the perimeter, write a function named 
calculate_perimeter that takes two parameters, width and
height. The parameters should be given a default value 
of 10.

If the user enters a length or width value of 0 or less, call 
calculate_perimeter and use the default value. 
Otherwise, use the length value given as the parameter value.'''

def calculate_perimeter(width = 10, height = 10):
    return 2*(width+height)


####Run Functions Here###
print(floor_division(38,7))
print(38/7)
print(floor_division(50,9))
print(50/9)

###

print("Enter width: ")
user_width = int(input())
print("Enter height: ")
user_height = int(input())

if user_width <=0 or user_height <=0:
    perimeter = calculate_perimeter()
else:
    perimeter = calculate_perimeter(user_width, user_height)

print(perimeter)