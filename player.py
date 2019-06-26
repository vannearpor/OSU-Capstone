
"""
    Class to create and instantiate the player character within the game
"""

class Player:
    def __init__(self):
        self.name = "Ellis"
        self.inventory = []
        self.location = None
        
    def look(self):
        print("You are at the {0}, you scan you environment and look around.".format(self.location.name))
        
        if self.location,familiar == True:
            print("{0}".format(self.location.shortDesc))
        
        if self.location.familiar == False:
            print("{0}".format(self.location.longDesc))
            self.location.familiar = True

    def look_at(self, cmd_item):
        item = None
        if cmd_item:
            for room_item in self.location.items:
                if room_item == cmd_item:
                    item = self.location.items[room_item]
                    break
                    
        else:
            print("That item doesn't exist in this room")

    def take(self, cmd_item):
        item = None
        if cmd_item:
            for room_item in self.location.items:
                if room_item == cmd_item:
                    item = self.location.items[room_item]

        if item is not None:
            if item.can_be_held == True:
                if item.held == False:
                    self.inventory.append(item)
                    item.held = True
                else:
                    print("You are already holding this item")
            else:
                print("This item cannot be held")
        else:
            print("This item does not exist in this room")

    def drop(self, cmd_item):
        item = None
        if cmd_item:
            for held_item in self.inventory:
                if held_item == cmd_item:
                    item = self.inventory[held_item]

        if item is not None:
            self.location.items.append(item)
            self.inventory.remove(item)
            item.held = False

        else:
            print("You cannot drop an item that you do not have in your inventory")

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





