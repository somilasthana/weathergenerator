from refactor.contract.factory import WeatherModelFactory
from refactor.core.naive_algorithm import NaiveWeatherGenerationAlgorithm
from refactor.core.random_algorithm import RandomWeatherGenerationAlgorithm
from refactor.core.latlong_algorithm import LatLongWeatherGenerationAlgorithm


from refactor.simerror.unknown import UnknownAlgoException

from refactor.constant import AlgoType


class WeatherModelFactoryImpl(WeatherModelFactory):

    def get_model(self, algo_name, city=None):
        """
        This factory class creates specific models based on  algo_name.
        It can be extended by adding new AlgoTypes but should implement "WeatherGenerationAlgorithm"
        :param algo_name: can be "naive", "random". latlong"
        :param city: instance of CityMetaAttributes which has City details like lat,long, sea_level however,
        underneath algo can run ignoring city details.
        :return: Implementation Algorithm
        """
        if algo_name == AlgoType.NAIVE_ALGORITHM.value:
            return NaiveWeatherGenerationAlgorithm(city)
        elif algo_name == AlgoType.RANDOM_ALGORITHM.value:
            return RandomWeatherGenerationAlgorithm(city)
        elif algo_name == AlgoType.LATLONG_ALGORITHM.value:
            return LatLongWeatherGenerationAlgorithm(city)
        else:
            raise UnknownAlgoException("{} algo implementation doesnt exist".format(algo_name))
