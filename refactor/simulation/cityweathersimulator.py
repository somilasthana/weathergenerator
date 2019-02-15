from refactor.library.weathergenerator import WeatherGeneratorProcess
from refactor.library.weatheralgofactory import WeatherModelFactoryImpl
from refactor.simulation.basicsimulator import BasicSimulator
from refactor.simerror.unknown import UnknownCityAttributesException
from refactor.simerror.unknown import UnknownConfigException
from refactor.simlog.printlog import printlog

class CityWeatherSimulator(BasicSimulator):

    def __init__(self, config, city_meta_attributes):
        """
        This class extends the BasicSimulator and populates the tasks which Simulator will run
        :param config: Config object which gives details on what type of model to use to generate weather data points
        The format used by ymal file :
          city_config:
            default:
              model_used: naive
          Vancouver:
              model_used: random
          Denver:
              model_used: latlong
          Config can be specific to each city for example "Vancouver" and "Denver" use different models ("random" and "latlong")
          rest of cities provided in city_meta_attributes uses default "naive" model.

          "naive model" refers to "NaiveWeatherGenerationAlgorithm"
          "random model" refers to "RandomWeatherGenerationAlgorithm"
          "latlong model" refers to "LatLongWeatherGenerationAlgorithm"

        :param city_meta_attributes: City Attributes - This is a necessary input
        """
        super().__init__()
        self.city_config = config["city_config"] if config is not None and "city_config" in config else None
        iterations = config["iterations"] if config is not None and "iterations" in config  else 1

        maximum_task_to_run = config["maximum_task_to_run"] if config is not None and "maximum_task_to_run" in config else 10
        self.city_meta_attributes = city_meta_attributes
        self.initialize(iterations, maximum_task_to_run)
        self.set_tasks()

    def set_tasks(self):

        if self.city_meta_attributes is None:
            raise UnknownCityAttributesException("CityWeatherSimulator expects city_meta_attributes : CityMetaAttributes")

        if self.city_config is None:
            raise UnknownConfigException("CityWeatherSimulator expects city_config parameter in ymal file")

        city_names = self.city_meta_attributes.city_names
        for city in city_names:
            if city in self.city_config:
                model_name = self.city_config[city]["model_used"]
            elif "default" in self.city_config:
                """apply the default model suggested in config"""
                model_name = self.city_config["default"]["model_used"]
            else:
                printlog("Simulation", "No default config for a model if city name does not exist in CityMetaAttributes")
                continue

            weather_algorithm = WeatherModelFactoryImpl().get_model(model_name, self.city_meta_attributes(city))
            task = WeatherGeneratorProcess(weather_algorithm)
            self.activate(task)

