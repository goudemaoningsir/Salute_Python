class Animal:
    def __init__(self, name):
        self.name = name

    def say(self):
        print("I'm {}.".format(self.name))


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def catch(self, thing):
        print("{} caught a {}!".format(self.name, thing))


tom = Cat("Tom", "black")
tom.say()
tom.catch("mouse")


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I'm an animal and my name is {}".format(self.name))


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print("I'm a {} dog and my name is {}.".format(self.breed, self.name))


animal = Animal("Kangaroo")
animal.speak()  # I'm an animal and my name is Kangaroo.

dog = Dog("Buddy", "Golden Retriever")
dog.speak()  # I'm a Golden Retriever dog and my name is Buddy.


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I'm an animal and my name is {}.".format(self.name))


class Mammal:
    def eat(self):
        print("I'm a mammal and I eat!")


class Dog(Animal, Mammal):
    def __init__(self, name, breed):
        self.breed = breed
        super().__init__(name)

    def speak(self):
        super().speak()
        print("I'm a {} dog and I bark!".format(self.breed))


dog = Dog("Buddy", "Golden Retriever")
dog.speak()  # I'm an animal and my name is Buddy. I'm a Golden Retriever dog and I bark!
dog.eat()  # I'm a mammal and I eat!
