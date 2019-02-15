from refactor.contract.propsinterface import WeatherProps


class NaivePressure(WeatherProps):
    def __init__(self, city_details):
        self.city_details = city_details
        self.pressure = 1018

    def next_value(self):
        yield self.pressure
