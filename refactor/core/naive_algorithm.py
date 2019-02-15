from refactor.contract.strategy import WeatherGenerationAlgorithm
from refactor.model.naive.temperature import NaiveTemperature
from refactor.model.naive.pressure import NaivePressure
from refactor.model.naive.humidity import NaiveHumidity
from refactor.model.naive.condition import NaiveCondition


class NaiveWeatherGenerationAlgorithm(WeatherGenerationAlgorithm):

    def __init__(self, city_details):
        """
        This class implements "WeatherGenerationAlgorithm" interface enforced by "SimulatorFactory"
        It loosely couples models for temperature, pressure, humidity and weather condition.
        :param city_details: Expects city details such as lat, long, elevation, time zone information.
        It passes the city details to models for models to use lat, long, elevation in generating weather properties.
        ( The interface  is such that depending on city details model will generate different values. For instance,
        lat and long closer to equator will always have high temperature)
        """
        super().__init__(city_details)
        self.count = 0
        self.city_details = city_details
        self.temperature_model = NaiveTemperature(city_details)
        self.pressure_model = NaivePressure(city_details)
        self.humidity_model = NaiveHumidity(city_details)
        self.condition_model = NaiveCondition(city_details)

    def init(self):
        """
        Naive Model doesnt needs any pre-processing to run.
        :return: None
        """
        pass

    def run(self):
        """
        The design takes an advantage of python "yield" keyword which automatically keeps the state while looping.
        Here is High Level Design

        For loop:
              First run ...
                         invokes          runs
              Simulator ---------> Task -------->  Weather Algorithm
                                                  computes temperature, pressure, humidity, weather cond <-  Model

              Next run  ...

                                                   Weather  Algorithm
                                                   yield preserves previous temperature, pressure, humidity, weather cond
                                                   Can use these values to influence the current computation of weather properties

        :return: State ( contains weather properties )
        """
        for temp, pressure, humidity, condition in zip(self.temperature_model.next_value(),
                           self.pressure_model.next_value(),
                           self.humidity_model.next_value(),
                           self.condition_model.next_value()
                           ):
            self.count += 1

            self.state.temperature = temp
            self.state.pressure = pressure
            self.state.humidity = humidity
            self.state.weather_condition = condition

            yield self.state

    def cleanup(self):
        """
        Naive Model doesnt has any resources to clean
        :return:
        """
        pass


