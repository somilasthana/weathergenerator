import pandas as pd
from refactor.simerror.paramerror import InvalidParamException


class State(pd.Series):
    """
    This class extends Pandas Series for conveniently store key-pair value
    s = State()
    s["param1"] = value1
    s["param2"] = value2
    """
    def __init__(self, *args, **kwargs):
        if len(args) == 0:
            super().__init__(list(kwargs.values()), index=kwargs)
        else:
            msg = '__init__() takes no positional argument'
            raise TypeError(msg)

    def set(self, **kwargs):
        """
        Updating Series
        """
        for name, value in kwargs.items():
            self[name] = value

    def repr(self, keys_used):
        """
        This function gives values of keys listed in keys_used
        :param keys_used: Names of keys for which value needs to extracted
        :return: array values of keys_used or UnknownParameterException if finds that key name doesnt exist
        """
        arr_key_values = []
        for key in keys_used:
            if key in self:
                arr_key_values.append(str(self[key]))
            else:
                raise InvalidParamException("key: {} from config doesnt exist".format(key))
        return arr_key_values


class System(State):
    pass
