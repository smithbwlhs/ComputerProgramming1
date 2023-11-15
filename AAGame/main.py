'''
Name: Ryan Bradley
Date: 10/23/23
Assignment: Text Adventure Game


'''
score = 0

import random
import time


def intro():
    print(''' it is dark and rainny you are looking for somewhere to stay..''')
    print()
    time.sleep(3)
    print('''  you find a old mansion at the edge of the town.''')
    time.sleep(3)
    return first_part()


def first_part():
    global score
    print()
    print('''you check to see if anyone is inside... ''')
    time.sleep(3)
    print()
    print('''  But it looks like nobody has lived in  there for years..''')
    time.sleep(3)
    print()
    print("the wind blows open the old runn down door..\t")
    print()
    time.sleep(3)
    print()
    print(''' What will you do?
            Enter ( 1 ) if you want to enter the house
            Enter ( 2 ) if you dont want to enter the house ''')
    decision = int(input("Enter choice here :"))
    while decision != 1 and decision != 2:
        decision = int(input("Enter choice  here :"))
    if decision == 1:
        score = score + 10
        print()
        print("you gained 10 points you now have a total of ", score, "points")
        print()
        return second_part()


    elif decision == 2:
        print(''' You ran past the house and tried to make it to the next town but.''')
        print()
        time.sleep(3)
        print("you died of natural causes on your way ...")
        print()
        print("you died with a total score of ", score, "points :C")


def main_hall():
    global score
    print(''' you jump into a wardrobe...''')
    time.sleep(3)
    print()
    print(
        '''  as the foot steps grow closer you peak through the crack of the doors...''')
    print()
    time.sleep(3)
    print("you see a ghost of a women skipping passed you with a knife in her hand")
    time.sleep(3)
    print(''' what will you do
                Enter ( 1 ) if you want to sneak up stairs
                Enter ( 2 ) if you want to rush back to the front door and see if its
                unlocked''')
    print()
    decision = int(input("Enter choice  here :"))
    while decision != 1 and decision != 2:
        decision = int(input("Enter choice  here :"))
    if decision == 1:
        score = score + 10
        print("you gained 10 points you now have a total of ", score, "points")
        print()
        return bedroom()
    elif decision == 2:
        print()

        return main_hall_bad()


def hide_in_cabinets():
    global score
    print(''' now that you look around it is a pretty big kitchen...

         you see 4 cabinets that you cabinets that you could hide in ''')
    print()
    print(''' Which cabinet will you get in

               ''')

    decision = int(input('Enter a number between 1 and 4 :'))
    while decision > 4:
        decision = int(input('Enter a number between 1 and 4 :'))
    death = random.randint(1, 4)
    if decision != death:
        score = score + 10
        print()
        print("you gained 10 points you now have a total of ", score, "points")
        print()
        return third_part()
    else:
        print()
        print("you died with a total score  was ", score, "points")
        print()


def third_part():
    global score
    print(''' The ghost reaches down and opens the cabinet right next to you ''')
    print()
    time.sleep(3)
    print(''' The women skips away out of the kitchen into the main hall ''')
    print()
    print(''' what will you do?
                Enter ( 1 ) if you want to make a dash for the front door
                Enter ( 2 ) if you want to make a dash for the back door''')
    decision = int(input("Enter choice  here :"))
    while decision != 1 and decision != 2:
        decision = int(input("Enter choice  here :"))
    if decision == 1:
        print()
        print("you died with a total score  was ", score, "points")
        print()

        print(''' you make a mad dash through the dark hall way. ''')
        print()
        print(' you make it to the front door')
        # time.spent(2)
        print()
        print('its locked ')
        print()
        # time.spent(1)
        print(''' you feel a cold prescense hovering above you...''')
        print()
        print(''' The ghost lady is standing over you peircing you with her eyes..''')
        # time.sleep(1)
        print()
        print(
            'you feel your chest go numb and you look down and see a knife peircing  your chest')
        print()
        print('                             game over     ')
        print()
        print("    you died with a total of score of ", score, "points :C")
    elif decision == 2:
        score = score + 10
        print()
        print("you gained 10 points you now have a total of ", score, "points")
        print()
        return back_door()


