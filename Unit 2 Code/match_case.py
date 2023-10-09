user_number = int(input("Enter your favorite number: "))

match user_number % 2:
    case 0:
        print("Even")
    case 1:
        print("Odd")
    case _:
        print("NaN")


match user_number:
    case 1:
        print("Boring")
    case 2:
        print("Interesting, first prime")
    case 3:
        print("Totally agree!")
    case _:
        print("What a bad choice")
#Equivalent by using if-elif-else
if user_number == 1:
    print("Boring")
elif user_number == 2:
    print("Interesting, first prime")
elif user_number == 3:
    print("Totally agree!")
else:
    print("What a bad choice")