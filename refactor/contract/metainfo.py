import abc


class CityDetails:
    """
    This interface mandates the structure of City Details information that Simulator may need
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def city_name(self):
        pass

    @abc.abstractmethod
    def city_lat(self):
        pass

    @abc.abstractmethod
    def city_long(self):
        pass

    @abc.abstractmethod
    def city_sealevel(self):
        pass
