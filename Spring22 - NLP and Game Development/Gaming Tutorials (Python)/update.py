"""This module is used to explore updating and reading from files"""

text  = "A programmer is a person who looks both ways before going down a one-way street"

with open("coding_quotes.txt", 'w') as file:
	file.write(text)

print("Is file closed?\t", file.closed)

with open("coding_quotes.txt", 'r+') as file:
	quote = file.read()
	print(quote)

	file.seek(2)
	print("\nCurrent location in file:", file.tell())
	file.write("firefighter")


	file.seek(len(quote))
	print(file.tell())
	file.write(" and saves cats from trees")
	print(quote)
	quote = file.read()
	print(quote)


print(quote, "")
	

