from refactor.contract.propsinterface import WeatherProps
from refactor.constant import WeatherPropertiesRange
import numpy as np


class RandomTemperature(WeatherProps):
    def __init__(self, city_details):
        self.city_details = city_details

    def next_value(self):
        yield np.random.uniform(WeatherPropertiesRange.MIN_TEMPERATURE.value,
                                WeatherPropertiesRange.MAX_TEMPERATURE.value, 1)
