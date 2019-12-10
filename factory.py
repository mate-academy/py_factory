"""
docstring
"""
from csv import reader


class Zoo:
    """
    zoo class
    """

    def __init__(self, zoo_file):
        """
        def animals list
        """
        self.animal_zo = {"Dog": Dog, "Cat": Cat,
                          "Bird": Bird, "Platypus": Platypus}
        self._animals = []
        with open(zoo_file, 'rt') as file:
            csv = list(reader(file, delimiter=','))
            for animal_type, name, weight in csv:
                if animal_type in self.animal_zo:
                    try:
                        anim = self.animal_zo[animal_type](name, float(weight))
                        self._animals.append(anim)
                    except TypeError:
                        print("ValueError")

    def get_animals(self):
        """

        :return:
        """
        return self._animals

    def get_animals_in_zoo(self):
        """

        :param animal:
        :return:
        """
        return self.animal_zo


class Animal:
    """
    animal class
    """

    def __init__(self, name, weight):
        """

        :param name:
        """
        self._name = name
        self._weight = weight
        self._voice = None

    def get_name(self):
        """

        :return:
        """
        return self._name

    def weight(self):
        """

        :return:
        """
        return self._weight

    def say(self):
        """

        :return:
        """
        return self._voice


class Dog(Animal):
    """
    dog class
    """

    def __init__(self, name, weight):
        """

        :param name:
        """
        super().__init__(name, weight)
        self._voice = 'Woof'


class Cat(Animal):
    """
    cat class
    """

    def __init__(self, name, weight):
        """

        :param name:
        """
        super().__init__(name, weight)
        self._voice = 'Meow'


class Bird(Animal):
    """
    bird class
    """

    def __init__(self, name, weight):
        """

        :param name:
        """
        super().__init__(name, weight)
        self._voice = 'Tweet'


class Platypus(Animal):
    """
    Platypus class
    """
    def __init__(self, name, weight):
        """

        :param name:
        """
        super().__init__(name, weight)
        self._voice = 'Crr'