def second_part():
    global score
    print(''' you tip toe into the house with the only sound is the old floor boards
            creaking under you... ''')
    print()
    time.sleep(3)
    print(''' as you are making your way through the main hall..''')
    print()
    time.sleep(3)
    print('''YOU SUDDENLTY HERE FOOTS STEP!!!! you notice that in the main hall

             there are 4 war drobes that look big enough to fit a person...''')
    print()
    time.sleep(3)
    print(''' but that the kitchen is also very close by

                and you can find somthing to protect yourself in there.''')
    print()
    time.sleep(3)
    print(''' what will you do?
               Enter ( 1 ) if you want to hide in one of the wardrobes
               Enter ( 2 ) if you want to try and make it to the kitchen.''')

    decision = int(input("Enter choice  here :"))
    while decision != 1 and decision != 2:
        decision = int(input("Enter choice  here :"))
    if decision == 2:
        score = score + 10
        print()
        print("you gained 10 points you now have a total of ", score, "points")
        print()
        return kitchen()
    elif decision == 1:

        print(''' you decide to get into one of the wardrobes there are 4 wardrobes..

                            which one will you get in ''')
    wardrobe = int(input("Enter ( 1 ) or ( 2 ) or  ( 3 ) or ( 4 ) :"))
    while wardrobe >= 5:
        wardrobe = int(input("Enter ( 1 ) or ( 2 ) or  ( 3 ) or ( 4 ) :"))

    death = random.randint(1, 4)
    if wardrobe != death:
        score = score + 10
        print()
        print("you gained 10 points you now have a total of ", score, "points")
        print()
        return main_hall()
    else:
        print()
        print("you gained 0 points your total score  was ", score)
        print()
        return main_hall_bad()


def bad_ending():
    global score
    print(''' you get under the bed''')
    time.sleep(2)
    print()
    print('''the ghost goes to pick up the picture she looks over and sees you.. ''')
    print()
    print(''' she grabs the broken picture and stabs you with it
                                game over''')
    print(" you died with a total score of ", score, "points")


def kitchen():
    global score
    print(''' You sneak into through the hall to the kitchen...''')
    print()
    time.sleep(3)
    print(''' becuase it is super dark you accidenlty run into a china wardrobe..

        it crashes to the ground and the foot steps get faster and are heading your way.
              ''')
    print()
    time.sleep(3)
    print(''' you made it to the kitchen ''')
    time.sleep(3)
    print("but what ever is folowing is right behind you. ")
    time.sleep(3)
    print('''you notice 2 giant cabinets that look like
                        they could fit a person...  ''')

    print()
    time.sleep(3)
    print(" you also see a knife on the kitchen counter...")
    print()
    time.sleep(3)
    print('''  What will you do
                   Enter ( 1 ) if you want to grab the knife and attack the entity
                   Enter ( 2 ) if you want to hide in of the 2 large cabinets''')
    decision = int(input("Enter choice  here :"))
    while decision != 1 and decision != 2:
        decision = int(input("Enter choice  here :"))

    if decision == 1:
        print()
        print("you gained 0 points your total score  was ", score)
        print()
        return kitchen_bad()

    elif decision == 2:
        return hide_in_cabinets()


def main_hall_bad():
    global score
    print(''' the ghost of a women skipping with a knife stops infront of your wardrobe

          It raises its knife and stabs you through the wardrobe doors..

                                 (game over you died)''')
    print("you died with a total socre of ", score, "points")


