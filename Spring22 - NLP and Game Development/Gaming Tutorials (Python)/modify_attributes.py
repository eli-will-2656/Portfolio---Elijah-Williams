""" This module creates a simple base class with no attributes, and adds attributes to the instances of the class"""

class Empty():
    """An empty class containing no class methods (other than __init__), variables, or attributes """

    def __init__(self):
        pass


bob = Empty()

bob.name = "Bob"
bob.age = 32

setattr(bob, 'coder', False)

print(bob.__dir__)

"""
print("bob's attributes")
print(dir(bob))

for attribute in dir(bob):
    if attribute[0] != '_':
        print("Attribute:", attribute, "\t\tValue:\t", getattr(bob, attribute))

del bob.name
delattr(bob, 'age')

print()

for attribute in dir(bob):
    if attribute[0] != '_':
        print("Attribute:\t", attribute, "Value:\t", getattr(bob, attribute))
"""
