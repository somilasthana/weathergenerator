from enum import Enum


class AlgoType(Enum):
    NAIVE_ALGORITHM = "naive"
    RANDOM_ALGORITHM = "random"
    LATLONG_ALGORITHM = "latlong"


class SimulationType(Enum):
    SIMPLE_SIMULATOR = "SimpleSimulator"
    CITY_WEATHER_SIMULATOR = "CityWeatherSimulator"


class ConfigInfo(Enum):
    CONFIG_PATH_KEY = "CONFIG_PATH_KEY"
    SIMULATION = "simulation"


class ReporterType(Enum):
    FILE_BASED = "filebased"
    RABBITMQ = "rabbitmq"
    KAFKA = "kafka"
    STRING_BASED = "stringbased"


class WeatherPropertiesRange(Enum):
    MIN_TEMPERATURE = 0.0
    MAX_TEMPERATURE = 50.0
    MAX_PRESSURE = 1085.0
    MIN_PRESSURE = 1065.0
    MAX_HUMIDITY = 99.0
    MIN_HUMIDITY = 0.0


class WeatherCondition(Enum):
    Sunny = "Sunny"
    Cloudy = "Cloudy"
    Rainy = "Rainy"
    Snow = "Snow"
    ThunderStorm = "ThunderStorm"
    Foggy = 'Foggy',
    Sandstorm = 'Sandstorm',
    Smog = 'Smog',
    Snowstorm = 'Snowstorm',
    Tornado = 'Tornado',
    Windy = 'Windy'


WeatherConditionCnt = {'Sunny': 0,
                       'Cloudy': 1,
                       'Rainy': 2,
                       'Snow': 3,
                       'Thunderstorm': 4,
                       'Foggy': 5,
                       'Sandstorm': 6,
                       'Smog': 7,
                       'Snowstorm': 8,
                       'Tornado': 9,
                       'Windy': 10}


class FormatterType(Enum):
    PIPE_TYPE= "pipe"
    CBA_TYPE = "cba"


CBA_TEMP_FORMAT = "+"
