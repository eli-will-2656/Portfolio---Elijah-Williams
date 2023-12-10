zoo = ("Kangaroo", "Leopard", "Moose", "Giraffe")

print("Tuple:\t", zoo, "\tLength", len(zoo))
print(type(zoo))

colors = {"blue", "green", "red", "orange"}
print("Set:\t", colors, "\tLength", len(colors))

x ="purple"
y = "green"
z ="red"

colors.update({x,y,z})
print(colors)

print(colors.pop())
print(colors.pop())