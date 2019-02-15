from refactor.contract.propsinterface import WeatherProps
from refactor.time.systime import SimulationSystemTime


class LatLongHumidity(WeatherProps):
    def __init__(self, city_details):
        """
        These coefficients were calculated off hand by applying Linear Regression on humidity data
        The training feature used were Latitude, Longitude and Time(Hour) and target variable was Humidity.

        After applying Linear Regression the equation to get new humidity value is

        humidity = 53.685 + 0.683 * lat + 0.063 * long - 0.468 * hour

        CityMetaAttributes has Latitude, Longitude information
        SimulationSystemTime can get hour information.

        Code for applying Linear Regression Training Model is not included in this code.
        :param city_details: Instance of CityMetaAttributes

        Training Data used ( showing few rows )
            Time	Latitude	Longitude	Humidity
        0	13	31.769039	35.216331	50.0
        1	14	31.769039	35.216331	47.0
        2	15	31.769039	35.216331	67.0
        3	16	31.769039	35.216331	88.0
        4	17	31.769039	35.216331	45.0
        """
        self.city_details = city_details
        self.lat_coefficent = 0.683
        self.long_coefficent = 0.063
        self.hour_time_coefficent = -0.468
        self.intercept = 53.685

    def next_value(self):
        hour = SimulationSystemTime().get_hour()
        yield self.city_details.latitude * self.lat_coefficent \
              + self.city_details.longitude * self.long_coefficent + self.hour_time_coefficent * hour + self.intercept
