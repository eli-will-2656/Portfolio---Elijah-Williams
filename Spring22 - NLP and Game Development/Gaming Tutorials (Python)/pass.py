# This program will print the string "\nPython In Easy Steps\n" in three different ways

title = "\nPython In Easy Steps\n"

print(title)


for char in title:
	print(char, end= " ")

# pass
for char in title:
	if char.lower()  == 's':
		print(chr(250),end= " ")
		pass

	print(char, end= " ")




# continue
for char in title:
	if char.lower() == 's':
		print(chr(259), end= " ")
		continue

	print(char, end = " ")