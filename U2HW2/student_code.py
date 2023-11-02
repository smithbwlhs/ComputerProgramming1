def triangleStudent(side1, side2, side3):
    """Student code here"""
    if side1 >= side2+side3 or side2 >= side1+side3 or side3 >= side2+side1:
        print("Thats not possible") 
    else:
        print("Yay! you made a triangle!")

#Exercise 2
def triangleSolution(a, b, c):
    sum1 = a + b
    sum2 = a + c
    sum3 = b + c

    if sum1 <= c:
        print("No")
    elif sum2 <= b:
        print("No")
    elif sum3 <= a:
        print("No")
    else:
        print("Yes")
