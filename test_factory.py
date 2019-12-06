import factory


def test_zoo():
    z = factory.Zoo('zoo.csv')
    # + Platypus,Perry,1.2 -> Quack
    assert [animal.say() for animal in z.get_animals()] == ['Woof', 'Meow', 'Meow', 'Quack', 'Tweet']


def test_weight():
    z = factory.Zoo('zoo.csv')
    # + Platypus,Perry,1.2
    assert sum(animal.get_weight() for animal in z.get_animals()) == 49.6
