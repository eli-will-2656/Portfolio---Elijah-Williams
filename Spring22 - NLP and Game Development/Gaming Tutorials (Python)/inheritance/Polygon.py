""" A module to define a regular Polygon base class """

class Polygon:
    """ A class to represent a regular polygon """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_shape(self):
        print(f"This shape has a width of {self.width} and a height of {self.height}")
