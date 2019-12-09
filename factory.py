"""This program  processes csv file with list of animals to inhabit the zoo"""
import csv


class Zoo:
    """This is class for operating with animals"""
    def __init__(self, file_name):
        """Initiate zoo inhabitants data"""
        self.fauna = ["Cat", "Dog", "Bird"]
        self.animals = []
        self.process_csv(file_name)

    def process_csv(self, f_name):
        """Read csv file"""
        with open(f_name, "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            self.generate_animals(csv_reader)

    def generate_animals(self, csv_reader):
        """Add animals from csv file to the zoo animals list"""
        for line in csv_reader:
            if line[0] in self.fauna:
                if line[0] == "Dog":
                    self.animals.append(Dog(line[1], line[2]))
                elif line[0] == "Cat":
                    self.animals.append(Cat(line[1], line[2]))
                elif line[0] == "Bird":
                    self.animals.append(Bird(line[1], line[2]))


class Animal:
    """This is parent class for all zoo animals"""
    def __init__(self, name, weight, say):
        """Initiate basic class variables"""
        self.name = name
        self.weight = float(weight)
        self.say_s = say

    def get_name(self):
        """Return name from class object"""
        return self.name

    def get_weight(self):
        """Return weight from class object"""
        return self.weight

    def say(self):
        """Refer to the sound of animal"""
        return self.say_s


class Dog(Animal):
    """This is child class for type of animals"""
    def __init__(self, name, weight, say="Woof"):
        """Re-assign sound of child class"""
        super().__init__(name, weight, say)


class Cat(Animal):
    """This is child class for type of animals"""
    def __init__(self, name, weight, say="Meow"):
        """Re-assign sound of child class"""
        super().__init__(name, weight, say)


class Bird(Animal):
    """This is child class for type of animals"""
    def __init__(self, name, weight, say="Tweet"):
        """Re-assign sound of child class"""
        super().__init__(name, weight, say)
