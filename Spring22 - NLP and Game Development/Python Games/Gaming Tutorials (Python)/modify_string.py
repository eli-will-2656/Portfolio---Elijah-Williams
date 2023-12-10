""" This module contains examples of string methods that can be used to return modified strings """


# This shows the method only returns a copy of the string
s1 = "Hello world"
print(s1.lower())
print(s1)

# At the end of every prompt passes into input function, make sure to include a colon and a space
exit = input("Do you want to continue in this program (y/n): ")

if exit.lower().startswith("y"):
  print("\nThat's great!")

spacy_string = "                      this is the first word"

print(spacy_string)
print(spacy_string.strip())

name = input("Please enter your full name: ")
print("Hello", name.title())
print()
