
from config import ConfigState
from earth import EarthDetails
from utils import UtilTool


class CityDetails:
    def __init__(self, config, city_name, country_name, longitude, latitude, timezone=None):
        self.config = config
        self.city_name = city_name
        self.country_name = country_name
        self.glongitude = longitude
        self.glatitude = latitude
        self.gtimezone = timezone

    @property
    def name(self):
        return self.city_name

    @property
    def country(self):
        return self.country_name

    @property
    def longitude(self):
        return self.glongitude

    @property
    def latitude(self):
        return self.glatitude

    @property
    def timezone(self):
        return self.gtimezone


class CityAttributes:
    def __init__(self, config):
        self.config = config
        self._process()

    def _process(self):
        city_attr_config = ConfigState(filename=self.config.city_attr_file_name, path=self.config.city_attr_file_path)
        pd_city_attr = UtilTool.read_to_dataframe(city_attr_config)

        pd_city_attr = pd_city_attr.set_index("City")
        citylist = list(pd_city_attr.index)

        self.earth_details = EarthDetails()

        for cityname in citylist:
            print("<cityinfo.py>:Extracting city attributes for city = {}".format(cityname))
            latitude = pd_city_attr.loc[cityname]['Latitude']
            longitude = pd_city_attr.loc[cityname]['Longitude']
            countryname = pd_city_attr.loc[cityname]['Country']
            zone = pd_city_attr.loc[cityname]['Zone']
            city_details = CityDetails(self.config, cityname, countryname, longitude, latitude, zone)
            self.earth_details[cityname] = city_details

    @property
    def details(self):
        return self.earth_details