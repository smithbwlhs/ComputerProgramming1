'''
ChatGPT Version
With EC
'''

import math

PI = 3.1416

def main():
    # Ask the user for a positive whole number
    while True:
        try:
            num = int(input("Please enter a whole number: "))
            if num > 0:
                break
            else:
                print("Please enter a positive whole number.")
        except ValueError:
            print("That's not a valid number. Please try again.")
    
    # Ask the user for a number of sides for a regular polygon
    while True:
        try:
            sides = int(input("Please enter a number of sides for a regular polygon (at least 3): "))
            if sides >= 3:
                break
            else:
                print("Please enter a number of sides greater than or equal to 3.")
        except ValueError:
            print("That's not a valid number. Please try again.")

    # Calculations for square
    square_perimeter = 4 * num
    square_area = pow(num, 2)

    # Calculations for circle
    circle_radius = num / 2.0
    circle_circumference = PI * num
    circle_area = PI * pow(circle_radius, 2)

    # Calculations for equilateral triangle
    triangle_perimeter = 3 * num
    triangle_area = (math.sqrt(3) / 4) * pow(num, 2)

    # Calculations for regular polygon
    polygon_perimeter = sides * num
    polygon_area = (sides * pow(num, 2)) / (4 * math.tan(PI / sides))

    # Displaying results
    print("\nA square with side length of", num)
    print("\thas a perimeter of", square_perimeter)
    print("\thas an area of", square_area)

    print("\nA circle with a diameter of", num)
    print("\thas a radius of {:.3f}".format(circle_radius))
    print("\thas a circumference of {:.3f}".format(circle_circumference))
    print("\thas an area of {:.3f}".format(circle_area))

    print("\nAn equilateral triangle with side length of", num)
    print("\thas a perimeter of", triangle_perimeter)
    print("\thas an area of {:.3f}".format(triangle_area))

    print("\nA regular polygon with side length of", num, "and", sides, "sides")
    print("\thas a perimeter of", polygon_perimeter)
    print("\thas an area of {:.3f}".format(polygon_area))

if __name__ == '__main__':
    main()
