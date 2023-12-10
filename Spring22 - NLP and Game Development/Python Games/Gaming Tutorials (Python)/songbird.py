
class SongBird:
    "A base class to define songbird properties"
    count = 0

    def __init__(self, name, song):
        self.name = name
        self.song = song
        print("{} says {} ... Hello World!".format(name, song))
        SongBird.count += 1

    def sing(self):
        print(self.name, "sings:", self.song)

    def __del__(self):
        print("{} has died!".format(self.name))
        print("{} birds remaining!".format(SongBird.count))
        SongBird.count -= 1



sparrow = SongBird("sparrow", "wallalalala")
sparrow.sing()

nic = SongBird("nic", "gallalalla")
nic.sing()
print(nic.__dict__)

print("The 'nic' songbird object is singing in memory location:", id(nic))

print("The {} songbird object is singing in memory location: {}".format(sparrow.name, id(sparrow)))

del nic
del sparrow
