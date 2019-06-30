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

#Load characters into rooms
behemoth = characters.behemoth()
lyn = characters.lyn()
fisherman = characters.fisherman()
elder = characters.elder()

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
        self.longDesc = "You walk up the gravel path and stop in your tracks. You look up ahead North and you see a great big wooden gate. It looks like it should be closed, but you noticed it is cracked open."
        self.shortDesc = "You are standing in front of the open wooden gate."
        self.familiar = False
        self.north_room = None
        self.south_room = None
        self.east_room = None
        self.west_room = None
        self.items = [gate, sign]
        self.characters = []

class Lawn(Room):
    def __init__(self):
        self.name = "Castle Grass Lawn"
        self.longDesc = "Although you are unarmed, you decide to step through the open wooden gates. Once inside, you find yourself in a huge grassy field. This place is beautiful and maintained well. Ahead at the end of the field you see an enormous Castle... You suspect Lyn might be there."
        self.shortDesc = "You are standing in the middle of a huge grassy lawn."
        self.familiar = False
        self.north_room = None
        self.south_room = None
        self.east_room = None
        self.west_room = None
        self.items = [statue, boat]
        self.characters = []

class Lakeside(Room):
    def __init__(self):
        self.name = "Lakeside"
        self.longDesc = "You row across the lake and get to the other side, you hop off the boat lakeside and pack up your boat. You hear the water flowing, birds are whistling, this also looks like a great place to fish."
        self.shortDesc = "You are standing on the side of the lake on wet stones."
        self.familiar = False
        self.north_room = None
        self.south_room = None
        self.east_room = None
        self.west_room = None
        self.items = [bones, dung]
        self.characters = []

class Forest(Room):
    def __init__(self):
        self.name = "Forest"
        self.longDesc = "You leave the lawn and find yourself in a very dense forest. The trees are large and you see animals rustling in the leaves. You take a look around and the first thing you see is a broke cage... odd... looks like something or someone escaped."
        self.shortDesc = "You are standing in the middle of the dense forest."
        self.familiar = False
        self.north_room = None
        self.south_room = None
        self.east_room = None
        self.west_room = None
        self.items = [tree, cage, sword]
        self.characters = []

class Shed(Room):
    def __init__(self):
        self.name = "Abandoned Shed"
        self.longDesc = "You find yourself in front of the abandoned shed, the door is unlocked... you walk yourself in and cough at the quick breathe filled with dust and cobwebs. It's very dim with the single ray of sunlight coming from the window. There are a lot of old things in here."
        self.shortDesc = "You find yourself in the dusty shed."
        self.familiar = False
        self.north_room = None
        self.south_room = None
        self.east_room = None
        self.west_room = None
        self.items = [tools, furnace]
        self.characters = []

class Castle(Room):
    def __init__(self):
        self.name = "Behemoth's Castle"
        self.longDesc = ""
        self.shortDesc = ""
        self.familiar = False
        self.north_room = None
        self.south_room = None
        self.east_room = None
        self.west_room = None
        self.items = []
        self.characters = [behemoth]

class Dungeon(Room):
    def __init__(self):
        self.name = "Prisoner's Dungeon"
        self.longDesc = ""
        self.shortDesc = ""
        self.familiar = False
        self.north_room = None
        self.south_room = None
        self.east_room = None
        self.west_room = None
        self.items = []
        self.characters = [lyn]
