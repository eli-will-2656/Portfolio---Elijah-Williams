""" A module to create a Rectangle class derived from Polygon class """

from Polygon import Polygon

class Rectangle(Polygon):
    """ A class to represent a rectangle object """

    def set_shape(self, isSquare):
        self.isSquare = isSquare

    def diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def isSquare(self):
        return isSquare
