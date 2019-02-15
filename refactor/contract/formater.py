import abc


class FormatterInterface:
    """
    Interface ot implement different formatter types depending on requirements
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __call__(self, state):
        pass