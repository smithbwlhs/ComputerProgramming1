'''
Name: Aarik Abrahamsen
Date:9/7-/23
Assingment:Geometry_Fun - Project 1
Desciption:This code is to be able tht use the inputted length value of a square and calculate the area and perimeter off that entered value
Another piece of code is to be able to be given the length of the diameter of a circle and calculate the radius, circumference, and area of the circle.
The third piece of code with be able to be given the side length of a equilateral triangle and calculate the area and perimeter of that triangle.
'''
import math

# ask user to input the length of a square and store it in square_length.
user_number = (float(input("Enter a whole number: ")))
# Then calculate perimeter and area of a square whose side length is the entered number and print the area and perimeter
square_area = math.pow(user_number, 2)
square_perimeter = user_number * 4
print("\tA square with the length of: ", round(user_number, 3))
print("\tthe square has a perimeter of: ", round(square_perimeter, 3))
print("\tthe square has an area of: ", round(square_area, 3))
# The radius, circumference, and area of a circle whose diameter is the entered number
PI = 3.1416
circle_radius = user_number / 2
circle_area = 2 * PI * circle_radius
circle_circumference = 2 * PI * circle_radius
print("\tA circle with the dimeter of: ", round(user_number, 3))
print("\tthe circle has a radius of: ", round(circle_radius, 3))
print("\tthe circle has a circumference of: ", round(circle_circumference, 3))
print("\tthe circle has an area of: ", round(square_area, 3))

# The perimeter and area of an equilateral triangle whose side length is equal to the entered number.
triangle_height = (math.sqrt(3) * user_number) / 2
triangle_area = (math.sqrt(3) / 4) * (math.pow(user_number, 2))
triangle_perimeter = math.pow(user_number, 3)
print("\t A equilateral triangle with the side length of: ", round(user_number, 3))
print("\t the triangle has a height of: ", round(triangle_height, 3))
print("\tthe triangle has a perimeter of: ", round(square_perimeter, 3))
print("\t the triangle has an area of: ", round(square_area, 3))

# extra credit
polygon_sides = (float(input("\tEnter a whole number for how many sides your regular polygon has: ")))
polygon_p = user_number * polygon_sides
polygon_inside_angles = 360 / polygon_sides
polygon_apothem = user_number / 2 * math.tan(polygon_inside_angles / 2)
polygon_a = (polygon_apothem * polygon_p) / 2
print("\tYour regular polygon has a perimeter of: ", polygon_p, "\tYour regular polygon also has an area of:",
      round(polygon_a, 3))