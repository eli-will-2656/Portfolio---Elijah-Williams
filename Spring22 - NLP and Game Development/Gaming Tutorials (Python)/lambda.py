
def squared(x): return x**2
def cubed(x): return x**3
def fourth_power(x): return x**4

callbacks = [squared, cubed, fourth_power]

for i, function in enumerate(callbacks): print("Function", i + 1,":", function(6))

# Here we are going to try and create anonymous functions using the lambda keyword

callbacks = [lambda x:x**1.5, lambda x: x**3, lambda x: x**4]

for i, function in enumerate(callbacks): print("Function", i + 1, ":", function(6))
