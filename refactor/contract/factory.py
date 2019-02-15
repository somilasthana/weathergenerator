import abc


class SimulatorFactoryInterface:
    """
    This interface needs to be implemented by Simulator Factory to create Simulator Object
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_simulator(self):
        pass


class SimulatorFactoryReporterInterface:
    """
    This interface needs to be implemented by Reporter Factory to create Reporter Object
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_reporter(self):
        pass


class WeatherModelFactory:
    """
    This interface needs to be implemented by Weather Model Factory to Create Weather Models
    """
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