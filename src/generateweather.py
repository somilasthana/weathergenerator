from config import ConfigState
from weathertype import different_weather_types
from weatherdriver import WeatherDriver


class WeatherSimulator:

    def __init__(self, config):
        self.config = config
        self.driver = WeatherDriver(config)
        self.earth_weather = self.driver.weather

    def generate(self):

        citylist = list(self.earth_weather.keys())

        if self.config.generate_city_list is not None:
            citylist = self.config.generate_city_list

        for i in range(0, self.config.number_records_to_generate):
            for cityname in citylist:
                record = self.earth_weather[cityname].generate_record(self.config)
                frecord = "|".join(map(str, record))
                print(frecord)


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
                         generate_city_list=None,
                         number_records_to_generate=10,
                         specific_date=None,
                         weather_types=different_weather_types)
    print("=====================STEP 1=====================================")
    print("=====================Building Model=============================")
    simulator = WeatherSimulator(config)
    print("=====================STEP 2=========================================")
    print("=====================Generating Records=============================")
    simulator.generate()