"""In this module, we will be practicing string formatting, which can be accomplished in two ways:
    (1) Using {} for field replacements
    (2) Using %s for string field replacements
"""

# This is to practice python-style formatting
def add_punctuation(str1, str2):
    """Concatenates two strings, adding a period to the first and a question mark to the second"""
    format = "{str1}.\n{str2}?".format(str1=str1, str2=str2)

    return format


str1 = "Hello there, my name is Elijah"
str2 = "How are you doing today"

print("THIS FUNCTION:", add_punctuation.__doc__)
print("PASSED STRINGS:")
print("1:", str1)
print("2:", str2)
print("FINAL RESULT:", add_punctuation(str1, str2))
print()


# This is to practice c-style formatting
def remove_punctuation(str1, str2):
    """Concatenates two strings, after removing the last letter of each strings"""

    format = "%s\n%s" % (str1[:-1], str2[:-1])

    return format

str1 += "."
str2 += "?"

print("THIS FUNCTION:", remove_punctuation.__doc__)
print("PASSED STRINGS:")
print("1:", str1)
print("2:", str2)
print("FINAL RESULT:", remove_punctuation(str1, str2))
