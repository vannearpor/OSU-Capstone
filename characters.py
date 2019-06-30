
"""
    Class to create and instantiate characters within the game
"""

class Character:
    def __init__(self):
        self.name = None
        self.dialogue = None
        self.alive = True

class behemoth (Character):
    def __init__(self):
        self.name = "Behemoth"
        self.dialogue = "\"You will never be able to save your partner Lyn.\""
        self.alive = True

    def interact(self):
        print(self.dialogue)

class lyn (Character):
    def __init_(self):
        self.name = "Lyn"
        self.dialogue = "\"Ellis you did it! You saved me! Let's get back to town\""
        self.alive = True

    def interact(self):
        print(self.dialogue)

class fisherman (Character):
    def __init__(self):
        self.name = "Fisherman"
        self.dialogue = "\"A fair warning... this land belongs to a great beast. It often comes lakeside to feast on fish within these waters.\""
        self.alive = True

    def interact(self):
        print(self.dialogue)

class elder (Character):
    def __init__(self):
        self.name = "Forest Elder"
        self.dialogue = "\"A heavy golden sword was found here long ago... I haven't the energy to move it. It has been in this forest for as long as I can remember.\""
        self.alive = True
    
    def interact(self):
        print(self.dialogue)

