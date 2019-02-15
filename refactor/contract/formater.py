import abc


class FormatterInterface:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __call__(self, state):
        pass