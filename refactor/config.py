import yaml
from refactor.constant import ConfigInfo
from refactor.simerror.unknown import UnknownPropertyException,UnknownEnvironmentalException
from refactor.simlog.printlog import printlog
import os


class Config:
    """
    Generic Config Class
    """
    def __init__(self, config_file_path=None):
        """
        Config class can be invoked by a client either as
        1. conf = Config() (This will try to find path by reading $CONFIG_PATH_KEY environmental variable in bash)
        or
        2. conf = Config("/path/for/config") by explicitly given the path.
        :param config_file: Optional Config Path
        """
        self.config_file_path = config_file_path

        if self.config_file_path is None:
            try:
                self.config_file_path = os.environ[ConfigInfo.CONFIG_PATH_KEY]
            except Exception:
                raise UnknownEnvironmentalException("{} Environment var does exist".format(ConfigInfo.CONFIG_PATH_KEY))

        printlog("Config", "Config file name used {}".format(self.config_file_path))

        with open(self.config_file_path, "r") as ymlfile:
            self.cfg = yaml.load(ymlfile)

        printlog("Config", "yaml properties available{}".format(",".join(self.cfg.keys())))

    def __call__(self, property_name):
        """
        The reason for implementing __call__ instead of get_method is coding convenience ( One view is that
        this implement higher order function for Config).
        The simple usage to exact configuration for task which exist in yaml file is
            ## In this usage the client of Config class doesnt care about the config path it is read as environment
            ## variable
            conf = Config()
            task_properties = conf("task")

        :param property_name: Property Name to read details it will give results in form of a dictionary.
        :return: dictionary object for a known property else UnknownPropertyException exception
        """

        if property_name in self.cfg:
            return self.cfg[property_name]
        else:
            raise UnknownPropertyException("{} property doesnt exist".format(property_name))

