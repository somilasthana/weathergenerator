from refactor.contract.propsinterface import WeatherProps


class NaivePressure(WeatherProps):
    """
    Trivial  Pressure Models always gives the same value 1018
    """
    def __init__(self, city_details):
        self.city_details = city_details
        self.pressure = 1018

    def next_value(self):
        yield self.pressure
