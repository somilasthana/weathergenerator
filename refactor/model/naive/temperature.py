from refactor.contract.propsinterface import WeatherProps


class NaiveTemperature(WeatherProps):
    def __init__(self, city_details):
        self.city_details = city_details
        self.temperature = 23

    def next_value(self):
        yield self.temperature
