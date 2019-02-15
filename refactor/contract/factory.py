import abc


class SimulatorFactoryInterface:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_simulator(self):
        pass


class SimulatorFactoryReporterInterface:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_reporter(self):
        pass


class WeatherModelFactory:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_model(self, city, algo_name):
        pass

"""
class TaskProcessInterface:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_tasks(self):
        pass
"""