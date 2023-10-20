def student_solution(favorite_integer,favorite_character):
    """
    Name: Luke Tye
    Date: 9/25/23
    Description: Ask user for favorite integer and character and print out a variety of information
    regarding those numbers.

    """
    #favorite_integer = int(input("What's your favorite integer? "))
    if favorite_integer < 0:
        print("\tThis integer is negative.")
    else:
        print("\tThis integer is positive")

    if 10 < favorite_integer <= 100:
        print("\tThis integer is greater than 10")
    elif 100 < favorite_integer <= 1000:
        print("\tThis integer is greater than 100")
    elif favorite_integer > 1000:
        print("\tThis number is greater than 1000")
    else:
        print("\tThis number is smaller than 10")

    if favorite_integer % 2 == 0:
        print("\tThis number is even.")
    else:
        print("\tThis number is odd.")

    match favorite_integer:
        case 2:
            print("\tThis is the Noble Gas Helium!")
        case 10:
            print("\tThis is the Noble Gas Neon!")
        case 18:
            print("\tThis is the Noble Gas Argon!")
        case 36:
            print("\tThis is the Noble Gas Krypton!")
        case 54:
            print("\tThis is the Noble Gas Xenon!")
        case 86:
            print("\tThis is the Noble Gas Radon!")
        case 118:
            print("\tThis is the Noble Gas Oganesson!")
        case _:
            print("\tThis is not one of the Noble Gasses.")

    #favorite_character = input("Give me your favorite character ")
    print(favorite_character)

    if favorite_character.isdigit():
        print("\tYour character is a numeric digit.")
    elif favorite_character.islower():
        print("\tYour character is a lowercase letter")
        if favorite_character in "aeiou":
            print("\tIt's a lowercase vowel")
        else:
            print("\tIt's a consonant.")
    elif favorite_character.isupper():
        print("\tYour character is an uppercase letter")
        if favorite_character in "AEIOU":
            print("\tIt's an uppercase vowel")
        else:
            print("\tIt's a consonant.")
    else:
        print("\tInvalid input.")

    ascii_value = ord(favorite_character)
    print("\tThe ASCII value of favorite_character is " + str(ascii_value))

    if favorite_character.islower() or favorite_character.isupper():
        letter_position = ord(favorite_character) - ord("A") + 1
        if letter_position == 1:
            suffix = "st"
        elif letter_position == 2:
            suffix = "nd"
        elif letter_position == 3:
            suffix = "rd"
        else:
            suffix = "th"
        print(
            "\tAnd it is the " + str(letter_position) + suffix + " letter of the alphabet."
        )