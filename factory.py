"""
module zoo with animals
"""
from csv import reader


class Animal:
    """
    Class using for creation an instance of Animal
    """

    def __init__(self, name, weight):
        self._name = name
        self._weight = weight
        self._voice = 'Hi, I\'m an animal'

    def get_name(self):
        """
        Return the name of animal.
        :return: str
        """
        return self._name

    def get_weight(self):
        """
        Return the weight of animal.
        :return: str
        """
        return self._weight

    def say(self):
        """
        Return the voice of animal.
        :return: str
        """
        return self._voice


class Dog(Animal):
    """
    Class using for creation an instance of Dog.
    Inherits from Animal class.
    """

    def __init__(self, name, weight):
        super().__init__(name, weight)
        self._voice = "Woof"


class Cat(Animal):
    """
    Class using for creation an instance of Cat.
    Inherits from Animal class.
    """

    def __init__(self, name, weight):
        super().__init__(name, weight)
        self._voice = "Meow"


class Bird(Animal):
    """
    Class using for creation an instance of Bird.
    Inherits from Animal class.
    """

    def __init__(self, name, weight):
        super().__init__(name, weight)
        self._voice = "Tweet"


class Platypus(Animal):
    """
    Class using for creation an instance of Platypus.
    Inherits from Animal class.
    """

    def __init__(self, name, weight):
        super().__init__(name, weight)
        self._voice = "Quack"


class Zoo:
    """
    Class using for creation an instance of Zoo.
    Using for keeping information about Animal instances.
    """

    def __init__(self, filename):
        self._animals = []
        try:
            with open(filename, 'rt') as file:
                animals_csv = list(reader(file, delimiter=','))
                for animal in animals_csv:
                    if animal[0] == 'Dog':
                        new_animal = Dog(
                            animal[1],
                            float(animal[2])
                        )
                        self.add(new_animal)
                    if animal[0] == 'Cat':
                        new_animal = Cat(
                            animal[1],
                            float(animal[2])
                        )
                        self.add(new_animal)
                    elif animal[0] == 'Bird':
                        new_animal = Bird(
                            animal[1],
                            float(animal[2])
                        )
                        self.add(new_animal)
                    elif animal[0] == 'Platypus':
                        new_animal = Platypus(
                            animal[1],
                            float(animal[2])
                        )
                        self.add(new_animal)
        except ValueError:
            print("Oops!  That was no valid data.  Try again...")

    def get_animals(self):
        """Return the list of animals of zoo.
        :return: list
        """
        return self._animals

    def add(self, animal):
        """
        Add animal to zoo.
        :param animal:
        :return: None
        """
        self._animals.append(animal)
