import abc


class SimulatorReporterInterface:
    """
    Interface the reporter needs to implement
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def save_state(self, obj):
        return None


