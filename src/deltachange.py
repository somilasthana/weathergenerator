from config import ConfigState
from utils import UtilTool
from weatherstate import DeltaDailyTemperature

class DeltaTemperatureChange:

    def __init__(self,config):
        self.config = config
        self._process()

    def extract_city_temperature_diff(self, cityname):

        pd_temperature_portland = self.pd_temperature[["datetime", cityname]]

        pd_temperature_portland_diff = pd_temperature_portland.set_index('datetime').diff()

        return pd_temperature_portland_diff

    def _process(self):
        temperature_config = ConfigState(filename=self.config.temperature_file_name,
                                         path=self.config.temperature_file_path)
        self.pd_temperature = UtilTool.read_to_dataframe(temperature_config)

        self.city_name_list = set(self.pd_temperature.columns)
        self.city_name_list.remove('datetime')

        diff_temperature_city = DeltaDailyTemperature()

        for city_name in self.city_name_list:
            diff_temperature_city[city_name] = self.extract_city_temperature_diff(city_name)


