import math

PI = 3.14159

input_number = int(input("Please enter a whole number: "))
number_of_sides = int(input("Number of sides: "))

square_area = pow(input_number,2)
square_perimeter = 4 * input_number

circle_radius = input_number / 2
circle_circumference = 2 * PI * circle_radius
circle_area = PI * pow(circle_radius,2)

equilateral_triangle_perimeter = 3 * input_number
equilateral_triangle_area = (math.sqrt(3) / 4) * pow(input_number,2)

n_sided_perimeter = input_number * number_of_sides
apothem = input_number / (2*math.tan(PI/number_of_sides))
n_sided_area = 0.5 * n_sided_perimeter * apothem

print("A square with a side length of",input_number)
print("\thas a perimeter of",square_perimeter)
print("\thas an area of", square_area)

print("A circle with a diameter of",input_number)
print("\thas a radius of",circle_radius)
print("\thas a circumference of",round(circle_circumference,3))
print("\thas an area of",round(circle_area,3))

print("An equilateral triangle with side length of",input_number)
print("\thas a perimeter of",equilateral_triangle_perimeter)
print("\thas an area of",round(equilateral_triangle_area,3))

print("A regular polygon with",number_of_sides,"sides and a side length of",input_number)
print("\thas a perimeter of",n_sided_perimeter)
print("\thas an area of",round(n_sided_area,3))