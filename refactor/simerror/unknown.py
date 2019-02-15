

class UnknownAlgoException(Exception):
    """In case simulation tries to use an unknown model"""


class UnknownPropertyException(Exception):
    """The config property name does not exist"""


class UnknownEnvironmentalException(Exception):
    """Unknown environmental variable in os"""


class UnknownSimulatorException(Exception):
    """Unknown simulator used"""


class UnknownReporterException(Exception):
    """Unknown reporter used"""


class UnknownCityAttributesException(Exception):
    """Unknown city attributes are not known"""


class UnknownConfigException(Exception):
    """Unknown config"""


class UnknownFileException(Exception):
    """Unknown File used in Simulation"""
