import factory


def test_zoo():
    z = factory.Zoo('zoo.csv')
    print(z)
    assert [animal.say() for animal in z.get_animal()] == ['Woof', 'Meow', 'Meow', 'Tweet']


def test_weight():
    z = factory.Zoo('zoo.csv')
    assert sum(animal.weight for animal in z.get_animal()) == 48.4