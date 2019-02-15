from refactor.contract.propsinterface import WeatherProps
from refactor.constant import WeatherCondition
from refactor.time.systime import SimulationSystemTime


class LatLongCondition(WeatherProps):
    def __init__(self, city_details):
        """
        This is not a perfect model instead of using Linear Regression to find weather condition one should use
        the probabilities of likelyhood of ['Sunny', 'Cloudy', 'Rainy', 'Snow', 'Storm', "ThunderStorm", "Foggy",
                                   "Sandstorm", "Smog", "Snowstorm", "Tornado", "Windy"]
        One choice was use of Logistic Regression.
        One issue with Linear Regression is that it outputs a continuous value instead of discrete.
        :param city_details:
        """
        self.city_details = city_details
        self.lat_coefficent = 0.014
        self.long_coefficent = -0.004
        self.hour_time_coefficent = -0.468
        self.intercept = 0.226
        self.weather_state = WeatherCondition.__dict__["_member_names_"]

    def next_value(self):
        """
        Linear Regression Model used to find weather condition. Since weather condition is a discrete variable
        and linear models give continuous output we have to discretize it.
        :return: Weather Condition
        """
        hour = SimulationSystemTime().get_hour()
        val = self.city_details.latitude * self.lat_coefficent \
              + self.city_details.longitude * self.long_coefficent + self.hour_time_coefficent * hour + self.intercept
        val = int(val)

        if val < 0:
            val -= val

        val = val % 10

        yield self.weather_state[val]
