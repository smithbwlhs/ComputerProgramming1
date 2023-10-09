user_number = int(input("Enter your favorite number: "))
user_name = input("Name: ")

if user_number == 1:
    print("Boring")
elif user_number == 2:
    print("Interesting")
elif user_number == 3: 
    print("Totally agree!")
else:
    print("What a bad choice")

##Equivalent match case

match user_number:
    case 1:
        print("Boring")
    case 2 | 5:
        print("Interesting")
    case 3:
        print("Totally agree!")
    case _:
        print("What a bad choice")

match user_number % 2:
    case 0:
        print("Even")
    case 1:
        print("Odd")
    case _:
        print("Not an integer")

match user_name:
    case "Mr. Smith":
        print("Hi!")
    case _:
        print("Goodbye")