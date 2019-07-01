
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
        self.name = "behemoth"
        self.dialogue = "\"You will never be able to save your partner Lyn.\""
        self.alive = True

class partner (Character):
    def __init__(self):
        self.name = "lyn"
        self.dialogue = "\"ELLIS YOU FOUND ME. Lets go home.\""
        self.alive = True

class fisherman (Character):
    def __init__(self):
        self.name = "fisherman"
        self.dialogue = "\"A fair warning... this land belongs to a great beast. It often comes lakeside to feast on fish within these waters.\""
        self.alive = True

class elder (Character):
    def __init__(self):
        self.name = "elder"
        self.dialogue = "\"A heavy golden sword was found here long ago... I haven't the energy to move it. It has been in this forest for as long as I can remember.\""
        self.alive = True
