""" This module explores converting strings from on encoding to another """

# In python 3+, characters are stored as Unicode code points, instead of having ASCII encoding

s = "ã student"

print("\nRegular string:", s)
print("Type:", type(s),"\tLength:", len(s))

s = s.encode("utf-8")
print("\nEncoded String:", s)
print("Type:", type(s),"\tLength:", len(s))

s = s.decode('utf-8')
print("\nDecoded String:", s)
print("Type:", type(s),"\tLength:", len(s))

import unicodedata
for i in range(len(s)):
    print(s[i], unicodedata.name(s[i]), sep=':')

s = b'Gr\xc3\xb6n'
print("New string:", s.decode('utf-8'))

s = 'Gr\N{LATIN SMALL LETTER O WITH DIAERESIS}n'
print("New string:", s, type(s))
print()

x = "Encoded message".encode()
print("Encoded message:", x)
print(x, type(x), len(x))
