from refactor.contract.propsinterface import WeatherProps
from refactor.constant import WeatherCondition


class NaiveCondition(WeatherProps):
    """
    Trivial Weather Condition Models always gives the same condition "Sunny"
    """
    def __init__(self, city_details):
        self.city_details = city_details
        self.weather_condition = WeatherCondition.Sunny.value

    def next_value(self):
        yield self.weather_condition
