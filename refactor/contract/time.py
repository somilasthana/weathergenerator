import abc


class SimulationTick:
    """
    Time Interface by users to get system time, hour, day, month and year.
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_time(self,zone):
        pass

    @abc.abstractmethod
    def get_hour(self, timezone="UTC"):
        pass

    @abc.abstractmethod
    def get_day(self, timezone="UTC"):
        pass

    @abc.abstractmethod
    def get_month(self, timezone="UTC"):
        pass

    @abc.abstractmethod
    def get_year(self, timezone="UTC"):
        pass
