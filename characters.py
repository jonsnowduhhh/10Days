from locations import *

class Character:
    def __init__(self, name, str, dex, con, int, wis, cha, location, backpack):
        self.name = name
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.location = location
        self.backpack = backpack

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
        print("")
        print(self.location)

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

    def look(self):
        look_at_what = input("Look at what? ").upper()
        for key, value in self.location.looks.items():
            match = False
            if match == False:
                if look_at_what == key:
                    print(value)
                    match = True
                else:
                    continue
            else:
                break

    def pick_up(self):
        pass

    def use(self):
        pass

    def talk(self):
        pass

    def attack(self):
        pass

    def travel(self, new_loc):
        #use dict here to simplify code, like the look function
        if new_loc == "TOWN SQUARE":
            self.location = town_square
        elif new_loc == "SHEEP PASTURE":
            self.location = sheep_pasture
        elif new_loc == "BLACKSMITH":
            self.location = blacksmith

