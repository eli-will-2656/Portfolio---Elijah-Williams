# Write your code here :-)

def incrementor():
    i = 1
    while True:
        yield i
        i += 1

inc = incrementor()

for i in range(3):
    print(next(inc))

