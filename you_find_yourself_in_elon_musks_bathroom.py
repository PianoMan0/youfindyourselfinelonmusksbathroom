import os
import time
import math
import random
import crayons
from os import system
from playsound import playsound
import threading


def start_game():
    print("You find yourself in the bathroom of Elon Musk.")
    print("You don't know how you got here.")
    print("The room is filled with mysterious objects.")
    print("There are so many decisions to make.")
    print("Buuuuttttt, first you have to decide if you want some music!")
    print(crayons.blue("1. I want music!. ", bold=True))
    print(crayons.blue("2. No thanks! ", bold=True))

    choice = input("Enter 1 or 2")

    if choice == '1':
        music()

    elif choice == '2':
        look_mirror()

    else:
        print("Invalid choice. Please try again.")
        start_game()

def check_toilet():
    print("You walk toward the toilet. It's very high-tech!")
    print("You open the lid and Donald Trump pops out!")
    print("He looks around ... and then ducks back in.")
    print("You decide to move on for now.")
    print(crayons.blue("1. Look in the mirror. ", bold=True))
    print(crayons.blue("2. Try to leave the bathroom. ", bold=True))
    print(crayons.blue("3. Inspect the sink. ", bold=True))
    choice = input("Enter 1, 2, or 3: ")

    if choice == '1':
        look_mirror()

    elif choice == '2':
        leave_bathroom()

    elif choice == '3':
        inspect_sink()

    else:
        print("Invalid choice. Please try again.")
        check_toilet()
    print("What would you like to do?")
    print(crayons.blue("1. Check out the toilet. ", bold=True))
    print(crayons.blue("2. Look in the mirror. ", bold=True))
    print(crayons.blue("3. Try to leave the bathroom. ", bold=True))
    print(crayons.blue("4. Inspect the sink. ", bold=True))

    choice = input("Enter 1, 2, 3, or 4: ")

    if choice == '1':
        check_toilet()

    elif choice == '2':
        look_mirror()

    elif choice == '3':
        leave_bathroom()

    elif choice == '4':
        inspect_sink()

    else:
        print("Invalid choice. Please try again.")
        start_game()

def check_toilet():
    print("You walk toward the toilet. It's very high-tech!")
    print("You open the lid and Donald Trump pops out!")
    print("He looks around ... and then ducks back in.")
    print("You decide to move on for now.")
    print(crayons.blue("1. Look in the mirror. ", bold=True))
    print(crayons.blue("2. Try to leave the bathroom. ", bold=True))
    print(crayons.blue("3. Inspect the sink. ", bold=True))
    choice = input("Enter 1, 2, or 3: ")

    if choice == '1':
        look_mirror()

    elif choice == '2':
        leave_bathroom()

    elif choice == '3':
        inspect_sink()

    else:
        print("Invalid choice. Please try again.")
        check_toilet()

def look_mirror():
    print("You look in the mirror.")
    print("It says, 'You are not Elon Musk. Therefore, you don't look good.'")
    print("You are quite offended.")
    print("You decide to move on for now.")
    print(crayons.blue("1. Check out the toilet. ", bold=True))
    print(crayons.blue("2. Try to leave the bathroom. ", bold=True))
    print(crayons.blue("3. Inspect the sink. ", bold=True))
    choice = input("Enter 1, 2, or 3: ")

    if choice == '1':
        check_toilet()

    elif choice == '2':
        leave_bathroom()

    elif choice == '3':
        inspect_sink()

    else:
        print("Invalid choice. Please try again.")
        look_mirror()

def leave_bathroom():
    print("You decide to leave the bathroom.")
    print("As you try to walk out,")
    print("you realize that there is an invisible forcefield keeping you inside.")
    print("You decide to move on for now.")
    print("")
    print("")
    print(crayons.blue("1. Check out the toilet. ", bold=True))
    print(crayons.blue("2. Look in the mirror. ", bold=True))
    print(crayons.blue("3. Walk back to where you started. ", bold=True))
    print(crayons.blue("4. Inspect the sink. ", bold=True))
    choice = input("Enter 1, 2, 3, or 4: ")

    if choice == '1':
        check_toilet()

    elif choice == '2':
        look_mirror()

    elif choice == '3':
        start_game_again_evil_laugh()

    elif choice == '4':
        inspect_sink()

    else:
        print("Invalid choice. Please try again.")
        leave_bathroom()

