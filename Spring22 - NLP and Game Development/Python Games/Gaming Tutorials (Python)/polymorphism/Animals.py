""" A module implementing a duck class """

class Duck:
    def print_me(self):
        print(self)

    def talk(self):
        print("\nDuck Says: Quack!")

    def coat(self):
        print("Duck Wears: A suit")

"""Method overloading is not supported by Python
(in which methods can have the same name but different arguments),
You will receive a positional argument error.
This is likely not supported because Python is a dynamically-typed language
"""
#    def coat(self, str):

#        print(f"Duck Wears: {str}")

class Mouse:

    def talk(self):
        print("\nMouse Says: Screech!")

    def coat(self):
        print("Mouse Wears: Fur")
