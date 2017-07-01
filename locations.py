import random

class Location:

    list_of_locations = []

    def __init__(self, loc_name, cur_npcs):
        self.loc_name = loc_name
        self.cur_npcs = cur_npcs

        #add locations to list as you create them, for use in checking if available for travel.
        self.list_of_locations.append(self.loc_name)

    def __str__(self):
        return 'Location: {}'.format(self.loc_name)

class Sheep_Pasture(Location):

    def __init__(self, loc_name, cur_npcs):
        super().__init__(loc_name, cur_npcs)

    looks = {
             "VIEW":
"""
You see before you a familiar sight: 
Farmer Josie's Sheep Pasture.
The wind is blowing through the long stalks of grass, 
and you can just spot the fluffy woolen lumps grazing. 
A single tree defies the rolling field,
providing shade to the nearby sheep.
Many a villager has fallen subject to the temptations of Josie's premium stock,
and you recall your Father's warning from your early childhood.
'RESIST THE FLOCK MY CHILD. THE SINS OF BEASTIAL FLESH ARE HEAVIER THAN THE POWERS THEY GRANT.'              
""",
             "TREE":
"""
The tree is old and mega lush. There's like, whispy vines on it and shit.
The branches creek in response to the sayings of the wind, 
and maybe it's just your imagination, but it looks as if the
fingers of the tree are reaching desperately to the flock below.
""",
             "SHEEP":
"""
The sheep are waving their lusty little tail stumps to and fro,
relentlessly nibbling their way through the slender stalks.
"""
             }

sheep_pasture = Sheep_Pasture("Sheep Pasture", [] )