def inspect_sink():
    print("You walk towards the sink. It's made of pure gold!")
    print("As you turn on the faucet, a hologram of Elon Musk appears.")
    print("He says, 'Welcome to my bathroom. Enjoy your stay!'")
    print("You decide to move on for now.")
    print(crayons.blue("1. Check out the toilet. ", bold=True))
    print(crayons.blue("2. Look in the mirror. ", bold=True))
    print(crayons.blue("3. Try to leave the bathroom. ", bold=True))
    choice = input("Enter 1, 2, or 3: ")

    if choice == '1':
        check_toilet()

    elif choice == '2':
        look_mirror()

    elif choice == '3':
        leave_bathroom()

    else:
        print("Invalid choice. Please try again.")
        inspect_sink()

def start_game_again_evil_laugh():
    print("You find yourself back where you started.")
    print("But now you hear Elon Musk's laugh.")
    print("He can hear you, and now you can hear him.")
    print("You notice a loose tile in the wall.")
    print("You push it and the wall falls over!")
    print("You find a small shower.")
    print("You step inside and shower door closes behind you.")
    print("You are trapped in Elon Musk's shower!")
    print("You decide to move on for now.")
    print(crayons.blue("1. Pick up the bar of soap. ", bold=True))
    print(crayons.blue("2. Turn on the shower. ", bold=True))
    print(crayons.blue("3. Hit stuff. ", bold=True))
    choice = input("Enter 1, 2, or 3: ")

    if choice == '1':
        pick_up_soap()

    elif choice == '2':
        turn_on_shower()

    elif choice == '3':
        hit_stuff()

    else:
        print("Invalid choice. Please try again.")
        start_game_again_evil_laugh()

# Start the game
start_game()

def pick_up_soap():
    print("You pick up the bar of soap.")
    print("It splits in two revealing a swastika.")
    print("You smell something strange and then everything goes")
    crayons.black("black.", bold=True)
    print("")
    print("")
    print("You wake up slowly, groaning.")
    print("The bar of soap is gone.")
    print("You are still stuck in the shower.")
    print(crayons.blue("1. Pick up the bar of soap. ", bold=True))
    print(crayons.blue("2. Turn on the shower. ", bold=True))
    print(crayons.blue("3. Hit stuff. ", bold=True))
    choice = input("Enter 1, 2, or 3: ")

    if choice == '1':
        pick_up_soap_again()

    elif choice == '2':
        turn_on_shower()

    elif choice == '3':
        hit_stuff()

    else:
        print("Invalid choice. Please try again.")
        inspect_sink()

def hit_stuff():
    print("What do you want to hit?")
    print(crayons.blue("1. The door. ", bold=True))
    print(crayons.blue("2. The wall. ", bold=True))
    print(crayons.blue("3. Yourself. ", bold=True))
    choice = input("Enter 1, 2, or 3: ")

    if choice == '1':
        door_hit()

    elif choice == '2':
        wall_hit()

    elif choice == '3':
        self_hit()

    else:
        print("Invalid choice. Please try again.")
        inspect_sink()

def self_hit():
    print("You hit yourself.")
    
    
def pick_up_soap_again():
    print("Bruh, who are you?")
    print("Didn't you read the last message?")
    print("There is no soap anymore.")
    print("Just for that I'm adding a plot twist.")
    print("A ton of bars of soap fall on your head, and you start to loose consciousness.")
    print(crayons.blue("1. Don't fight it. ", bold=True))
    print(crayons.blue("2. Punch the wall. ", bold=True))
    choice = input("Enter 1, 2, or 3: ")

    if choice == '1':
        no_fighty()

    elif choice == '2':
        punch_wall()

    else:
        print("Invalid choice. Please try again.")
        pick_up_soap_again()


def punch_wall():
    print("You punch the wall.")
    print("")

    if choice == '1':
        start_game()

    elif choice == '2':
        print("Goodbye.")

    else:
        print("Invalid choice. Please try again.")
        punch_wall()

    
def no_fighty():
    print("You wake up in a dark room.")
    print("You hear a voice.")
    print("It says, 'You have been chosen.'")
    print("You are never seen again.")
    print(crayons.red("THE END. ", bold=True))
    print("Thanks for playing!")
    print("What would have happened if you made different choices?.")
    print("You'll never know.")
    print("Or will you?")
    print(crayons.blue("1. Play again. ", bold=True))
    print(crayons.blue("2. Be a boring person and quit. ", bold=True))
    choice = input("Enter 1, 2, or 3: ")

    if choice == '1':
        start_game()

    elif choice == '2':
        print("Goodbye.")

    else:
        print("Invalid choice. Please try again.")
        no_fighty()

    print("This could be your final choice of the game, so choose wisely.")
