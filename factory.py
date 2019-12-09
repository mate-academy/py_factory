"""ZOO MODULE
"""
import csv


class Zoo:
    """Zoo class"""
    def __init__(self, filename):
        self._factory = {
            Dog.__name__: Dog,
            Cat.__name__: Cat,
            Bird.__name__: Bird
        }
        self._animals = []
        with open(filename, 'rt') as reader:
            data = csv.DictReader(reader)
            for row in data:
                if row['type'] in self._factory.keys():
                    print(row['type'], row['name'], row['weight'])
                    self._animals.append(
                        self._factory[row['type']](row['name'], row['weight'])
                    )

    def animals(self):
        """Get all animals"""
        return self._animals

    def get_names_of_classes(self):
        """Get Dict with classes' names"""
        return self._factory


class Animal:
    """Common animal class"""
    def __init__(self, name, weight):
        self._name = name
        self._weight = float(weight)
        self._say = ''

    def get_name(self):
        """Get animal's name"""
        return self._name

    def say(self):
        """Animal's voice"""
        return self._say

    def get_weight(self):
        """Get animal's weight"""
        return self._weight


class Dog(Animal):
    """Class of dog"""
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self._say = "Woof"


class Cat(Animal):
    """Class of cat"""
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self._say = "Meow"


class Bird(Animal):
    """Class of bird"""
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self._say = "Tweet"
