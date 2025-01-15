class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

    def speak(self):
        return f"{self.name} makes a sound."

class Cow(Animal):
    def __init__(self, name, age, milk_production):
        super().__init__(name, age, "Cow")
        self.milk_production = milk_production

    def moo(self):
        return f"{self.name} says Moo!"

    def produce_milk(self):
        return f"{self.name} is producing {self.milk_production} liters of milk."

# Chicken class (child of Animal)
class Chicken(Animal):
    def __init__(self, name, age, egg_count):
        super().__init__(name, age, "Chicken")
        self.egg_count = egg_count

    def cluck(self):
        return f"{self.name} says Cluck!"

    def lay_eggs(self):
        return f"{self.name} has laid {self.egg_count} eggs."

class Sheep(Animal):
    def __init__(self, name, age, wool):
        super().__init__(name, age, "Sheep")
        self.wool = wool

    def baa(self):
        return f"{self.name} says Baa!"

    def shear_wool(self):
        return f"{self.name} has {self.wool} kg of wool."

cow = Cow("Bessie", 5, 20)
chicken = Chicken("Clara", 2, 12)
sheep = Sheep("Woolly", 3, 15)

print(cow.eat())  
print(cow.moo()) 
print(cow.produce_milk())  

print(chicken.sleep()) 
print(chicken.cluck())  
print(chicken.lay_eggs())  

print(sheep.speak())  
print(sheep.baa()) 
print(sheep.shear_wool()) 