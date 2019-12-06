"""
Module to create a zoo out of csv.file with animals
Classes
-------
Animal
Zoo
"""
import csv


class Animal:
    """
    A base class Animal for creating animals
    Attributes
    ----------
    species : str  --  species of the animal
    name : str  --  name of the animal
    weight : float  --  weight of the animal

    Methods
    -------
    say() -- return the sound of the animal
    get_name() -- return name of the animal
    """

    def __init__(self, species, name, weight):
        self.species = species
        self.name = name
        self.weight = weight

    def say(self):
        """Return the sound of the animal"""
        sounds = {'Dog': 'Woof', 'Cat': 'Meow', 'Platypus': 'Prrr', 'Bird': 'Tweet'}
        try:
            return sounds[self.species]
        except KeyError:
            return f"Sound of a {self.species} not found"

    def get_name(self):
        """Return name of the animal (for pylint test)"""
        return self.name


class Zoo:
    """
    Zoo class - used to create a zoo from csv.file
    Attributes
    ----------
    file_with_animals : str -- name of the csv.file with animals
    animals_in_zoo : list -- list of animals in the zoo

    Methods
    -------
    read_csv() -- read data from csv file
    animals() -- return list of animals
    """

    def __init__(self, file_with_animals):
        self.file_with_animals = file_with_animals
        self.animals_in_zoo = []
        self.read_csv()

    def read_csv(self):
        """Read data from the csv file with animals"""
        weight_idx = 2
        with open(self.file_with_animals, 'r') as file:
            csv_reader = csv.reader(file)
            _ = next(csv_reader)
            for animal in csv_reader:
                try:
                    animal[weight_idx] = float(animal[weight_idx])
                except ValueError:
                    raise Exception("ValueError! float value expected")
                self.animals_in_zoo.append(Animal(*animal))

    def animals(self):
        """Return list of animals"""
        return self.animals_in_zoo
