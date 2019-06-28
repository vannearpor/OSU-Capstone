
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
        print()
        print("Here are the items you are currently holding in your inventory:")
        print()
        
        if self.inventory:
            for item in self.inventory:
                print("{0}".format(item.name))
                print()

        else:
            print("NONE. You currently have no items in your inventory.")
            print()

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
        if self.location.north_room is not None:
            self.location = self.location.north_room
        #if room available

        else:
            print("There is nowhere to go north of {0}".format.self.location)
            #print description of going into new room, set player's location to new room
            #initiate player look, print description
            #print items seen in the room

    def go_south(self):
        #grab players current location
        #go into room object and see what the north room is
        if self.location.south_room is not None:
            self.location = self.location.south_room
        #if room available
        
        else:
            print("There is nowhere to go south of {0}".format.self.location)

    def go_west(self):
        #grab players current location
        #go into room object and see what the north room is
        if self.location.west_room is not None:
            self.location = self.location.west_room
        #if room available
        
        else:
            print("There is nowhere to go west of {0}".format.self.location)

    def go_east(self):
        #grab players current location
        #go into room object and see what the north room is
        if self.location.east_room is not None:
            self.location = self.location.east_room
        #if room available
        
        else:
            print("There is nowhere to go east of {0}".format.self.location)

    #place this function in game file - def help(self):
        #print out list of verbs that the user can use and some brief descriptions





