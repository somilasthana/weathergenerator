from refactor.contract.propsinterface import WeatherProps


class NaiveHumidity(WeatherProps):
    def __init__(self, city_details):
        self.city_details = city_details
        self.humidity = 63

    def next_value(self):
        yield self.humidity
