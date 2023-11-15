# while True:
#     try:
#         user_num = float(input("Enter a whole number: "))
#         print(int(user_num))
#         user_num2 = float(input("Give me another whole number: "))
#         print(int(user_num2))
#         print("The quotient is:", (user_num / user_num2))
#         break
#     except ValueError:
#         print("Enter whole numbers only.")
#     except ZeroDivisionError:
#         print("Don't enter 0")
#     except Exception as e:
#         print("You caused an error", e, "of type", type(e))

def celsius_to_fahrenheit(celsius):
    fahrenheit = 1.8*celsius+32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32)/1.8
    return celsius

####Test code####
while True:
    try:
        user_celsius = float(input("Enter a temp in C: "))
        print(celsius_to_fahrenheit(user_celsius))
        user_fahrenheit = float(input("Enter a temp in F: "))
        print(fahrenheit_to_celsius(user_fahrenheit))
        break
    except ValueError:
        print("Enter numbers only.")