def triangleStudent(stick_1  , stick_2, stick_3):
    """Student code here"""


    if(stick_1 > stick_2 and stick_1 > stick_3):
        if(stick_1 < stick_2 + stick_3):
            print("Yes")
        else:
            print("No")
    elif(stick_2 > stick_1 and stick_2 > stick_3):
        if(stick_2 < stick_1 + stick_3):
            print("Yes")
        else:
            print("No")
    elif(stick_3 < stick_1 + stick_2):
        print("Yes")
    else:
        print("No")

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
