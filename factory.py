"""
docstring
"""
import pandas as pd


class Zoo:
    """
    docstring
    """
    def __init__(self, animals_csv):
        """

        :param animals_csv:
        """
        self.animals_csv = animals_csv
        self._zoo_data = pd.read_csv(animals_csv)
        # self.type = list(self._zoo_data.type)
        # self.name = list(self._zoo_data.name)
        self.sounds = list(self._zoo_data.sound)
        self.weight = list(self._zoo_data.weight)

    def get_weight(self):
        """

        :return:
        """
        return sum(self.weight)

    def say(self):
        """

        :return:
        """
        return self.sounds
