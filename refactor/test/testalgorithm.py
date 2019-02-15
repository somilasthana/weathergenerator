from refactor.core.naive_algorithm import NaiveWeatherGenerationAlgorithm
from refactor.core.random_algorithm import RandomWeatherGenerationAlgorithm
from refactor.core.latlong_algorithm import LatLongWeatherGenerationAlgorithm
from refactor.utils.citydetails import CityInformation


def test_NaiveAlgo():

    city = CityInformation(cityname="Vancouver",
                           latitude=49.24,
                           longitude=-123.12,
                           country="Canada",
                           zone="America/Vancouver",
                           sealevel=10)
    n = NaiveWeatherGenerationAlgorithm(city)

    s = next(n.run())
    assert s.temperature == 0
    assert s.pressure == 0
    assert s.humidity == 0
    assert s.weather_condition == "Sunny"


def test_RandomAlgo():

    city = CityInformation(cityname="Vancouver",
                           latitude=49.24,
                           longitude=-123.12,
                           country="Canada",
                           zone="America/Vancouver",
                           sealevel=10)

    n = RandomWeatherGenerationAlgorithm(city)

    s = next(n.run())

    assert s.temperature > 0.0
    assert s.temperature < 50.0
    assert s.pressure > 1065.0
    assert s.pressure < 1085.0
    assert s.humidity > 0.0
    assert s.humidity < 99.0
    assert s.weather_condition in ['Sunny', 'Cloudy', 'Rainy', 'Snow', 'Storm', "ThunderStorm", "Foggy",
                                   "Sandstorm", "Smog", "Snowstorm", "Tornado", "Windy"]

    # Second Attempt

    s = next(n.run())

    assert s.temperature > 0.0
    assert s.temperature < 50.0
    assert s.pressure > 1065.0
    assert s.pressure < 1085.0
    assert s.humidity > 0.0
    assert s.humidity < 99.0
    assert s.weather_condition in ['Sunny', 'Cloudy', 'Rainy', 'Snow', 'Storm', "ThunderStorm", "Foggy",
                                   "Sandstorm", "Smog", "Snowstorm", "Tornado", "Windy"]
    assert s.cityname == "Vancouver"
    assert float(s.latitude) == 49.24
    assert float(s.longitude) == -123.12
    assert s.country == "Canada"
    assert int(s.sea_level) == 10

def test_latAlgo():

    city = CityInformation(cityname="Vancouver",
                           latitude=49.24,
                           longitude=-123.12,
                           country="Canada",
                           zone="America/Vancouver",
                           sealevel=10)

    n = LatLongWeatherGenerationAlgorithm(city)
    s1 = next(n.run())

    print(s1)

    s2 = next(n.run())

    print(s2)


if __name__ == '__main__':
    test_NaiveAlgo()
    test_RandomAlgo()
    test_latAlgo()