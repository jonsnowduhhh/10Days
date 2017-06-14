import os

#Class templates
class Weapon:

    def __init__(self, name, type, damage, speed, special):
        self.name = name
        self.type = type
        self.damage = damage
        self.speed = speed
        self.special = special

    def display_weapon(self):
        print("""
        Name = {}
            Type = {}
            Damage = {}
            Speed = {}
            Special = {}
        """.format(self.name, self.type, self.damage, self.speed, self.special))


class Character:

    def __init__(self, name, job, str, dex, con, int, wis, cha, backpack):
        self.name = name
        self.job = job
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.backpack = backpack

    def stats(self):
        print("""
Job = {}
Str = {}
Dex = {}
Con = {}
Int = {}
Wis = {}
Cha = {}
        """.format(self.job, self.str, self.dex, self.con, self.int, self.wis, self.cha))

    def inventory(self):
        bindex = 0
        for item in self.backpack:
            Weapon.display_weapon(self.backpack[bindex])
            bindex += 1



    def pick_up(self, item):
        self.backpack.append(item)

#WeaponInstances
club = Weapon("Club", "bludgeoning", 11, 4.0, None)
wand = Weapon("Wand", "sparkling", 5, 8.0, "Hypnotize")
spatula = Weapon("Spatula", "Smacking", 2, 6.0, None)

#Character Instances
Jingo = Character("Jingo Nadi", "asciiMage", 15, 15, 14, 13, 11, 14, [])
Luka = Character("Luka Moth", "wandermaticer", 11, 15, 12, 15, 14, 14, [])


#Application Functions
def commands():
    print("""
  _________________
/\                 \  
\_|      move      |  
  |      look      |
  |      stats     |
  |    inventory   |
  |       use      |
  |  ______________|_ 
  \_/_______________/
    """)

def game_loop():

    startup_counter = 1
    while True:
        if startup_counter >0:
            print("You, being the master of fates, are tasked with these humanoids.")
            print("What shall you do with them?")
            user_input = input("༼ つ ◕_◕ ༽つ").upper()
            startup_counter -= 1
        else:
            print("What  now?")
            user_input = input("༼ つ ◕_◕ ༽つ").upper()

        if user_input == "STATS":
            whose_stats = input("Who? ").upper()
            if whose_stats == "JINGO":
                Jingo.stats()
            elif whose_stats == "LUKA":
                Luka.stats()
            else:
                print("That is no one that you have control of")
        elif user_input == "INVENTORY":
            whose_inventory = input("Whose? ").upper()
            if whose_inventory == "JINGO":
                Jingo.inventory()
            if whose_inventory == "LUKA":
                Luka.inventory()
        elif user_input == "PICK UP":
            who_pickup = input("Who? ").upper()
            if who_pickup == "JINGO":
                pickup_what = input("What? ").upper()
                if pickup_what == "SPATULA":
                    Jingo.pick_up(spatula)
                elif pickup_what == "CLUB":
                    Jingo.pick_up(club)
                elif pickup_what == "WAND":
                    Jingo.pick_up(wand)
                else:
                    print("Nothing like that around...")
            else:
                print("not a valid character")
        else:
            print("NO!! NOT VALID!")

game_loop()


