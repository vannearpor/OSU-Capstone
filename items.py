#Item parent class
class Item:
    def __init__(self):
        self.name = None
        self.description = None
        self.can_be_held = None
        self.held = False

#Item child classes
class sword (Item):
    def __init__(self):
        self.name = "sword"
        self.description = "This is a mighty sword to be weld by a warrior, slayer of beasts."
        self.can_be_held = True
        self.held = False
        
class boat (Item):
    def __init__(self):
        self.name = "boat"
        self.description = "An inflatable boat that seems good for traveling across bodies of water."
        self.can_be_held = True
        self.held = False
            
class key (Item):
    def __init__(self):
        self.name = "key"
        self.description = "Shiny gold key. Looks like it may unlock something very important..."
        self.can_be_held = True
        self.held = False

class statue (Item):
    def __init__(self):
        self.name = "statue"
        self.description = "A giant marble statue of a majestic dragon."
        self.can_be_held = False
        self.held = False

class tree (Item):
    def __init__(self):
        self.name = "tree"
        self.description = "A young tree starting to bear fruit."
        self.can_be_held = False
        self.held = False

class cage (Item):
    def __init__(self):
        self.name = "cage"
        self.description = "A dismantled and broken cage. It seems something escaped from inside."
        self.can_be_held = False
        self.held = False

class bones (Item):
    def __init__(self):
        self.name = "bones"
        self.description = "Large pile of old fish bones from previous eaten fish."
        self.can_be_held = False
        self.held = False

class dung (Item):
    def __init__(self):
        self.name = "dung"
        self.description = "Large pile of dung from what seems to be a very large animal... what could have been here?"
        self.can_be_held = False
        self.held = False

class gate (Item):
    def __init__(self):
        self.name = "gate"
        self.description = "Giant wooden gate that has been left open. It seems you may enter as you please."
        self.can_be_held = False
        self.held = False

class sign (Item):
    def __init__(self):
        self.name = "sign"
        self.description = "You examine a written sign right near the gate... \"HOME OF BEHEMOTH\""
        self.can_be_held = False
        self.held = False

class tools (Item):
    def __init__(self):
        self.name = "tools"
        self.description = "These tools are brown, rusty, and dull. They are useless."
        self.can_be_held = False
        self.held = False

class furnace (Item):
    def __init__(self):
        self.name = "furnace"
        self.description = "The furnace is old and cold, maybe weapons and tools were created here."
        self.can_be_held = False
        self.held = False
