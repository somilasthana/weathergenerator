import abc


class Process:
    """
    Simulator Object runs task each task should implement Process Interface
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def run_method(self):
        pass

    @abc.abstractmethod
    def get_state(self):
        pass

    @abc.abstractmethod
    def cleanup(self):
        pass

    @abc.abstractmethod
    def __repr__(self):
        pass
