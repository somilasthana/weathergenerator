import abc


class WeatherProps:
    """
    Interface that Condition, Temperature, Pressure and Humidity Algorithm need to implement.
    Each run of simulation eventually calls next_value() get the next value.
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def next_value(self):
        pass
