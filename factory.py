"""
Zoo
"""


class Zoo:
    """
    Zoo
    """
    def __init__(self, file):
        self._animals = []
        self.create_animal(file)

    def animals(self):
        """
        animals
        """
        return self._animals

    def create_animal(self, file):
        """
        create_animal
        """
        with open(file, 'rt') as file1:
            for line in file1:
                animal = None
                kind, name, weight = line.split(',')

                if kind == 'Dog':
                    animal = Dog(name, weight)
                elif kind == 'Cat':
                    animal = Cat(name, weight)
                elif kind == 'Bird':
                    animal = Bird(name, weight)
                else:
                    continue

                self._animals.append(animal)


class Animal:
    """
    Animal
    """
    def __init__(self, name, weight):
        self._weight = float(weight)
        self._name = name
        self._voice = ''

    def say(self):
        """
        say
        """
        return self._voice

    @property
    def weight(self):
        """
        weight
        """
        return self._weight


class Bird(Animal):
    """
    Bird
    """
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self._voice = 'Tweet'


class Dog(Animal):
    """
    Dog
    """
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self._voice = 'Woof'


class Cat(Animal):
    """
    Cat
    """
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self._voice = 'Meow'
