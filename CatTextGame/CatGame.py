'''
Filename: CatGame.py
Author: Brandon Smith
Date: 11/8/23
Description: This is a game about a cat that is exploring the dark streets of
The Town. He will encounter various challenges along the way and their choices
will determine their fate.

'''

import time
import random
import sys
import os

num_lives = 9
name = ""
cat_king_lives = 9
rat_king_lives = 6
def screen_clear()->None:
    for i in range(20):
        time.sleep(0.1)
        print("\n")
def print_intro(name: str):
    sleep_animation()
    for i in range(20):
        time.sleep(0.1)
        print("\n")
    time.sleep(2)
    print(r"""
 _._     _,-'""`-._
(,-.`._,'(       |\`-/|
    `-.-' \ )-`( , o o)
          `-    \`_`"'-""")
    time.sleep(2)
    print(f"""        
{name}, you have just woken up from a short cat nap that started in the afternoon sun.
It is now night time and you are ready for an adventure. """)


def lives_change(num_lives: int, value: int) -> int:
    return num_lives + value


def status() -> str:
    global num_lives
    global name
    return f"{name}, your current lives is {num_lives}"

#Decision 2a
def eat_tuna_can():
    global num_lives
    global name
    print(f"""{name}, you come across a tuna can with some tuna left in it.
    Do you want to eat it or keep going?""")
    choice = int(input("""
    1. Eat it
    2. Keep going
    > """))
    if choice == 1:
        rand_num = random.randint(1,10)
        if 1<= rand_num <= 3:
            print(f"""{name} you chose to eat the can of tuna 
            and unfortunately it made you sick.""")
            num_lives -= 3
            status()
    else:
        print(f"""""")
def alley_street_cross(street_name: str):
    global num_lives
    print(
        f"""You reach an intersection on {street_name}. 
What are you going to do?...""")
    time.sleep(3)
    print(f"""
1. Go down the dark alley
2. Continue down {street_name}
3. Cross the street. """)

    print("""> """, end="")
    choice = int(input())
    if choice == 1:
        alley_encounter()
    elif choice == 2:
        eat_tuna_can()
    else:
        alley_encounter()




def alley_animation() -> None:
    print(r"""
    
.             .        .     .     |--|--|--|--|--|--|  |===|==|   /    i
        .            ______________|__|__|__|__|__|_ |  |===|==|  *  . /=\
__ *            .   /______________________________|-|  |===|==|       |=|  .
__|  .      .   .  //______________________________| :----------------------.
__|   /|\      _|_|//       ooooooooooooooooooooo  |-|                      |
__|  |/|\|__   ||l|/,-------8                   8 -| |                      |
__|._|/|\|||.l |[=|/,-------8                   8 -|-|                      |
__|[+|-|-||||li|[=|---------8                   8 -| |                      |
_-----.|/| //:\_[=|\`-------8                   8 -|-|                      |
 /|  /||//8/ :  8_|\`------ 8ooooooooooooooooooo8 -| |                      |
/=| //||/ |  .  | |\\_____________  ____  _________|-|                      |
==|//||  /   .   \ \\_____________ |X|  | _________| `---==------------==---'
==| ||  /         \ \_____________ |X| \| _________|     ||            ||
==| |~ /     .     \
LS|/  /             \______________________________________________________
    
    """)


def dumpster_animation():
    print(r"""
                          __________________
                      \                 \
                        \                 \
                          \                 \
                            \                 \
           /-------------------------------------
         //---------------//                  / |
       //               //                  / __|
     //               //                  / /  ||
   //               //                  / /    ||
 //_______________//   o o            / /      ||      ___/-\___
------------------------------------/   ------- |     |---------|
| DO NOT PLAY |         | HOUSEHOLD |           |      | | | | |
| ON OR AROUND|         |WASTE ONLY |           |      | | | | |
|--------------         ------------|           |      | | | | |
|                                   |           |      | | | | |
-------------------------------------------------      |_______|
    
    """)
    return None

def sleep_animation():
    print(r"""
               __..--''``---....___   _..._    __
 /// //_.-'    .-/";  `        ``<._  ``.''_ `. / // /
///_.-' _..--.'_    \                    `( ) ) // //
/ (_..-' // (< _     ;_..__               ; `' / ///
 / // // //  `-._,_)' // / ``--...____..-' /// / //
    
    
    """)

