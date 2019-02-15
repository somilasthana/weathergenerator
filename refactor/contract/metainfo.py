import abc

class CityDetails:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def city_name(self):
        return None

    @abc.abstractmethod
    def city_lat(self):
        return float(0.0)

    @abc.abstractmethod
    def city_long(self):
        return float(0.0)

    @abc.abstractmethod
    def city_sealevel(self):
        return 0
