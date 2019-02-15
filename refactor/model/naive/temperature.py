from refactor.contract.propsinterface import WeatherProps


class NaiveTemperature(WeatherProps):
    """
    Trivial Temperature Models always gives the same value 23
    """
    def __init__(self, city_details):
        self.city_details = city_details
        self.temperature = 23

    def next_value(self):
        yield self.temperature
