"""
Name: Brandon Smith
Date: 9/29/23
Assignment: Rock Paper Scissors game
Description: An implementation of rock, paper, scissors in 
Python where a user can play against the computer until 
they type 'quit'.

"""

# Welcome the user
print("Welcome to rock, paper, scissors!")
# Get user choice

user_choice = ""
while user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
    print("Do you want rock, paper, or scissors?")
    user_choice = input("> ").lower()

print("You chose",user_choice)
# Get computer choice
computer_choice = "rock"
print("The computer chose",computer_choice)

# Determine win, loss, tie - rock beat scissors, paper beats rock,
# scissors beat paper

# win
if (
    (user_choice == "rock" and computer_choice == "scissors")
    or (user_choice == "paper" and computer_choice == "rock")
    or (user_choice == "scissors" and computer_choice == "paper")
):
    print("You win!")

# loss
elif (
    (user_choice == "scissors" and computer_choice == "rock")
    or (user_choice == "rock" and computer_choice == "paper")
    or (user_choice == "paper" and computer_choice == "scissors")
):
    print("You lose :-( ")
# tie
elif user_choice == computer_choice:
    print("Tie!")

# Thank user for playing
print("Thanks for playing!")
