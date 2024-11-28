import os
import time
import math
import crayons
from os import system

def start_game():
    print("You find yourself in the bathroom of Elon Musk.")
    print("You don't know how you got here.")
    print("The room is filled with mysterious objects.")
    print("What would you like to do?")
    print(crayons.blue("1. Check out the toilet. ", bold=True))
    print(crayon.blue("2. Look in the mirror. ", bold=True))
    print(crayon.blue("3. Try to leave the bathroom. ", bold=True))

    choice = input("Enter 1, 2, or 3: ")

    if choice == '1':
        check_toilet()

    elif choice == '2':
        look_mirror()

    elif choice == '3':
        leave_bathroom()

    else:
        print("Invalid choice. Please try again.")
        start_game()

def check_toilet():
    print("You walk toward the toilet. It's very high-tech!")
    print("You open the lid and Donald Trump pops out!")
    print("He looks around ... and then ducks back in.")
    print("You decide to move on for now.")
    print("")
    print("")
    start_game()

def look_mirror():
    print("You look in the mirror.")
    print("It says, 'You are not Elon Musk. Therefore, you don't look good.'")
    print("You are quite offended.")
    print("You decide to move on for now.")
    print("")
    print("")
    start_game()

def leave_bathroom():
    print("You decide to leave the bathroom.")
    print("As you try to walk out,")
    print("you realize that there is a invisible forcefield keeping you inside.")
    print("You decide to move on for now.")
    print("")
    print("")

start_game()