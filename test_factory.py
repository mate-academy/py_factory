import factory


def test_zoo():
    z = factory.Zoo('zoo.csv')
    assert [animal.say() for animal in z.animals()] == ['Woof', 'Meow', 'Meow', 'Prrr', 'Tweet']


def test_weight():
    z = factory.Zoo('zoo.csv')
    assert sum(animal.weight for animal in z.animals()) == 49.6