def death_animation()->None:
    print(r"""
           ___
          (___)
   ____
 _\___ \  |\_/|
\     \ \/ , , \ ___
 \__   \ \ ="= //|||\
  |===  \/____)_)||||
  \______|    | |||||
      _/_|  | | =====
     (_/  \_)_) 
  _________________
 (                _)
  (__   '          )
    (___    _____)
        '--'
    
    """)

def rat_animation():
    print(R"""
               _     __,..---""-._                 ';-,
        ,    _/_),-"`             '-.                `\\
       \|.-"`    -_)                 '.                ||
       /`   a   ,                      \              .'/
       '.___,__/                 .-'    \_        _.-'.'
          |\  \      \         /`        _`""""""`_.-'
             _/;--._, >        |   --.__/ `""""""`
           (((-'  __//`'-.....-;\\      )
                (((-'       __//  '--. /
                          (((-'    __//
                                 (((-'
    
    """)


def load_animation(animation:str)->None:
    if animation == "alley":
        alley_animation()
    elif animation == "dumpster":
        dumpster_animation()

def alley_encounter():
    global num_lives
    dumpster_animation()
    time.sleep(2)
    for i in range(20):
        time.sleep(0.1)
        print("\n")
    time.sleep(2)
    print(f"""While continuing down the alley, you come across a tasty 
    looking dumpster. You currently have {num_lives} lives. 
    What do you want to do?""")
    time.sleep(0.8)
    print(f"""
    1. Explore the dumpster
    3. Explore the open door """)
    choice = int(input("> "))
    if choice == 1:
        dumpster_encounter()
    else:
        rat_king_encounter()


def dumpster_encounter() -> None:
    global num_lives
    dumpster_animation()
    print(f"""You follow the delicious smells and 
    enter the dumpster. You just found an excellent looking
    piece of fish when you hear a noise...""")
    rand_num = random.randint(1,10)
    if 0 <= rand_num <= 6:
        rand_health = random.randint(1,2)
        print(f"""A large rat scurries by, but leaves you unharmed.
        You enjoy the food and get {rand_health} extra lives""")
        num_lives += rand_health
    else:
        print("""A large rat attacks you from behind, bites you, then
              steals the fish from you. You lose one life""")
        num_lives -= 1
    status()
    rat_king_encounter()
def cat_king_encouter():
    print("""""")
    return None
def rat_status():
    global rat_king_lives
    print(f"The rat king has {rat_king_lives} lives left")
def rat_king_encounter():
    global num_lives
    global rat_king_lives
    block = False
    print(f"""You enter the door and find yourself in a large kitchen.
    It is full of fresh food and you are so hungry.""")
    time.sleep(0.5)
    print(f"""Out of the corner of your eye, you see movement in
    the shadows and realize you are not alone.""")
    screen_clear()
    rat_animation()
    for i in range(3):
        rat_damage = random.randint(0,3)
        block_chance = random.randint(1,10)
        if 1 <= block_chance <= 3:
            rat_damage = 0
            block = True
        print("""The rat attacks, do you...
        1. Bite
        2. Use your claws""")
        choice = int(input("> "))
        if choice == 1:
            if block:
                print(f"You blocked the rat king's attack and ",end=" ")
            cat_damage_bite = random.randint(0,2)
            num_lives -= rat_damage
            rat_king_lives -= cat_damage_bite
        if choice == 2:
            cat_damage_claws = random.randint(0,4)
            num_lives -= rat_damage
            rat_king_lives -= cat_damage_claws



    return None
def street_cross_encounter():
    print(""" decide to cross the street. It looks rather quiet, 
but then you see the headlights of a car and...\n""")
    rand_num = random.randint(1, 10)
    if rand_num <= 10 :
        print("you are not able to get out of the way in time.")
        bad_ending()
    else:
        print("""the car swerves out of the way, crashes into a fire
hydrant, but you safely make it across.""")
        cat_king_encouter()


def bad_ending() -> bool:
    screen_clear()
    death_animation()

    print(f"""The life of a street cat is a tough one. Unfortunately,
you did not survive the night. Would you like to play again?
> """)
    choice = ""
    while choice == "" or (choice != "yes" or choice != "no"):
        choice = input().lower()
    if choice == "yes":
        return True
    else:
        return False


def main():
    global name
    time.sleep(2)
    name = input("What is your name? ")
    print_intro(name)
    time.sleep(0.5)
    status()
    first_choice = alley_street_cross("Cat Nip Lane")


if __name__ == '__main__':
    main()
