#This game file will utilize the parser and initiate the actions commanded by the user

import sys
import os
import datetime
import subprocess
import time

import termios import tcflush, TCIFLUSH

import parse
import player
import rooms
import items
import characters

action_cmd = parse.Parser.ACTIONLIST
direction_cmd = parse.Parser.DIRECTIONLIST

def user_input():
    tcflush(sys.stdin, TCIFLUSH)
    cmd = input("Please enter your next move:\n")
    return cmd

class Game(object):
    def __init__(self, player = None):
        if player:
            self.player = player
        self.rooms = []
        self.items = []
        self.characters = []

    def play(self):
        game_parser = Parser()
        current_location = None

        run_game = True
        while run_game:
            current_location = self.player.location
            print("You are currently in room {0}".format(current_room.name))
            print()
            if current_location.familiar == False:
                print("{0}".format(current_location.longDesc))
                print()
                current_location.familiar = True

            else:
                print("{0}".format(current_location.shortDesc))
                print()

            print("Here are the contents of the room:\n")

            print("Items:")
            if current_location.items:
                for item in current_location.items:
                    print(" {0}".format(item.name))
            else:
                print("There are currently no items in this room.\n")
            print()

            print("Characters:")
            if current_location.characters:
                for char in current_location.characters:
                    print(" {0}".format(char.name))

            user_cmd = user_input()

            user_action, user_direction, user_item, user_char = Parser.parse_command(user_cmd)

            if user_action == "go":
                if user_direction:
                    if user_direction == "north":
                        self.player.go_north()
                    elif user_direction == "south":
                        self.player.go_south()
                    elif user_direction == "west":
                        self.player.go_west()
                    elif user_direction == "east":
                        self.player.go_east()
                    else:
                        print("Your directions weren't clear. Please specify: north, south, west, or east.")
                        print()
                else:
                    print("When using the \"go\" action, please specify a direction: north, south, west, or east.")
                    print()

            if user_action == "look":
                self.player.look()

            if user_action == "take":
                if user_item:
                    self.player.take(user_item)

            if user_action == "drop":
                if user_item:
                    self.player.drop(user_item)

            if user_action == "view":
                self.player.view_inventory()

            if user_action == "help":
            #insert list of possible actions here

            if user_action == "quit":
                print("Shutting down...")
                return



