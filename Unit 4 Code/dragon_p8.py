import random
import time

random.seed(7815)

"""
Name: Brandon Smith
Date: 10/23/23
File name: dragon.py
Description: A text based game where an explorer chooses
what cave to enter and deals with the consequences

"""

def display_intro():
    """Prints an introduction to the game

    Parameters
    ----------
    None

    Returns
    -------
    None
    
    """
    print()
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly and will
share his treasure with you. The other dragon is greedy and 
hungry and will eat you on sight.''')
    print()

def choose_cave():
    """Asks a user to choose the cave they want to enter. It
    will prompt them until they enter either 1 or 2.
    
    Parameters
    ----------
    None

    Returns
    -------
    cave: str
        The cave the user chooses
    """
    cave = ''
    while cave != '1' and cave != '2':
        print("Which cave will you go into? (1 or 2) ", end = '')
        cave = input()
    return cave

def check_cave(chosen_cave):
    """Determines if the user is eaten or not based on 
    their cave choice.

    Parameters
    ----------
    chosen_cave: str
        The cave the user chose

    Returns
    -------
    None
    
    """
    print("You approach the cave...")
    time.sleep(2)
    print("It's dark and spooky...")
    time.sleep(2)
    print('''A large dragon jumps out in front of you!
He opens his jaws and...''')
    print()
    time.sleep(2)

    friendly_cave = random.randint(1,2)
    if chosen_cave == str(friendly_cave):
        print("Gives you his treasure!")
    else:
        print("Gobbles you down in one bite!")



####Test Code Here###

play_again = "yes"

while play_again.lower() == "yes":
    display_intro()
    user_cave = choose_cave()
    check_cave(user_cave)

    print("Do you want to play again? (yes or no)", end = ' ')
    play_again = input()
