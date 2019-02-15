from refactor.contract.propsinterface import WeatherProps
from refactor.constant import WeatherPropertiesRange
import numpy as np


class RandomHumidity(WeatherProps):
    def __init__(self, city_details):
        self.city_details = city_details

    def next_value(self):
        yield np.random.uniform(WeatherPropertiesRange.MIN_HUMIDITY.value,
                                WeatherPropertiesRange.MAX_HUMIDITY.value, 1)