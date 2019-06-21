import items

#Room parent class
class Room:
    def __init__(self):
        self.name = "Template"
        self.north_room = None
        self.south_room = None
        self.east_room = None
        self.west_room = None
        self.items = []
        self.characters = []

#Actual Rooms
class Gateway(Room):
    def __init__(self):
        self.name = "Template"
        self.north_room = None
        self.south_room = None
        self.east_room = None
        self.west_room = None
        self.items = []
        self.characters = []

class Lawn(Room):
    def __init__(self):
        self.name = "Castle Grass Lawn"
        self.north_room = None
        self.south_room = None
        self.east_room = None
        self.west_room = None
        self.items = []
        self.characters = []

class Lakeside(Room):
    def __init__(self):
        self.name = "Lakeside"
        self.north_room = None
        self.south_room = None
        self.east_room = None
        self.west_room = None
        self.items = []
        self.characters = []

class Forest(Room):
    def __init__(self):
        self.name = "Forest"
        self.north_room = None
        self.south_room = None
        self.east_room = None
        self.west_room = None
        self.items = []
        self.characters = []

class Shed(Room):
    def __init__(self):
        self.name = "Abandoned Shed"
        self.north_room = None
        self.south_room = None
        self.east_room = None
        self.west_room = None
        self.items = []
        self.characters = []

class Castle(Room):
    def __init__(self):
        self.name = "Template"
        self.north_room = None
        self.south_room = None
        self.east_room = None
        self.west_room = None
        self.items = []
        self.characters = []

class Castle_Room(Room):
    def __init__(self):
        self.name = "Template"
        self.north_room = None
        self.south_room = None
        self.east_room = None
        self.west_room = None
        self.items = []
        self.characters = []
