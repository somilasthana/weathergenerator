import abc


class SimulatorInterface:
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