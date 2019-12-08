"""
docstring
"""
import factory


def test_zoo():
    """

    :return:
    """
    z = factory.Zoo('zoo.csv')
    assert z.say() == ['Woof', 'Meow', 'Meow', 'Crr', 'Tweet']


def test_weight():
    """

    :return:
    """
    z = factory.Zoo('zoo.csv')
    assert z.get_weight() == 49.6
