"""
There is a csv file with a list of animals from the zoo (see exercise py_zoo).
Your task is to create a zoo from this file. Please note that the file may
contain invalid data.
"""

import csv


class Zoo:
    """Class Zoo with animals"""
    def __init__(self, file_name):
        self.zoo_animals = []
        self.catalog = {'Dog': Dog, 'Cat': Cat, 'Bird': Bird}
        self.read_file(file_name)

    def read_file(self, file_name):
        """Create animals"""
        with open(file_name, 'rt') as rfile:
            reader = csv.DictReader(rfile)
            for row in reader:
                try:
                    animal = self.catalog[row['type']](row['name'], float(row['weight']))
                except KeyError:
                    print("Doesn't have in zoo catalog {}".format(row['type']))
                    continue
                self.zoo_animals.append(animal)

    def animals(self):
        """Get all animals in Zoo"""
        return self.zoo_animals


class Animal:
    """Class Animals mixim"""
    def __init__(self):
        super().__init__()
        self.name = ""
        self.weight = ""
        self.animal_say = ""

    def get_name(self):
        """Get animal name"""
        return self.get_name()

    def get_weight(self):
        """Get animal weight"""
        return self.weight

    def say(self):
        """Get animal say"""
        return self.animal_say


class Dog(Animal):
    """Class Dog with name, weight and say"""
    def __init__(self, name, weight):
        super().__init__()
        self.name = name
        self.weight = weight
        self.animal_say = "Woof"


class Cat(Animal):
    """Class Cat with name, weight and say"""
    def __init__(self, name, weight):
        super().__init__()
        self.name = name
        self.weight = weight
        self.animal_say = "Meow"


class Bird(Animal):
    """Class Bird with name, weight and say"""
    def __init__(self, name, weight):
        super().__init__()
        self.name = name
        self.weight = weight
        self.animal_say = "Tweet"
