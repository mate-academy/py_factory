"""Module"""
from csv import reader


class Zoo:
    """
    Representing the zoo.
    """
    def __init__(self, filename):
        self.existing_animals = {"Dog": Dog, "Cat": Cat, "Bird": Bird}
        self.animals = []
        with open(filename, 'rt') as csvfile:
            csv = list(reader(csvfile, delimiter=','))
            for animal_type, name, weight in csv:
                if animal_type in self.existing_animals:
                    try:
                        animal = self.existing_animals[animal_type](name, float(weight))
                        self.animals.append(animal)
                    except ValueError:
                        print("ValueError")

    def existing_animals(self):
        """get all existing animals"""
        return self.existing_animals

    def animals(self):
        """get all zoo list"""
        return self.animals


class Animal:
    """
    Parent animal class
    """
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.voice = None

    def get_name(self):
        """return animal name"""
        return self.name

    def say(self):
        """return what animal say"""
        return self.voice

    def get_weight(self):
        """return animal weight"""
        return self.weight


class Dog(Animal):
    """ dog class"""
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = "Woof"


class Cat(Animal):
    """class cat"""
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = "Meow"


class Bird(Animal):
    """
    class bird
    """
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = "Tweet"