def bedroom():
    global score
    print(''' you see the ghost skip into the kitchen...''')
    time.sleep(3)
    print(''' you see this as a chance and head toward the spiral stare case in the

        middle of the main hall and ascend into the second floor

        all the doors are locked besides the door to the bedroom...''')
    time.sleep(3)
    print(''' You enter the bedroom and see pictures of the ghost women...''')
    time.sleep(3)
    print()
    print(''' She was beautiful ''')
    print()
    time.sleep(3)
    print(''' you hear skipping coming from the stairs. you drop the picture and it
    shatters...''')
    time.sleep(3)
    print()
    print('''  you hear the skipping get much faster as it draws closer and closer to

    The bedroom.''')
    time.sleep(3)
    print()
    print('''  you see that the window is open make you could escape through that


        but you are on the 2nd floor would you survive...''')
    time.sleep(3)
    print()
    print(''' you also realize that you could hide under the bed and wait for her
    to leave...''')
    time.sleep(3)
    print()
    print(''' What will you do?
          Enter ( 1 ) if you want to take a chance and jump ouf the window.
          Enter ( 2 ) if you want to hide under the bed and wait for her to go away.''')
    decision = int(input("Enter choice here :"))
    while decision != 1 and decision != 2:
        decision = int(input("Enter choice here :"))
    if decision == 1:
        score = score + 10
        print()
        print("you gained 10 points you now have a total of ", score, "points")
        print()
        return victory_1()
    elif decision == 2:
        print()
        print("you died with a  total score  was ", score)
        print()
        return bad_ending()


def victory_1():
    global score
    print(''' as the ghost women skips into the room you jump through the window''')
    time.sleep(3)
    print(''' and you land on a horse carrege filled with hay..''')
    time.sleep(3)
    print('''as you ride away you see the ghost women in the window staring at you...
                        (VICTORY)''')
    print(" you survided and ended up with a total of ", score, "points")


def kitchen_bad():
    global score
    print(''' while the ghost women looks away you slowly grab the knife off the counter
          ''')
    print()
    time.sleep(3)
    print(''' you lunge at the women but you just go right through her...

              the knife slips from your hand and it falls on the ground

                    and you fall onto the knife...''')
    print("                 game over     ")
    print()
    print("you died with a total score of ", score, "points")


def back_door():
    global score
    print(''' the back door is unlocked you open the door and find your self in a huge garden

              you rush into the garden and easily get lost...''')
    time.sleep(3)
    print(''' you hear a clacking sound that sounds like a horse its coming closer...''')
    print()
    print(''' What will you do?
              Enter ( 1 ) if you want to hide in a bush and wait for the sounds go by
              Enter ( 2 ) if you want to try and run to the exit of the gardan ''')
    decision = int(input("Enter choice here :"))
    while decision != 1 and decision != 2:
        decision = int(input("Enter choice here :"))
    if decision == 1:
        score = score + 10
        print("you gained 10 points you now have a total of ", score, "points")
        return hid_in_bush()
    elif decision == 2:
        print("you died with a total score   of  ", score, "points")
        return run_to_exist()


def hid_in_bush():
    global score
    print(''' you hide in  a bush ''')
    time.sleep(2)
    print()
    print("the steps go right past you you take a peak and see...")
    time.sleep(3)
    print(''' a gaint ghost horse with a armor set sitting on top of it wtih a spear ''')
    print()
    time.sleep(2)
    print(''' after a bit of waiting you see the knight charge towards somthing ''')
    time.sleep(2)
    print()
    print("you see this as a chance to make it out.")
    print()
    time.sleep(1)
    print(''' you make a run for the exit and you make it out ''')
    time.sleep(2)
    print()
    print(' you look back and the house and the garden are gone...')
    print()
    time.sleep(3)
    print('you return to the village and continue your journey')
    print()
    print("                         victory")
    print()
    print("you survived!! you escaped with a total of ", score, "points")


def run_to_exist():
    global score
    print(''' you make a run for it ''')
    time.sleep(2)
    print()
    print(''' but the foot steps are right behind you you look back and see...''')
    time.sleep(2)
    print("a knight sititng on top of a horse charging at you!!! ")
    print()
    time.sleep(1)
    print(''' the knight catches up to you  ''')
    time.sleep(2)
    print(''' and  feel a numbness in your chest and see a spear peirced through your heart  

                                game over''')

    print()
    print("oh no you died with a total of ", score, "points :C")


intro()