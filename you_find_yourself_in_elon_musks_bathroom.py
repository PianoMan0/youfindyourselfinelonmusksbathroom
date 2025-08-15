import os
import time
import math
import random
import crayons
from os import system
import threading

# --- SETTINGS ---
settings = {
    "colorblind_mode": False,
    "music_on": False # Music is always off now
}


def color_text(text, color, bold=False):
    if settings["colorblind_mode"]:
        return crayons.white(text, bold=bold)
    return getattr(crayons, color)(text, bold=bold)

def get_input(prompt):
    user_input = input(prompt).strip().lower()
    if user_input == "settings":
        open_settings_menu()
        return get_input(prompt)
    return user_input

def open_settings_menu():
    print("\n--- SETTINGS MENU ---")
    print("1. Toggle colorblind mode (currently: {})".format(
        "ON" if settings["colorblind_mode"] else "OFF"
    ))
    print("3. Return to game") #Removed music toggle option
    choice = input("Enter 1 or 3: ").strip()
    if choice == "1":
        settings["colorblind_mode"] = not settings["colorblind_mode"]
        print("Colorblind mode is now {}.".format(
            "ON" if settings["colorblind_mode"] else "OFF"
        ))
        open_settings_menu()
    elif choice == "3":
        print("Returning to game...\n")
    else:
        print("Invalid choice. Please try again.")
        open_settings_menu()

# -------------------------------------------

def start_game():
    print("You find yourself in the bathroom of Elon Musk.")
    print("You don't know how you got here.")
    print("The room is filled with mysterious objects.")
    print("There are so many decisions to make.")
    first_choice()

def first_choice(): 
    print("You see a toilet and a mirror. Which one do you want to check out first?")
    print(color_text("1. Check out the toilet. ", "blue", bold=True))
    print(color_text("2. Look in the mirror. ", "blue", bold=True))

    choice = get_input("Enter 1 or 2: ")

    if choice == '1':
        check_toilet()
    elif choice == '2':
        look_mirror()
    else:
        print("Invalid choice. Please try again.")
        first_choice()
        return

def check_toilet():
    print("You walk toward the toilet. It's very high-tech!")
    print("You open the lid and Donald Trump pops out!")
    print("He looks around ... and then ducks back in.")
    print("You decide to move on for now.")
    print(color_text("1. Look in the mirror. ", "blue", bold=True))
    print(color_text("2. Try to leave the bathroom. ", "blue", bold=True))
    print(color_text("3. Inspect the sink. ", "blue", bold=True))
    choice = get_input("Enter 1, 2, or 3: ")

    if choice == '1':
        look_mirror()
    elif choice == '2':
        leave_bathroom()
    elif choice == '3':
        inspect_sink()
    else:
        print("Invalid choice. Please try again.")
        check_toilet()
        return

def look_mirror():
    print("You look in the mirror.")
    print("It says, 'You are not Elon Musk. Therefore, you don't look good.'")
    print("You are quite offended.")
    print("You decide to move on for now.")
    print(color_text("1. Check out the toilet. ", "blue", bold=True))
    print(color_text("2. Try to leave the bathroom. ", "blue", bold=True))
    print(color_text("3. Inspect the sink. ", "blue", bold=True))
    choice = get_input("Enter 1, 2, or 3: ")

    if choice == '1':
        check_toilet()
    elif choice == '2':
        leave_bathroom()
    elif choice == '3':
        inspect_sink()
    else:
        print("Invalid choice. Please try again.")
        look_mirror()
        return

def leave_bathroom():
    print("You decide to leave the bathroom.")
    print("As you try to walk out,")
    print("you realize that there is an invisible forcefield keeping you inside.")
    print("You decide to move on for now.")
    print(color_text("1. Check out the toilet. ", "blue", bold=True))
    print(color_text("2. Look in the mirror. ", "blue", bold=True))
    print(color_text("3. Walk back to where you started. ", "blue", bold=True))
    print(color_text("4. Inspect the sink. ", "blue", bold=True))
    choice = get_input("Enter 1, 2, 3, or 4: ")

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
        return

def inspect_sink():
    print("You walk towards the sink. It's made of pure gold!")
    print("As you turn on the faucet, a hologram of Elon Musk appears.")
    print("He says, 'Welcome to my bathroom. Enjoy your stay!'")
    print("You decide to move on for now.")
    print(color_text("1. Check out the toilet. ", "blue", bold=True))
    print(color_text("2. Look in the mirror. ", "blue", bold=True))
    print(color_text("3. Try to leave the bathroom. ", "blue", bold=True))
    choice = get_input("Enter 1, 2, or 3: ")

    if choice == '1':
        check_toilet()
    elif choice == '2':
        look_mirror()
    elif choice == '3':
        leave_bathroom()
    else:
        print("Invalid choice. Please try again.")
        inspect_sink()
        return

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
    start_game_again_evil_laugh_decision()

