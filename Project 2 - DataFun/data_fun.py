"""
Author: Brandon Smith
Date: 9/21/23
Assignment: DataFun Key
Description: The first part of the program will do the following: Get the user’s favorite integer. 
Print out if it’s positive or negative (consider 0 as positive)
Print out if it’s greater than 10, 100, or 1000 (only print the highest one it’s greater than).
Print out if it’s odd or even
If the number is the atomic number of one of the 7 noble gases, it should print out the name of 
the noble gas corresponding to that atomic number. If the number is NOT the atomic number of one 
of the 7 noble gases, it should print a message stating that. (use match case for this)

The second part of the program will do the following: Get the user’s favorite character.
Print out if it’s a numeric digit, lowercase letter, or uppercase letter. If it’s a letter, prints 
out if it’s a vowel or not 
Print out the ascii value of the character (hint: research the ord() method)
If it’s a letter, prints out where it is in the alphabet (A=1st, B=2nd, C=3rd, etc.),
and print the proper suffix (st, nd, rd, th, etc.)
"""

def student_solution(favorite_integer,favorite_character):
    '''enter student solution'''

def my_solution(favorite_integer, favorite_character):
    #favorite_integer = int(input("What is your favorite integer? "))

    if favorite_integer >= 0:
        print("\t" + str(favorite_integer) + " is a positive number,")
    else:
        print("\tit is a negative number,")

    if favorite_integer > 1000:
        print("\tit is greater than 1000,")
    elif favorite_integer > 100:
        print("\tit is greater than 100,")
    elif favorite_integer > 10:
        print("\tit is greater than 10,")

    if favorite_integer % 2 == 0:
        print("\tit is even,")
    else:
        print("\tit is odd,")

    match favorite_integer:
        case 2|10|18|36|54|86|118:
            print("\tand it is the atomic number of a noble gas.")
        case _:
            print("\tand it is not the atomic number of a noble gas.")

    #favorite_character = input("What is your favorite character? ")

    if favorite_character.isdigit():
        print("\t" + favorite_character + " is a numeric digit,")

    if favorite_character.isupper():
        print("\t" + favorite_character + " is an upper case letter,")

    if favorite_character.islower():
        print("\t" + favorite_character + " is a lower case letter,")


    match favorite_character.lower():
        case "a"|"e"|"i"|"o"|"u":
            print("\tit is a vowel,")
        case _:
            print("\tit is not a vowel,")

    ascii_value = ord(favorite_character)
    print("\tits ASCII value is",ascii_value)

    if favorite_character.isalpha():
        match favorite_character.lower():
            case "a":
                print("\tand it's the 1st letter of the alphabet")
            case "b":
                print("\tand it's the 2nd letter of the alphabet")
            case "c":
                print("\tand it's the 3rd letter of the alphabet")
            case _:
                print("\tand it's the " + str(ascii_value-64) + "th letter of the alphabet")


