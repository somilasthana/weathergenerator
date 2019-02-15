import abc


class WeatherProps:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def next_value(self):
        pass
