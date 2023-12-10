""" A module to implement a bird class """


class Bird:
    """ A base class to define bird properties """ # Doc string that will be stored as __doc__ attribute of class

    num_birds = 0

    def __init__(self, name, squak):
        self.name = name
        self.squak = squak
        Bird.num_birds += 1

    def print(self):
        print("{} says {}".format(self.name, self.squak))


harry = Bird("harry", "yeehaha")

harry.print()

print("Number of Bird instances in the cage:", Bird.num_birds)

esmeralda = Bird('esmeralda', 'cooocoocoo')

esmeralda.print()

print("Number of Bird instances in the cage:", Bird.num_birds)
