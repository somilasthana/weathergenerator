import abc
from refactor.utils.state import State
from refactor.time.systime import SimulationSystemTime


class WeatherGenerationAlgorithm:
    """
    Each Algorithm which is basically a task from CityWeatherSimulator  point of view implements
    following interfaces which CityWeatherSimulator will call.
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, city_details):
        if city_details is None:
            self.state = State(temperature=0,
                               pressure=0,
                               humidity=0,
                               weather_condition=None,
                               sea_level=10,
                               time=None
                               )
        else:
            self.state = State(temperature=0,
                               pressure=0,
                               humidity=0,
                               weather_condition=None,
                               cityname=city_details.cityname,
                               latitude=city_details.latitude,
                               longitude=city_details.longitude,
                               country=city_details.country,
                               zone=city_details.zone,
                               sea_level=10,
                               time=None
                            )
        self.state.time = SimulationSystemTime().get_time(self.state.zone) if "zone" in self.state else SimulationSystemTime().get_time()

    @abc.abstractmethod
    def init(self):
        pass

    @abc.abstractmethod
    def run(self):
        pass

    @abc.abstractmethod
    def cleanup(self):
        pass