from config import ConfigState
import pandas as pd
import numpy as np


class WeatherState(ConfigState):

    """
    An interface to keeping weather states.
    """
    pass


class DailyWeatherMeasureModel(WeatherState):

    """
    This keeps track of daily measures : temperature, pressure, humidity for a city
    """
    pass


class EarthDailyWeatherMeasureModel(WeatherState):

    """
    This keeps track of daily measures: temperature, pressure, humidity for all cities
    """
    pass


class EarthWeatherMeasureModel(WeatherState):

    """
    This keeps track of year measure: temperature, pressure, humidity for all cities
    """
    pass


class EarthWeatherCondtionModel(WeatherState):

    """
    This keeps track of weather types conditions for all cities
    """
    pass


class EarthWeather(WeatherState):

    """
    This keeps track of weather for all cities
    """
    pass


class WeatherTransitions(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        if args or kwargs:
            super().__init__(*args, **kwargs)
        else:
            super().__init__([], dtype=np.float64)

