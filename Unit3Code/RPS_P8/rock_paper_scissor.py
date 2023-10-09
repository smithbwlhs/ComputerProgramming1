import random
random.seed(45604)
'''
Extensions:
Can we check to make sure they pick rock, paper, scissors only?
Can we ignore the case of letters e.g. ROck is the same as rock

'''


print("Welcome to rock, paper, scissors!!")
user_choice = " "
computer_choice = " "
while user_choice != "quit":
    user_choice = input("Do you want rock, paper, scissors?\n")
    random_number = random.randint(1,3)
    if random_number == 1:
        computer_choice = "rock"
    elif random_number == 2:
        computer_choice == "paper"
    else:
        computer_choice == "scissors"
    #if statements to see who wins
    #check if tie
    if user_choice == computer_choice:
        print("Tie")
    #check user wins
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock ") or \
        (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")

    #check user loses
    else:
        print("Computer wins :(")

print("Thanks for playing!")

    
