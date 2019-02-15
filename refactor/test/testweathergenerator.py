from refactor.library.weathergenerator import WeatherGeneratorProcess
from refactor.core.naive_algorithm import NaiveWeatherGenerationAlgorithm
from refactor.core.random_algorithm import RandomWeatherGenerationAlgorithm


def testWeatherGenerator_with_Naive():
    task = WeatherGeneratorProcess(NaiveWeatherGenerationAlgorithm(None))
    task.run_method()
    s = task.get_state()
    assert s.temperature == 0
    assert s.pressure == 0
    assert s.humidity == 0
    assert s.weather_condition == "Sunny"


def testWeatherGenerator_with_Random():
    task = WeatherGeneratorProcess(RandomWeatherGenerationAlgorithm(None))
    task.run_method()
    s = task.get_state()

    assert s.temperature > 0.0
    assert s.temperature < 50.0
    assert s.pressure > 1065.0
    assert s.pressure < 1085.0
    assert s.humidity > 0.0
    assert s.humidity < 99.0
    assert s.weather_condition in ['Sunny', 'Cloudy', 'Rainy', 'Snow', 'Storm', "ThunderStorm", "Foggy",
                                   "Sandstorm", "Smog", "Snowstorm", "Tornado", "Windy"]


if __name__ == '__main__':
    testWeatherGenerator_with_Naive()
    testWeatherGenerator_with_Random()
