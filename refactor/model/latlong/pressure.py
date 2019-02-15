from refactor.contract.propsinterface import WeatherProps
from refactor.time.systime import SimulationSystemTime


class LatLongPressure(WeatherProps):
    def __init__(self, city_details):
        """
        These coefficients were calculated off hand by applying Linear Regression on pressure data
        The training feature used were Latitude, Longitude and Time(Hour) and target variable was Pressure.

        After applying Linear Regression the equation to get new pressure value is

        pressure = 1009.069 + 0.091 * lat - 0.054 * long + 0.025 * hour

        CityMetaAttributes has Latitude, Longitude information
        SimulationSystemTime can get hour information.

        Code for applying Linear Regression Training Model is not included in this code.
        :param city_details: Instance of CityMetaAttributes
        """
        self.city_details = city_details
        self.lat_coefficent = 0.091
        self.long_coefficent = -0.054
        self.hour_time_coefficent = 0.025
        self.intercept = 1009.069

    def next_value(self):
        hour = SimulationSystemTime().get_hour()
        yield self.city_details.latitude * self.lat_coefficent \
              + self.city_details.longitude * self.long_coefficent + self.hour_time_coefficent * hour + self.intercept
