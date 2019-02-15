from refactor.contract.propsinterface import WeatherProps
from refactor.constant import WeatherCondition
import numpy as np


class RandomCondition(WeatherProps):
    def __init__(self, city_details):
        """
        Simple Model it just selects one weather condition from given ['Sunny', 'Cloudy', 'Rainy', 'Snow', 'Storm', "ThunderStorm", "Foggy",
                                   "Sandstorm", "Smog", "Snowstorm", "Tornado", "Windy"]
        :param city_details:
        """
        self.city_details = city_details

    def next_value(self):
        yield np.random.choice(WeatherCondition.__dict__['_member_names_'])
