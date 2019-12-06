"""Module for work with csv files"""
import csv


class Zoo:
    """Class to represent zoo"""
    def __init__(self, file):
        self.animals_allowed = ["Cat", "Dog", "Bird"]
        self.animals_in_zoo = []
        with open(file, "rt") as csv_animals:
            for type_, name, weight in csv.reader(csv_animals):
                if type_ in self.animals_allowed:
                    self.animals_in_zoo.append(self.add_animal(type_, name, weight))

    @staticmethod
    def add_animal(type_: str, name: str, weight: str):
        """
        :param type_: type of animal
        :param name: name of animal
        :param weight: weight of animal
        :return: Animal object with specified params
        :raise: ValueError if animal of given type not allowed in zoo
        """
        type_ = type_.lower()
        if type_ == "cat":
            return Cat(name, weight)
        if type_ == "dog":
            return Dog(name, weight)
        if type_ == "bird":
            return Bird(name, weight)
        raise ValueError

    def animals(self):
        """
        :return: list of animals in zoo
        """
        return self.animals_in_zoo


class Animal:
    """Class representing animal"""
    def __init__(self, name: str, weight: str):
        try:
            self.weight = float(weight)
        except ValueError:
            raise ValueError
        self.name = name
        self.voice = ""

    def get_weight(self):
        """
        :return: weight of animal
        """
        return self.weight

    def say(self):
        """
        :return: voice of animal
        """
        return self.voice


class Cat(Animal):
    """Class to represent animal Cat"""
    def __init__(self, name: str, weight: str):
        super().__init__(name, weight)
        self.voice = "Meow"


class Dog(Animal):
    """Class to represent animal Dog"""
    def __init__(self, name: str, weight: str):
        super().__init__(name, weight)
        self.voice = "Woof"


class Bird(Animal):
    """Class to represent animal Bird"""
    def __init__(self, name: str, weight: str):
        super().__init__(name, weight)
        self.voice = "Tweet"
