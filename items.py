#Item parent class
class Item:
    def __init__(self):
        self.name = None
        self.description = None
        self.can_be_held = None
        self.held = False

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description)

#Item child classes
class sword (Item):
    def __init__(self):
        self.name = "Sword of Reckoning"
        self.description = "This is a mighty sword to be weld by a warrior, slayer of beasts."
        self.can_be_held = True
        self.held = False
        
class boat (Item):
    def __init__(self):
        self.name = "Inflatable Boat"
        self.description = "An inflatable boat that seems good for traveling across bodies of water."
        self.can_be_held = True
        self.held = False
            
class key (Item):
    def __init__(self):
        self.name = "Castle Key"
        self.description = "Shiny gold key. Looks like it may unlock something very important..."
        self.can_be_held = True
        self.held = False

class statue (Item):
    def __init__(self):
        self.name = "Dragon Statue"
        self.description = "A giant marble statue of a majestic dragon."
        self.can_be_held = False
        self.held = False

class tree (Item):
    def __init__(self):
        self.name = "Forest Tree"
        self.description = "A young tree starting to bear fruit."
        self.can_be_held = False
        self.held = False

class cage (Item):
    def __init__(self):
        self.name = "Empty Cage"
        self.description = "A dismantled and broken cage. It seems something escaped from inside."
        self.can_be_held = False
        self.held = False

class bones (Item):
    def __init__(self):
        self.name = "Pile of Fish Bones"
        self.description = "Large pile of old fish bones from previous eaten fish."
        self.can_be_held = False
        self.held = False

class dung (Item):
    def __init__(self):
        self.name = "Pile of Animal Dung"
        self.description = "Large pile of dung from what seems to be a very large animal... what could have been here?"
        self.can_be_held = False
        self.held = False

class gate (Item):
    def __init__(self):
        self.name = "Castle Gate"
        self.description = "Giant wooden gate that has been left open. It seems you may enter as you please."
        self.can_be_held = False
        self.held = False

class sign (Item):
    def __init__(self):
        self.name = "Written Sign"
        self.description = "You examine a written sign right near the gate... \"HOME OF BEHEMOTH\""
        self.can_be_held = False
        self.held = False

class tools (Item):
    def __init__(self):
        self.name = "Rusty Tools"
        self.description = "These tools are brown, rusty, and dull. They are useless."
        self.can_be_held = False
        self.held = False

class furnace (Item):
    def __init__(self):
        self.name = "Dusty Furnace"
        self.description = "The furnace is old and cold, maybe weapons and tools were created here."
        self.can_be_held = False
        self.held = False
