import math

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius*1.8) +32
    return(fahrenheit)

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32)/1.8
    return(celsius)


try:
    celsius_temperature = float(input("What is the temp in celsius?: "))
    fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
    print(f"{celsius_temperature}°C is equal to {fahrenheit_temperature}°F")

    fahrenheit_temperature = float(input("What is the temp in Fahrenheit?: "))
    celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)
    print(f"{fahrenheit_temperature}°F is equal to {celsius_temperature}°C")
    
except ValueError:
    print("please enter a valid tempature!")




# print(celsius_to_fahrenheit(0))
# print(celsius_to_fahrenheit(100))
# print(fahrenheit_to_celsius(40))
# print(fahrenheit_to_celsius(80))