class Parrot:

    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

Blu = Parrot("Blu", 10)
Wlu = Parrot("Wlu", 9)

print("Blu is a {}".format(Blu.species))
print("Wlu is also a {}".format(Wlu.species))

print("{} is {} years old".format(Blu.name, Blu.age))
print("{} is {} years old".format(Wlu.name, Wlu.age))
