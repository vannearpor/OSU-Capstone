#Item parent class
class Item:
    def __init__(self, name, description, can_be_held, held):
        self.name = name
        self.description = description
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
