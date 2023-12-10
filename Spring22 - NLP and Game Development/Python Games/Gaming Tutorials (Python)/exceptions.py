player_name = "Isaiah Williams"

try:
	print(player_yame)

except NameError:
	print("hello world, a name error has occured")
	

# We can actually raise our own errors, so that we know that our code is working properly
player_age = 104
player_height = 105

try:
	if player_age > 1000:
		raise ValueError("Invalid Player Age")
	if player_height > 1000:
		raise NameError("Invalid Player Height")

except (NameError, ValueError) as msg:
	print("The following error has occured:", msg)

finally:
	print("All exceptions have been handled correctly")