def start_game_again_evil_laugh_decision():
    print(color_text("1. Pick up the bar of soap. ", "blue", bold=True))
    print(color_text("2. Turn on the shower. ", "blue", bold=True))
    print(color_text("3. Hit stuff. ", "blue", bold=True))
    choice = get_input("Enter 1, 2, or 3: ")

    if choice == '1':
        pick_up_soap()
    elif choice == '2':
        turn_on_shower()
    elif choice == '3':
        hit_stuff()
    else:
        print("Invalid choice. Please try again.")
        start_game_again_evil_laugh()
        return

def pick_up_soap():
    print("You pick up the bar of soap.")
    print("It splits in two revealing a swastika.")
    print("You smell something strange and then everything goes")
    print(color_text("black.", "black", bold=True))
    print("")
    print("You wake up slowly, groaning.")
    print("The bar of soap is gone.")
    print("You are still stuck in the shower.")
    print(color_text("1. Pick up the bar of soap. ", "blue", bold=True))
    print(color_text("2. Turn on the shower. ", "blue", bold=True))
    print(color_text("3. Hit stuff. ", "blue", bold=True))
    choice = get_input("Enter 1, 2, or 3: ")

    if choice == '1':
        pick_up_soap_again()
    elif choice == '2':
        turn_on_shower()
    elif choice == '3':
        hit_stuff()
    else:
        print("Invalid choice. Please try again.")
        pick_up_soap()
        return

def pick_up_soap_again():
    print("Bruh, who are you?")
    print("Didn't you read the last message?")
    print("There is no soap anymore.")
    print("Just for that I'm adding a plot twist.")
    print("A ton of bars of soap fall on your head, and you start to lose consciousness.")
    print(color_text("1. Don't fight it. ", "blue", bold=True))
    print(color_text("2. Punch the wall. ", "blue", bold=True))
    choice = get_input("Enter 1 or 2: ")

    if choice == '1':
        no_fighty()
    elif choice == '2':
        punch_wall()
    else:
        print("Invalid choice. Please try again.")
        pick_up_soap_again()
        return

def punch_wall():
    print("You punch the wall.")
    print("The wall caves in, and falls on you.")
    print("You never wake up again.")
    print()
    credits()
    print()
    print(color_text("1. Start over.", "blue", bold=True))
    print(color_text("2. Quit. ", "blue", bold=True))
    choice = get_input("Enter 1 or 2: ")

    if choice == '1':
        start_game()
    elif choice == '2':
        print("Goodbye.")
    else:
        print("Invalid choice. Please try again.")
        punch_wall()
        return

def no_fighty():
    print("You wake up in a dark room.")
    print("You hear a voice.")
    print("It says, 'You have been chosen.'")
    print("You are never seen again.")
    print(color_text("THE END. ", "red", bold=True))
    print()
    credits()

def hit_stuff():
    print("What do you want to hit?")
    print(color_text("1. The door. ", "blue", bold=True))
    print(color_text("2. The wall. ", "blue", bold=True))
    print(color_text("3. Yourself. ", "blue", bold=True))
    choice = get_input("Enter 1, 2, or 3: ")

    if choice == '1':
        door_hit()
    elif choice == '2':
        wall_hit()
    elif choice == '3':
        self_hit()
    else:
        print("Invalid choice. Please try again.")
        hit_stuff()
        return

def wall_hit():
    print("You hit the wall.")
    print("It caves in and falls on you.")
    print("You never wake up again.")
    print()
    credits()

def self_hit():
    print("You hit yourself.")
    print("Bro, why would you do that?")
    print("That literally accomplished nothing.")
    print()
    start_game_again_evil_laugh_decision()

def door_hit():
    print("You hit the door.")
    print("It doesn't budge.")
    print("You hear Elon Musk's voice saying, 'Nice try!'")
    print("You are still trapped in the shower.")
    print(color_text("1. Pick up the bar of soap. ", "blue", bold=True))
    print(color_text("2. Turn on the shower. ", "blue", bold=True))
    print(color_text("3. Hit stuff again.", "blue", bold=True))
    choice = get_input("Enter 1, 2, or 3: ")

    if choice == '1':
        pick_up_soap()
    elif choice == '2':
        turn_on_shower()
    elif choice == '3':
        hit_stuff()
    else:
        print("Invalid choice. Please try again.")
        door_hit()
        return

def turn_on_shower():
    print("You turn on the shower. Water starts pouring down!")
    print("You feel refreshed, but you're still trapped.")
    print(color_text("1. Pick up the bar of soap. ", "blue", bold=True))
    print(color_text("2. Hit stuff. ", "blue", bold=True))
    choice = get_input("Enter 1 or 2: ")

    if choice == '1':
        pick_up_soap()
    elif choice == '2':
        hit_stuff()
    else:
        print("Invalid choice. Please try again.")
        turn_on_shower()

def credits():
    print(color_text("Credits:", "red", bold=True))
    print("Created by PianoMan0.")
    print("Thanks for playing!")
    print("Follow me on Github @PianoMan0")
    print("Visit my website: https://pianoman0.com")

if __name__ == "__main__":
    start_game()