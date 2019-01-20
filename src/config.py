import pandas as pd
import numpy as np


class SimulationSequence(pd.Series):
    def __init__(self, *args, **kwargs):
        if args or kwargs:
            super().__init__(*args, **kwargs)
        else:
            super().__init__([], dtype=np.float64)

    def set(self, **kwargs):
        """
        Updating Series
        """
        for name, value in kwargs.items():
            self[name] = value


class SimulationFrame(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        if args or kwargs:
            super().__init__(*args, **kwargs)
        else:
            super().__init__([], dtype=np.float64)


class ConfigState(SimulationSequence):

    def __init__(self, *args, **kwargs):
        if len(args) == 0:
            super().__init__(list(kwargs.values()), index=kwargs)
        else:
            msg = '__init__() takes no positional argument'
            raise TypeError(msg)