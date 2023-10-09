import math
import time

def geometryFunStudent(length, sides):
    PI = 3.1416
    import math

    #length = int(input("Enter a whole number: "))

    # Square
    print("\nSquare side length is: ", length)
    square_area = length * length
    print("\tSquare area: ", square_area)
    square_perimeter = length * 4
    print("\tSquare perimeter: ", square_perimeter)

    # Circle
    print("Circle diameter: ", length)
    circle_radius = length / 2
    print("\tCircle radius: ", circle_radius)
    circle_circumference = circle_radius * PI * 2
    print("\tCircle circumference: ", round(circle_circumference, 3))
    circle_area = pow(circle_radius, 2) * PI
    print("\tCircle area: ", round(circle_area, 3))

    # Equilateral Triangle
    print("Equilateral Triangle Side length is: ", length)
    equ_tri_area = math.sqrt(3) / 4 * pow(length, 2)
    print("\tTriangle area: ", round(equ_tri_area, 3))
    equ_tri_perimeter = length * 3
    print("\tTriangle perimeter: ", equ_tri_perimeter)
