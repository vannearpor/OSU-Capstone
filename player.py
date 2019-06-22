
"""
    Class to create and instantiate the player character within the game
"""

class Player:
    def __init__(self):
        self.name = "Ellis"
        self.inventory = []
        self.location = None
        
    def look(self):
        #grabs location room description

    def look_at(self, item):
        #if player location is in room1:
            #if item is in room1 item list:
                #then bring up item description

        #else if player location is in room2:
            #etc.

    def take(self, item):
        #if player location is in room1:
            #if item is in room1 item list:
                #check if item_taken is false:
                    #if is, take item
                #else
                    #you already have item

        #else if player location is in room2:
            #etc.

    def drop(self, item):
        #if player has item:
            #remove from inventory, item is taken is false, enter item in current room inventory

    def view_inventory(self):
        #prints item in the inventory list

    def fight(self, item, character):
        #check if in right room
            #check if character is Behemoth
                #check if you have a sword in inventory
                    #print defeat behemoth.
                    #behemoth removed from map
                    #allow user to enter princess room

    def go_north(self):
        #grab players current location
        #go into room object and see what the north room is
        #if room available
            #print description of going into new room, set player's location to new room
            #initiate player look, print description
            #print items seen in the room

    def go_south(self):

    def go_west(self):

    def go_east(self):

    #place this function in game file - def help(self):
        #print out list of verbs that the user can use and some brief descriptions





