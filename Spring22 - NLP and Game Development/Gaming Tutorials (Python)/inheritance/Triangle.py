""" A module to create a Triangle class derived from Polygon class """

from Polygon import Polygon

class Triangle(Polygon):
    """ A class to represent a triangle """

    def print_area(self):
        print(f"This shapes has an area of {self.height * self.width * .5}")
