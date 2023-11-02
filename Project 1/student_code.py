import math
import time

def geometryFunStudent(length, sides):

    #length = int(input("whats your favorite number?: "))


    #Calculate 
        
        #Square
    square_area = length * length 
    square_perimeter = length + length + length + length

        #Circle
    circle_circumference = round((length * 3.14),3)
    circle_area = 3.14 * ((length/2)**2)

        #Triangle
    triangle_area = round((math.sqrt(3)/4)*(length**2),1)
    triangle_perimeter = length * 3

    #Show n Tell

        #Square
    print("a square with a side length of", str(length)) 
    print("\thas an area of", str(square_area))
    print("\tand a perimeter of", str(square_perimeter))

        #Circle
    print("a circle with a radius of", str(length))
    print("\thas a circumference of", str(circle_circumference))
    print("\thas an area of", str(circle_area))

        #Triangle
    print("a triangle with a side length of",str(length))
    print("\thas a area of",str(triangle_area))
    print("\tand a perimeter of", str(triangle_perimeter))