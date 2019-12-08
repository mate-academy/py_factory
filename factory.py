"""There is a csv file with a list of animals from the zoo.
 Your task is to create a zoo from this file."""


class Zoo:
    """implementation zoo object"""
    def __init__(self, file_name):
        self.animals = []
        self.file_name = file_name
        self.read_animals()

    def read_animals(self):
        """read file and add animal in zoo"""
        with open(self.file_name, 'rt') as csv_file:
            csv_file.readline()
            for row in csv_file.readlines():
                type_animal = self.add_animal(row.split(","))
                if type_animal:
                    self.animals.append(type_animal)
                else:
                    continue

    @staticmethod
    def add_animal(row):
        """create animal object"""
        if row[0] == "Dog":
            return Dog(row[1], row[2])
        if row[0] == "Cat":
            return Cat(row[1], row[2])
        if row[0] == "Bird":
            return Bird(row[1], row[2])
        return None

    def get_animal(self):
        """return all animals in zoo"""
        return self.animals

    def __repr__(self):
        return f"{self.animals}"


class Animal:
    """animal object"""
    def __init__(self, name, weight):
        self.name = name
        self.weight = float(weight)
        self.word = ""

    def get_name(self):
        """return name animal"""
        return self.name

    def say(self):
        """return word """
        return self.word

    def get_weight(self):
        """return weight"""
        return self.weight


class Dog(Animal):
    """dog implementation"""
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.word = "Woof"


class Cat(Animal):
    """cat implementation"""
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.word = "Meow"


class Bird(Animal):
    """bird implementation"""
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.word = "Tweet"
