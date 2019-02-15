import abc


class SimulatorReporterInterface:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def save_state(self, obj):
        return None


