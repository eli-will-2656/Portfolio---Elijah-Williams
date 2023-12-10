# This code below will generate an error saying:
#	typeError: Module object not callable
#	Wait, are modules objects????
"""
import demo

object = demo()

print(object.i)
"""

# This is because we are not importing the class the correct way

from demo import demo

object = demo()

print(object.i)

# This should be correct