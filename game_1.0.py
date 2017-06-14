import random

#global variables
days_left = 10

#parent classes
class Location:

    list_of_locations = []

    def __init__(self, loc_name, cur_npcs, mechanics, items):
        self.loc_name = loc_name
        self.cur_npcs = cur_npcs
        self.mechanics = mechanics
        self.items = items

        self.list_of_locations.append(self.loc_name)

    def sights(self):
        print("You see")
        for thing in self.mechanics:
            print("{}".format(thing), end=", ")
        print("")
        for entity in self.cur_npcs:
            print("{}".format(entity.name), end=", ")
        print("")


class NPC:

    def __init__(self, name, age, sex, str, dex, con, int, wis, cha, location, backpack):
        self.name = name
        self.age = age
        self.sex = sex
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.location = location
        self.backpack = backpack

    def look(self):
        self.location.sights()

    def pick_up(self):
        pass

    def use(self):
        pass

    def talk(self):
        pass

    def attack(self):
        pass

    def travel(self, new_loc):
        if new_loc == "TOWN SQUARE":
            self.location = town_square
        elif new_loc == "SHEEP PASTURE":
            self.location = sheep_pasture
        elif new_loc == "BLACKSMITH":
            self.location = blacksmith


class Player(NPC):
#player subclass

    def __init__(self, name, age, sex, str, dex, con, int, wis, cha, location, backpack):
        super().__init__(name, age, sex, str, dex, con, int, wis, cha, location, backpack)

    def commands(self):
        print("""
  _________________
/\                 \  
\_|    commands    |  
  |    location    |
  |    inventory   |
  |    stats       |
  |    look        |
  |    pick up     |
  |    use         |
  |    talk        | 
  |    attack      |          
  |  ______________|_ 
  \_/_______________/    
    
    """)

    def cur_loc(self):
        print(self.location.loc_name)

    def inventory(self):
        print(self.backpack)

    def stats(self):
            print("""
Name = {}
Str = {}
Dex = {}
Con = {}
Int = {}
Wis = {}
Cha = {}
        """.format(self.name, self.str, self.dex, self.con, self.int, self.wis, self.cha))

    def action(self):
    #main loop for player
        global days_left

        while True:
            print("You have {} days left until the REAL_BAD_DUDES show up".format(days_left))
            print("What now?")
            action = input("༼☉ɷ⊙༽ > ").upper()
            if action == "COMMANDS":
                self.commands()
            elif action == "LOCATION":
                self.cur_loc()
            elif action == "INVENTORY":
                self.inventory()
            elif action == "STATS":
                self.stats()
            elif action == "LOOK":
                self.look()
            elif action == "PICK UP" or action == "PICKUP":
                self.pick_up()
            elif action == "USE":
                self.use()
            elif action == "TALK":
                self.talk()
            elif action == "ATTACK":
                self.attack()
            elif action == "TRAVEL":
                print(Location.list_of_locations)
                where_to = input("Travel where? ").upper()
                print(where_to)
                if where_to in Location.list_of_locations:
                    days_left -= .25
                    self.travel(where_to)
                else:
                    print("That isn't a valid location to travel")
            else:
                print("That's not a valid command")

#JUST FUCKIN AROUND WITH CREATING INSTANCES AND FUNCTIONALITY
farmer_bob = NPC("Farmer Bob", 72, "male", 13, 9, 17, 5, 5, 3, None, None)
hilda = NPC("Hilda", 35, "female", 18, 8, 18, 11, 13, 8, None, None)

town_square = Location("TOWN SQUARE", [farmer_bob, hilda], ["gallows", "manure cart"], ["pitchfork", "rock"])
sheep_pasture = Location("SHEEP PASTURE", [], ["Sheep"], [])
blacksmith = Location("BLACKSMITH", [], ["Anvil"], ["hammer"])

THEPLAYER = Player("Insert_Player_Name_lols", 25, "male-ish", 12, 16, 15, 15, 13, 15, town_square, [])

THEPLAYER.action()

