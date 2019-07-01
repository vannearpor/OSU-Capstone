import rooms

"""
    Class to create and instantiate the player character within the game
"""

class Player:
    def __init__(self):
        self.name = "Ellis"
        self.inventory = []
        self.location = None
        
    def look(self):
        print()
        print("You are at the {0}, you scan you environment and look around.".format(self.location.name))
        
        if self.location.familiar == True:
            print("{0}".format(self.location.shortDesc))
        
        if self.location.familiar == False:
            print("{0}".format(self.location.longDesc))
            self.location.familiar = True

        if self.location.items:
            print("Here are the contents of the room:\n")
            print("Items:")
            for item in self.location.items:
                print("{0}".format(item.name))

    def look_at(self, cmd_item):
        item = None
        if cmd_item:
            for room_item in self.location.items:
                if room_item == cmd_item:
                    item = room_item
                    break
                    
        else:
            print("That item doesn't exist in this room")

    def take(self, cmd_item):
        item = None
        if cmd_item:
            for room_item in self.location.items:
                print("{0}".format(room_item.name))
                if cmd_item == room_item.name:
                    item = room_item
                    break

        if item:
            if item.can_be_held == True:
                if item.held == False:
                    self.inventory.append(item)
                    item.held = True
                    self.location.items.remove(item)
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
                if cmd_item == held_item.name:
                    item = held_item

        if item:
            self.location.items.append(item)
            item.held = False
            self.inventory.remove(item)

        else:
            print("You cannot drop an item that you do not have in your inventory")

    def view_inventory(self):
        #prints item in the inventory list
        print()
        print("Here are the items you are currently holding in your inventory:")
        if self.inventory:
            for item in self.inventory:
                print("{0}".format(item.name))
                print()

        else:
            print("NONE. You currently have no items in your inventory.")
            print()

    def fight(self, character):
        if self.location.name == "Behemoth's Castle" and self.location.characters:
            if character == "behemoth":
                has_sword = False
                for item in self.inventory:
                    if item.name == "sword":
                        has_sword = True
                        print("You stare the Behemoth in the eyes as he roars in rage. You brandish your sword and get prepared for battle!")
                        print("You fight with all your might in a long grueling dual, you dodge all of Behemoth's attacks. Due to his large stature, he will surely knock you out!")
                        print("He lowers his neck and tries to breathe fire on you. You quickly somersault out of the way and grab onto his neck!")
                        print("Behemoth tries to wiggle out off but your grip is tight!")
                        print("You take your blade and swipe it across his neck! He lets out a loud cry and falls to the ground")
                        print("Behemoth lays motionless and you put away your sword. The Dungeon is now unguarded and free for you to enter...")
                        self.location.characters.pop()
                        break
                if has_sword == False:
                    print("You don't have a weapon to fight the Behemoth! HE'S HUGE. Come back and fight Behemoth when you find a weapon!")
            else:
                print("Error. Invalid character to fight.")
        else:
            print("There is no one to fight here.")
        #check if in right room
            #check if character is Behemoth
                #check if you have a sword in inventory
                    #print defeat behemoth.
                    #behemoth removed from map
                    #allow user to enter princess room

    def go_north(self):
        #grab players current location
        #go into room object and see what the north room is
        if self.location.name == "Castle Grass Lawn":
            has_key = False
            for item in self.inventory:
                if item.name == "key":
                    has_key = True
                    self.location = self.location.north_room
                    print("You use your key on the Castle door. *click* It unlocks...")
                    break
            if has_key == False:
                print("You walk up to the Castle doors... it is locked... You see a keyhole. Maybe there is a key lying around somewhere...")

        else:
            if self.location.north_room is not None:
                self.location = self.location.north_room
            #if room available

            else:
                print("There is nowhere to go north of {0}".format(self.location.name))
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
            print("There is nowhere to go south of {0}".format(self.location.name))

    def go_west(self):
        #grab players current location
        #go into room object and see what the north room is
        if self.location.west_room is not None:
            self.location = self.location.west_room
        #if room available
        
        else:
            print("There is nowhere to go west of {0}".format(self.location.name))

    def go_east(self):
        #grab players current location
        #go into room object and see what the north room is
        if self.location.name == "Castle Grass Lawn":
            has_boat = False
            for item in self.inventory:
                if item.name == "boat":
                    has_boat = True
                    self.location = self.location.east_room
                    print("You set up your boat and get ready to cross the lake.")
                    break
    
            if has_boat == False:
                print("You look East and there is a lake blocking you from getting to the other side. Maybe you can find a boat somewhere...")

        else:
            if self.location.east_room is not None:
                self.location = self.location.east_room
        #if room available
        
            else:
                print("There is nowhere to go east of {0}".format(self.location.name))

    #place this function in game file - def help(self):
        #print out list of verbs that the user can use and some brief descriptions





