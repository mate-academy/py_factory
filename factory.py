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


class Dog:
    """Class of dog"""
    def __init__(self, name, weight):
        self._name = name
        self._say = "Woof"
        self._weight = float(weight)

    def get_name(self):
        """Get name of a dog"""
        return self._name

    def say(self):
        """What does a dog say?"""
        return self._say

    def get_weight(self):
        """Get animal's weight"""
        return self._weight


class Cat:
    """Class of cat"""
    def __init__(self, name, weight):
        self._name = name
        self._say = "Meow"
        self._weight = float(weight)

    def get_name(self):
        """Get name of a cat"""
        return self._name

    def say(self):
        """What does a cat say?"""
        return self._say

    def get_weight(self):
        """Get animal's weight"""
        return self._weight


class Bird:
    """Class of bird"""
    def __init__(self, name, weight):
        self._name = name
        self._say = "Tweet"
        self._weight = float(weight)

    def get_name(self):
        """Get name of a bird"""
        return self._name

    def say(self):
        """What does a bird say?"""
        return self._say

    def get_weight(self):
        """Get animal's weight"""
        return self._weight
