from refactor.utils.state import State
import pandas as pd
from refactor.simerror.paramerror import InvalidParamException


class CityInformation(State):
    """
    For each city for which weather data needs to be generated, CityInformation keeps following details
    - name : Name of the City
    - latitude: Latitude information of the City
    - longitude: Longitude information of the City
    - country : Country
    - zone: Zone information such as "America/Vancouver" for city Vancouver
    - sealevel: Elevation Data ( In this implementation it set to 10 )
    """
    pass


class CityMetaAttributes:

    def __init__(self, city_meta_file):
        """
        Reads the city information from ../data/city_attributes_zone.csv. This file contains following columns
        Dummy,,City,Country,Latitude,Longitude,Zone
        Path for this csv file is read by Main application and stored in
        :param city_meta_file: path to csv file that contains the details. An example file is given
        ../data/city_attributes_zone.csv
        """
        self.city_meta_file = city_meta_file
        self.cities = {}
        self._process()

    def _process(self):
        """
        Reads the csv file in pandas frame
        Iterates thru each row and puts in dictionary
        :return: None
        """
        pd_city_attr = pd.read_csv(self.city_meta_file)
        pd_city_attr = pd_city_attr.set_index("City")
        city_list = list(pd_city_attr.index)
        for cityname in city_list:
            self.cities[cityname] = CityInformation(cityname=cityname,
                                                    latitude=pd_city_attr.loc[cityname]['Latitude'],
                                                    longitude=pd_city_attr.loc[cityname]['Longitude'],
                                                    country=pd_city_attr.loc[cityname]['Country'],
                                                    zone=pd_city_attr.loc[cityname]['Zone'],
                                                    sea_level=10)

    @property
    def city_names(self):
        """
        :return: The list of all city names
        """
        return self.cities.keys()

    def __call__(self, cityname):
        """
        :param cityname: city name
        :return: CityInformation object with city details or InvalidParamException() if city name is not found
        """
        if cityname in self.cities:
            return self.cities[cityname]
        else:
            raise InvalidParamException("city name {0} is not in the {1} provided "
                                        "at the start of simulation".format(cityname, self.city_meta_file))




