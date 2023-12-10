""" In this module, we will be creating an example class called player """


class Player:
    """ This class is used to create a soccer player, with attributes such as
    age and goals_scored """ # This is a docstring that will be stored the __doc__ attribute of this class

    num_players = 0  # This is a class variable that belongs to the class, and can be accessed by any class instance

    def __init__(self, name, age, goals_scored):

        self.name = name
        self.age = age
        self.goals_scored = goals_scored

        Player.num_players += 1

    def print_player(self):
        format = "{} is a famous soccer player who is currently {} years old, and has scored {} goals in their career."

        print(format.format(self.name, self.age, self.goals_scored))
