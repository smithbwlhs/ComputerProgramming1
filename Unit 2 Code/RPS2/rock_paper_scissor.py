"""
Name: Brandon Smith
Date: 9/29/23
Assignment: Rock, Paper, Scissor game

"""
import random

# Welcome the user
print("Welcome to rock, paper, scissor!")

# Get user choice
user_choice = ""
while user_choice != "rock" and user_choice != "scissor" and user_choice != "paper":
    print("Please select rock, paper, or scissor: ")
    user_choice = input(">").lower()

# Get computer choice
random_int = random.randint(1,3)
computer_choice = ""
if random_int == 1:
    computer_choice = "rock"
elif random_int == 2:
    computer_choice = "paper"
elif random_int == 3:
    computer_choice = "scissor"
else:
    computer_choice = "Invalid"

print("The computer chose",computer_choice)
# Determine win, loss, tie - rock beats scissor,
# paper beats rock, scissor beats paper

# win
if (
    (user_choice == "rock" and computer_choice == "scissor")
    or (user_choice == "paper" and computer_choice == "rock")
    or (user_choice == "scissor" and computer_choice == "paper")
):
    print("You win!")
# loss
elif (
    (user_choice == "rock" and computer_choice == "paper")
    or (user_choice == "paper" and computer_choice == "scissor")
    or (user_choice == "scissory" and computer_choice == "rock")
):
    print("You lose :-( ")
# tie
elif user_choice == computer_choice:
    print("Tied!")

# Print "Thanks for playing!"
print("Thaks for playing!")
