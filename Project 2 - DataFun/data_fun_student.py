def student_solution(favorite_integer,favorite_character):
    '''
    Name:Koleton Meir
    Date:09/25/23
    Assignment:Project 2
    '''
    #favorite_integer = int(input("What is your favorite integer: "))
    even = favorite_integer % 2
    if favorite_integer >= 0:
        print(favorite_integer, "is a positive number,")
    if favorite_integer < 0:
        print(favorite_integer, "is a negative number,")
    elif favorite_integer > 1000:
        print("it is greater than 1000,")
    elif favorite_integer > 100:
        print("it is greater than 100,")
    elif favorite_integer > 10:
        print("it is greater than 10,")

    if favorite_integer % 2 == 0:
        print("it is even,")
    else:
        print("it is odd,")

    if favorite_integer == 118:
        print("and it's the atomic number of the noble gas Organesson.")
    elif favorite_integer == 86:
        print("and it's the atomic number of the noble gas Radon.")
    elif favorite_integer == 54:
        print("and it's the atomic number of the noble gas Xenom.")
    elif favorite_integer == 36:
        print("and it's the atomic number of the noble gas Krypton.")
    elif favorite_integer == 18:
        print("and it's the atomic number of the noble gas Argon.")
    elif favorite_integer == 10:
        print("and it's the atomic number of the noble gas Neon.")
    elif favorite_integer == 2:
        print("and it's the atomic number of the noble gas Helium.")
    else:
        print("and it is not the atomic number of a noble gas.")

    #favorite_character = input("What is your favorite character?")

    if favorite_character.isdigit():
        print(favorite_character, "is a numeric digit")
    elif favorite_character.isupper():
        print(favorite_character, "is an uppercase letter")
        if favorite_character.lower == "a" or favorite_character.lower == "e" or favorite_character.lower == "i" or favorite_character.lower == "o" or favorite_character.lower == "u":
            print(favorite_character, "is a vowel")
        else:
            print(favorite_character, "is not a vowel")
    elif favorite_character.islower():
        print(favorite_character, "is a lowercase letter")
        if favorite_character.lower == "a" or favorite_character.lower == "e" or favorite_character.lower == "i" or favorite_character.lower == "o" or favorite_character.lower == "u":
            print("it is a vowel,")
        else:
            print("it is not a vowel,")
    ####if statement to check if a e i o u .lower

    if ord(favorite_character) == 0:
        print("it's ASCII value is NUL")
    if ord(favorite_character) == 1:
        print("it's ASCII value is SOH")
    if ord(favorite_character) == 2:
        print("it's ASCII value is STX")
    if ord(favorite_character) == 3:
        print("it's ASCII value is ETX")
    if ord(favorite_character) == 4:
        print("it's ASCII value is EOT")
    if ord(favorite_character) == 5:
        print("it's ASCII value is ENQ")
    if ord(favorite_character) == 6:
        print("it's ASCII value is ACK")
    if ord(favorite_character) == 7:
        print("it's ASCII value is BEL")
    if ord(favorite_character) == 8:
        print("it's ASCII value is BS")
    if ord(favorite_character) == 9:
        print("it's ASCII value is TAB")
    if ord(favorite_character) == 10:
        print("it's ASCII value is LF")
    if ord(favorite_character) == 11:
        print("it's ASCII value is VT")
    if ord(favorite_character) == 12:
        print("it's ASCII value is FF")
    if ord(favorite_character) == 13:
        print("it's ASCII value is CR")
    if ord(favorite_character) == 14:
        print("it's ASCII value is SO")
    if ord(favorite_character) == 15:
        print("it's ASCII value is SI")
    if ord(favorite_character) == 16:
        print("it's ASCII value is DLE")
    if ord(favorite_character) == 17:
        print("it's ASCII value is DC1")
    if ord(favorite_character) == 18:
        print("it's ASCII value is DC2")
    if ord(favorite_character) == 19:
        print("it's ASCII value is DC3")
    if ord(favorite_character) == 20:
        print("it's ASCII value is DC4")
    if ord(favorite_character) == 21:
        print("it's ASCII value is NAK")
    if ord(favorite_character) == 22:
        print("it's ASCII value is SYN")
    if ord(favorite_character) == 23:
        print("it's ASCII value is ETB")
    if ord(favorite_character) == 24:
        print("it's ASCII value is CAN")
    if ord(favorite_character) == 25:
        print("it's ASCII value is EM")
    if ord(favorite_character) == 26:
        print("it's ASCII value is SUB")
    if ord(favorite_character) == 27:
        print("it's ASCII value is ESC")
    if ord(favorite_character) == 28:
        print("it's ASCII value is FS")
    if ord(favorite_character) == 29:
        print("it's ASCII value is GS")
    if ord(favorite_character) == 30:
        print("it's ASCII value is RS")
    if ord(favorite_character) == 31:
        print("it's ASCII value is US")
    if ord(favorite_character) == 32:
        print("it's ASCII value is SPACE")
    if ord(favorite_character) == 33:
        print("it's ASCII value is", ord("!"))
    if ord(favorite_character) == 34:
        print("it's ASCII value is", ord("\\"))
    if ord(favorite_character) == 35:
        print("it's ASCII value is", ord("#"))
    if ord(favorite_character) == 36:
        print("it's ASCII value is", ord("$"))
    if ord(favorite_character) == 37:
        print("it's ASCII value is", ord("%"))
    if ord(favorite_character) == 38:
        print("it's ASCII value is", ord("&"))
    if ord(favorite_character) == 39:
        print("it's ASCII value is", ord("'"))
    if ord(favorite_character) == 40:
        print("it's ASCII value is", ord(" \" "))
    if ord(favorite_character) == 41:
        print("it's ASCII value is", ord(" ) "))
    if ord(favorite_character) == 42:
        print("it's ASCII value is", ord("*"))
    if ord(favorite_character) == 43:
        print("it's ASCII value is", ord("+"))
    if ord(favorite_character) == 44:
        print("it's ASCII value is", ord(","))
    if ord(favorite_character) == 45:
        print("it's ASCII value is", ord("-"))
    if ord(favorite_character) == 46:
        print("it's ASCII value is", ord("."))
    if ord(favorite_character) == 47:
        print("it's ASCII value is", ord("/"))
    if ord(favorite_character) == 48:
        print("it's ASCII value is", ord("0"))
    if ord(favorite_character) == 49:
        print("it's ASCII value is", ord("1"))
    if ord(favorite_character) == 50:
        print("it's ASCII value is", ord("2"))
    if ord(favorite_character) == 51:
        print("it's ASCII value is", ord("3"))
    if ord(favorite_character) == 52:
        print("it's ASCII value is", ord("4"))
    if ord(favorite_character) == 53:
        print("it's ASCII value is", ord("5"))
    if ord(favorite_character) == 54:
        print("it's ASCII value is", ord("6"))
    if ord(favorite_character) == 55:
        print("it's ASCII value is", ord("7"))
    if ord(favorite_character) == 56:
        print("it's ASCII value is", ord("8"))
    if ord(favorite_character) == 57:
        print("it's ASCII value is", ord("9"))
    if ord(favorite_character) == 58:
        print("it's ASCII value is", ord(":"))
    if ord(favorite_character) == 59:
        print("it's ASCII value is", ord(";"))
    if ord(favorite_character) == 60:
        print("it's ASCII value is", ord("<"))
    if ord(favorite_character) == 61:
        print("it's ASCII value is", ord("="))
    if ord(favorite_character) == 62:
        print("it's ASCII value is", ord(">"))
    if ord(favorite_character) == 63:
        print("it's ASCII value is", ord("?"))
    if ord(favorite_character) == 64:
        print("it's ASCII value is", ord("@"))
    if ord(favorite_character) == 65:
        print("it's ASCII value is", ord("A"))
    if ord(favorite_character) == 66:
        print("it's ASCII value is", ord("B"))
    if ord(favorite_character) == 67:
        print("it's ASCII value is", ord("C"))
    if ord(favorite_character) == 68:
        print("it's ASCII value is", ord("D"))
    if ord(favorite_character) == 69:
        print("it's ASCII value is", ord("E"))
    if ord(favorite_character) == 70:
        print("it's ASCII value is", ord("F"))
    if ord(favorite_character) == 71:
        print("it's ASCII value is", ord("G"))
    if ord(favorite_character) == 72:
        print("it's ASCII value is", ord("H"))
    if ord(favorite_character) == 73:
        print("it's ASCII value is", ord("I"))
    if ord(favorite_character) == 74:
        print("it's ASCII value is", ord("J"))
    if ord(favorite_character) == 75:
        print("it's ASCII value is", ord("K"))
    if ord(favorite_character) == 76:
        print("it's ASCII value is", ord("L"))
    if ord(favorite_character) == 77:
        print("it's ASCII value is", ord("M"))
    if ord(favorite_character) == 78:
        print("it's ASCII value is", ord("N"))
    if ord(favorite_character) == 79:
        print("it's ASCII value is", ord("O"))
    if ord(favorite_character) == 80:
        print("it's ASCII value is", ord("P"))
    if ord(favorite_character) == 81:
        print("it's ASCII value is", ord("Q"))
    if ord(favorite_character) == 82:
        print("it's ASCII value is", ord("R"))
    if ord(favorite_character) == 83:
        print("it's ASCII value is", ord("S"))
    if ord(favorite_character) == 84:
        print("it's ASCII value is", ord("T"))
    if ord(favorite_character) == 85:
        print("it's ASCII value is", ord("U"))
    if ord(favorite_character) == 86:
        print("it's ASCII value is", ord("V"))
    if ord(favorite_character) == 87:
        print("it's ASCII value is", ord("W"))
    if ord(favorite_character) == 88:
        print("it's ASCII value is", ord("X"))
    if ord(favorite_character) == 89:
        print("it's ASCII value is", ord("Y"))
    if ord(favorite_character) == 90:
        print("it's ASCII value is", ord("Z"))
    if ord(favorite_character) == 91:
        print("it's ASCII value is", ord("["))
    if ord(favorite_character) == 92:
        print("it's ASCII value is", ord("\\"))
    if ord(favorite_character) == 93:
        print("it's ASCII value is", ord("]"))
    if ord(favorite_character) == 94:
        print("it's ASCII value is", ord("^"))
    if ord(favorite_character) == 95:
        print("it's ASCII value is", ord("_"))
    if ord(favorite_character) == 96:
        print("it's ASCII value is", ord("`"))
    if ord(favorite_character) == 97:
        print("it's ASCII value is", ord("a"))
    if ord(favorite_character) == 98:
        print("it's ASCII value is", ord("b"))
    if ord(favorite_character) == 99:
        print("it's ASCII value is", ord("c"))
    if ord(favorite_character) == 100:
        print("it's ASCII value is", ord("d"))
    if ord(favorite_character) == 101:
        print("it's ASCII value is", ord("e"))
    if ord(favorite_character) == 102:
        print("it's ASCII value is", ord("f"))
    if ord(favorite_character) == 103:
        print("it's ASCII value is", ord("g"))
    if ord(favorite_character) == 104:
        print("it's ASCII value is", ord("h"))
    if ord(favorite_character) == 105:
        print("it's ASCII value is", ord("i"))
    if ord(favorite_character) == 106:
        print("it's ASCII value is", ord("j"))
    if ord(favorite_character) == 107:
        print("it's ASCII value is", ord("k"))
    if ord(favorite_character) == 108:
        print("it's ASCII value is", ord("l"))
    if ord(favorite_character) == 109:
        print("it's ASCII value is", ord("m"))
    if ord(favorite_character) == 110:
        print("it's ASCII value is", ord("n"))
    if ord(favorite_character) == 111:
        print("it's ASCII value is", ord("o"))
    if ord(favorite_character) == 112:
        print("it's ASCII value is", ord("p"))
    if ord(favorite_character) == 113:
        print("it's ASCII value is", ord("q"))
    if ord(favorite_character) == 114:
        print("it's ASCII value is", ord("r"))
    if ord(favorite_character) == 115:
        print("it's ASCII value is", ord("s"))
    if ord(favorite_character) == 116:
        print("it's ASCII value is", ord("t"))
    if ord(favorite_character) == 117:
        print("it's ASCII value is", ord("u"))
    if ord(favorite_character) == 118:
        print("it's ASCII value is", ord("v"))
    if ord(favorite_character) == 119:
        print("it's ASCII value is", ord("w"))
    if ord(favorite_character) == 120:
        print("it's ASCII value is", ord("x"))
    if ord(favorite_character) == 121:
        print("it's ASCII value is", ord("y"))
    if ord(favorite_character) == 122:
        print("it's ASCII value is", ord("z"))
    if ord(favorite_character) == 123:
        print("it's ASCII value is", ord("{"))
    if ord(favorite_character) == 124:
        print("it's ASCII value is", ord("|"))
    if ord(favorite_character) == 125:
        print("it's ASCII value is", ord("}"))
    if ord(favorite_character) == 126:
        print("it's ASCII value is", ord("~"))
    if ord(favorite_character) == 127:
        print("it's ASCII value is DEL")

    if ord(favorite_character) == ord("A"):
        print("and it is the 1st letter of the alphabet.")
    if ord(favorite_character) == ord("B"):
        print("and it is the 2nd letter of the alphabet.")
    if ord(favorite_character) == ord("C"):
        print("and it is the 3rd letter of the alphabet.")
    if ord(favorite_character) == ord("D"):
        print("and it is the 4th letter of the alphabet.")
    if ord(favorite_character) == ord("E"):
        print("and it is the 5th letter of the alphabet.")
    if ord(favorite_character) == ord("F"):
        print("and it is the 6th letter of the alphabet.")
    if ord(favorite_character) == ord("G"):
        print("and it is the 7th letter of the alphabet.")
    if ord(favorite_character) == ord("H"):
        print("and it is the 8th letter of the alphabet.")
    if ord(favorite_character) == ord("I"):
        print("and it is the 9th letter of the alphabet.")
    if ord(favorite_character) == ord("J"):
        print("and it is the 10 letter of the alphabet.")
    if ord(favorite_character) == ord("K"):
        print("and it is the 11th letter of the alphabet.")
    if ord(favorite_character) == ord("L"):
        print("and it is the 12th letter of the alphabet.")
    if ord(favorite_character) == ord("M"):
        print("and it is the 13th letter of the alphabet.")
    if ord(favorite_character) == ord("N"):
        print("and it is the 14th letter of the alphabet.")
    if ord(favorite_character) == ord("O"):
        print("and it is the 15th letter of the alphabet.")
    if ord(favorite_character) == ord("P"):
        print("and it is the 16th letter of the alphabet.")
    if ord(favorite_character) == ord("Q"):
        print("and it is the 17th letter of the alphabet.")
    if ord(favorite_character) == ord("R"):
        print("and it is the 18th letter of the alphabet.")
    if ord(favorite_character) == ord("S"):
        print("and it is the 19th letter of the alphabet.")
    if ord(favorite_character) == ord("T"):
        print("and it is the 20th letter of the alphabet.")
    if ord(favorite_character) == ord("U"):
        print("and it is the 21st letter of the alphabet.")
    if ord(favorite_character) == ord("V"):
        print("and it is the 22nd letter of the alphabet.")
    if ord(favorite_character) == ord("W"):
        print("and it is the 23rd letter of the alphabet.")
    if ord(favorite_character) == ord("X"):
        print("and it is the 24th letter of the alphabet.")
    if ord(favorite_character) == ord("Y"):
        print("and it is the 25th letter of the alphabet.")
    if ord(favorite_character) == ord("Z"):
        print("and it is the 26th letter of the alphabet.")