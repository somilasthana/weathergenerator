
from cityinfo import CityAttributes
from weathermodel import WeatherConditionModel
from weathermodel import WeatherMeasureDistributionModel
from weatherstate import EarthWeather
from cityweathermodel import CityWeatherModel
from config import ConfigState
from weathertype import different_weather_types


class WeatherDriver:
    def __init__(self, config):
        self.config = config
        self.earth_details = CityAttributes(self.config).details
        self.earth_weather_condition = WeatherConditionModel(self.config).weather_condition
        self.earth_weather_measure = WeatherMeasureDistributionModel(self.config).represent
        self._drive()

    def _drive(self):
        self.earth_weather = EarthWeather()
        for cityname in self.earth_details.keys():
            city_weather_model = CityWeatherModel(cityname,
                                                  self.earth_weather_measure[cityname],
                                                  self.earth_weather_condition[cityname],
                                                  self.earth_details[cityname]
                                                  )
            self.earth_weather[cityname] = city_weather_model


    @property
    def weather(self):
        return self.earth_weather


if __name__ == "__main__":
    config = ConfigState(city_attr_file_name="../data/city_attributes_zone.csv",
                         city_attr_file_path=None,
                         weather_desc_file_name="../data/weather_description.csv",
                         weather_desc_file_path=None,
                         temperature_file_name="../data/temperature.csv",
                         temperature_file_path=None,
                         pressure_file_name="../data/pressure.csv",
                         pressure_file_path=None,
                         humdity_file_name="../data/humidity.csv",
                         humdity_file_path=None,
                         weather_types=different_weather_types)
    
    print("<weatherdriver.py>:Initiating Weather Driver")
    driver = WeatherDriver(config)
    
    earth_weather = driver.weather
    config = ConfigState(specific_date="01-26")
    for i in range(0,24):
        sample = earth_weather["Chicago"].generate_measure("01-26")
        print(sample)

