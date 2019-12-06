"""
Module defines zoo and animals that live in it.
Classes
-------
Zoo
Animal
Dog
Cat
Bird
"""
from csv import reader


class Zoo:
    """
    Representing the zoo.
    Attributes
    ----------
    filename -- file for parcing animals
    Methods
    -------
    animals()
    """
    def __init__(self, filename):
        self._existing_animals = {"Dog": Dog,
                                  "Cat": Cat,
                                  "Bird": Bird}
        self._animals = []
        with open(filename, 'rt') as csvfile:
            csv = list(reader(csvfile, delimiter=','))
            for animal_type, name, weight in csv:
                if animal_type in self._existing_animals:
                    try:
                        animal = self._existing_animals[animal_type](name, float(weight))
                        self._animals.append(animal)
                    except ValueError:
                        print("ValueError")

    def existing_animals(self):
        """get all existing animals"""
        return self._existing_animals

    def animals(self):
        """get all zoo list"""
        return self._animals


class Animal:
    """
    Parent animal class
    Attributes
    ----------
    name -- animal name
    weight -- animal weight
    voice -- animal voice
    Methods
    -------
    get_name()
    say()
    get_weight()
    """
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight
        self._voice = None

    def get_name(self):
        """return animal name"""
        return self._name

    def say(self):
        """return what animal say"""
        return self._voice

    def get_weight(self):
        """return animal weight"""
        return self._weight


class Dog(Animal):
    """representing the dog class"""
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self._voice = "Woof"


class Cat(Animal):
    """representing the cat class"""
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self._voice = "Meow"


class Bird(Animal):
    """representing the bird class"""
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self._voice = "Tweet"
