import os
import sys

from game import Game
from parse import Parser
from player import Player
import rooms
import items
import characters

class Eden(Game):
    def __init__(self):
        Game.__init__(self)

    #def introduction(self):
    #write and print game intro here

def main():
    eden_instance = Eden()

    print("Welcome to Eden - The Adventure Game")
    print()

    existing_file = False
    is_valid = True
    
    #forever loops until options 1 & 2 causes a break
    while True:
        if is_valid is not True:
            is_valid = True

        print("Please select a number from the game options below.")
        print("(1) Play New Adventure Mode")
        print("(2) Load Saved Game")
        print("(3) Exit & Shutdown")
        user_input = input(":")

        if user_input in ["1", "2", "3"]:
            if user_input == "1":
                print("--- Starting Eden - The Adventure Game ---")
                print()
                print("Hi Ellis...")
                print("A week ago your village was attacked by a mighty beast named Behemoth. You and your partner Lyn were the top warriors protecting your village.")
                print("Your partner Lyn went off to battle before you even knew the village was being attacked... she said she couldn't wait for you, she needed to save the village.")
                print("The witnessing villagers say Lyn was close to defeating the Behemoth, but it was too strong.")
                print("Upon defeating your partner Lyn, the Behemoth flew off... taking Lyn with it.")
                print("The moment you found out you set on a journey to find Lyn... you stumble upon a large Castle... I think you've found the Behemoth and Lyn.")
                print()
                print("STARTING NOTE: TYPE IN \"help\" AND PRESS ENTER FOR A LIST OF COMMANDS")
                eden_instance.initialize()
                break

            elif user_input == "2":
                #Save game function here
                break
            elif user_input == "3":
                sys.exit()

        else:
            print("Your choice was not valid. Please select the number of your choice -")
            print()
            is_valid = False

    eden_instance.play()

if __name__ == "__main__":
    main()
