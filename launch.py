import os
import sys
import time

import parse
import player
import rooms
import items
import characters

class Eden(Game):
    def __init__(self, player):
        Game.__init__(self, player)

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

    eden_instance.start()

if __name__ == "__main__":
    main()
