import abc


class SimulatorInterface:
    """
    This interface needs to be implemented by any custom Simulator by the client of that Simulator
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def initialize(self, num_iterations, max_task_capacity):
        pass

    @abc.abstractmethod
    def activate(self, sim_task):
        pass

    @abc.abstractmethod
    def simulate(self, handler):
        pass

    @abc.abstractmethod
    def stop(self):
        pass