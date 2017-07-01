import random
from characters import *

days_left = 10
#design character creation stuff here

the_player = Character("testChar", 15, 15, 15, 15, 15, 15, sheep_pasture, [])

while True:
    print("You have {} days left until the REAL_BAD_DUDES show up".format(days_left))
    print("What now?")
    action = input("༼☉ɷ⊙༽ > ").upper()

    if action == "COMMANDS":
        the_player.commands()

    elif action == "LOCATION":
        the_player.cur_loc()

    elif action == "INVENTORY":
        the_player.inventory()

    elif action == "STATS":
        the_player.stats()

    elif action == "LOOK":
        the_player.look()

    elif action == "PICK UP" or action == "PICKUP":
        the_player.location.pick_up()

    elif action == "USE":
        the_player.use()

    elif action == "TALK":
        the_player.talk()

    elif action == "ATTACK":
        the_player.attack()

    elif action == "TRAVEL":
        where_to = input("Travel where? ").upper()
        if where_to in Location.list_of_locations:
            days_left -= .25
            the_player.travel(where_to)
        else:
            print("That isn't a valid location to travel")

    else:
        print("That's not a valid command")
