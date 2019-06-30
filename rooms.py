import items
import characters

#Load items into rooms
sword = items.sword()
boat = items.boat()
key = items.key()
statue = items.statue()
tree = items.tree()
cage = items.cage()
bones = items.bones()
dung = items.dung()
gate = items.gate()
sign = items.sign()
tools = items.tools()
furnace = items.furnace()

#Room parent class
class Room:
    def __init__(self):
        self.name = None
        self.longDesc = None
        self.shortDesc = None
        self.familiar = False
        self.north_room = None
        self.south_room = None
        self.east_room = None
        self.west_room = None
        self.items = []
        self.characters = []

#Actual Rooms
class Gate(Room):
    def __init__(self):
        self.name = "Castle Gates"
        self.longDesc = ""
        self.shortDesc = ""
        self.familiar = False
        self.north_room = "Lawn" #replace
        self.south_room = None
        self.east_room = None
        self.west_room = "Shed" #replace
        self.items = [gate, sign]
        self.characters = []

class Lawn(Room):
    def __init__(self):
        self.name = "Castle Grass Lawn"
        self.longDesc = ""
        self.shortDesc = ""
        self.familiar = False
        self.north_room = "Castle"
        self.south_room = "Gate"
        self.east_room = "Lakeside"
        self.west_room = "Forest"
        self.items = [statue]
        self.characters = []

class Lakeside(Room):
    def __init__(self):
        self.name = "Lakeside"
        self.longDesc = ""
        self.shortDesc = ""
        self.familiar = False
        self.north_room = None
        self.south_room = None
        self.east_room = None
        self.west_room = "Lawn"
        self.items = [bones, dung]
        self.characters = []

class Forest(Room):
    def __init__(self):
        self.name = "Forest"
        self.longDesc = ""
        self.shortDesc = ""
        self.familiar = False
        self.north_room = None
        self.south_room = None
        self.east_room = "Lawn"
        self.west_room = None
        self.items = [tree, cage, sword]
        self.characters = []

class Shed(Room):
    def __init__(self):
        self.name = "Abandoned Shed"
        self.longDesc = ""
        self.shortDesc = ""
        self.familiar = False
        self.north_room = None
        self.south_room = None
        self.east_room = "Gate"
        self.west_room = None
        self.items = ["boat"]
        self.characters = [tools, furnace]

class Castle(Room):
    def __init__(self):
        self.name = "Template"
        self.longDesc = ""
        self.shortDesc = ""
        self.familiar = False
        self.north_room = None
        self.south_room = "Lawn"
        self.east_room = None
        self.west_room = "Castle_Room"
        self.items = []
        self.characters = ["behemoth"]

class Castle_Room(Room):
    def __init__(self):
        self.name = "Template"
        self.longDesc = ""
        self.shortDesc = ""
        self.familiar = False
        self.north_room = None
        self.south_room = None
        self.east_room = "Castle"
        self.west_room = None
        self.items = []
        self.characters = ["Lyn"]
