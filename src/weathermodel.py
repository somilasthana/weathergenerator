
from config import ConfigState
from utils import UtilTool
from measuremodels import TemperatureModel
from measuremodels import PressureModel
from measuremodels import HumidityModel
from weatherstate import EarthWeatherMeasureModel
from weatherstate import EarthWeatherCondtionModel
from cityweathermodel import CityWeatherMeasureModel
from cityweathermodel import CityWeatherConditionModel


class WeatherMeasureDistributionModel:

    def __init__(self, config):
        self.config = config
        self._process()

    def _process(self):
        print("Extracting measure:temperature details for all cities")
        temperature_config = ConfigState(filename=self.config.temperature_file_name, path=self.config.temperature_file_path)
        pd_temperature = UtilTool.read_to_dataframe(temperature_config)
        
        
        print("Extracting measure:pressure details for all cities")
        pressure_config = ConfigState(filename=self.config.pressure_file_name, path=self.config.pressure_file_path)
        pd_pressure = UtilTool.read_to_dataframe(pressure_config)
        
        print("Extracting measure:humidity details for all cities")
        humidity_config = ConfigState(filename=self.config.humdity_file_name, path=self.config.humdity_file_path)
        pd_humdity = UtilTool.read_to_dataframe(humidity_config)

        t_citylist = set(pd_temperature.columns)
        p_citylist = set(pd_pressure.columns)
        h_citylist = set(pd_humdity.columns)

        # Find common cities in each dataset
        self.city_name_list = list(t_citylist.intersection(p_citylist).intersection(h_citylist))
        self.city_name_list.remove('datetime')

        self.temperature_model = TemperatureModel(pd_temperature, self.city_name_list)
        self.pressure_model = PressureModel(pd_pressure, self.city_name_list)
        self.humidity_model = HumidityModel(pd_humdity, self.city_name_list)

        self.earth_weather_measure = EarthWeatherMeasureModel()

        for city_name in self.city_name_list:
            city_weather = CityWeatherMeasureModel(
                city_name,
                self.temperature_model.represent[city_name],
                self.pressure_model.represent[city_name],
                self.humidity_model.represent[city_name]
            )
            self.earth_weather_measure[city_name] = city_weather

    @property
    def represent(self):
        return self.earth_weather_measure


class WeatherConditionModel:
    def __init__(self, config):
        self.config = config
        self._process()

    def _process(self):
        weather_desc_config = ConfigState(filename=self.config.weather_desc_file_name,
                                          path=self.config.weather_desc_file_path)
        pd_weather_desc = UtilTool.read_to_dataframe(weather_desc_config)
        pd_weather_desc = pd_weather_desc.dropna()

        citylist = list(pd_weather_desc.columns)
        citylist.remove('datetime')
        self.earth_weather_condition_model = EarthWeatherCondtionModel()
        for cityname in citylist:
            print("===================================================")
            print("<weathermodel.py> Creating Condtional Probability Distribution For city {}".format(cityname))
            pd_weather_desc[cityname] = pd_weather_desc[cityname].apply(lambda x: self.config.weather_types[x])
            city_conditions_transitions = CityWeatherConditionModel(self.config, cityname, pd_weather_desc).transitions
            self.earth_weather_condition_model[cityname] = city_conditions_transitions

    @property
    def weather_condition(self):
        return self.earth_weather_condition_model