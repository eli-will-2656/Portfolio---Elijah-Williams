""" This script will create some instances of the Player class """

import class2

# Creating player object named elijah
elijah = class2.Player("Elijah Williams", 19, 124)

elijah.print_player()

isaiah = class2.Player("Isaiah Williams", 19, -1)

isaiah.print_player()

print("Number of player objects:", class2.Player.num_players)
