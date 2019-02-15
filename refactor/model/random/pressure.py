from refactor.contract.propsinterface import WeatherProps
from refactor.constant import WeatherPropertiesRange
import numpy as np


class RandomPressure(WeatherProps):
    def __init__(self, city_details):
        self.city_details = city_details

    def next_value(self):
        yield np.random.uniform(WeatherPropertiesRange.MIN_PRESSURE.value,
                                WeatherPropertiesRange.MAX_PRESSURE.value, 1)

