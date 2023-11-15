
while(True):
    try:
        user_num = int(input("Enter: "))
        num = 10/user_num
        break
    except ValueError:
        print("Enter a float.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")

print(num)
#################################################

# This function takes a temperature
# in Celsius and converts it to
# Fahrenheit.
def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32

# This function takes a temperature
# in Fahrenheit and converts it to
# Celsius.
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

print("0C In F: " + str(celsius_to_fahrenheit(0)))
print("100C In F: " + str(celsius_to_fahrenheit(100)))
print("40F In C: " + str(fahrenheit_to_celsius(40)))
print("80F In C: " + str(fahrenheit_to_celsius(80)))

###Part 2###

# This function takes a temperature
# in Celcius and converts it to
# Farenheit.
def celcius_to_farenheit(celcius):
    return celcius * 1.8 + 32

# This function takes a temperature
# in Farenheit and converts it to
# Celcius.
def farenheit_to_celcius(farenheit):
    return (farenheit - 32) / 1.8

try:
    c = float(input("Enter a temp in C: "))
    print("In F: " + str(celcius_to_farenheit(c)))
    
    f = float(input("Enter a temp in F: "))
    print("In C: " + str(farenheit_to_celcius(f)))
except ValueError:
    print("You must enter a float!")


####Part 3#####
def retrieve_positive_number():
    while True:
        try:
            number = int(input("Enter a positive number: "))
            if number > 0:
                return number
            print("The number must be positive!")
        except ValueError:
            print("That wasn't a number!")

print(retrieve_positive_number())