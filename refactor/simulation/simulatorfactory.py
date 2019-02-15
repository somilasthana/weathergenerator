from refactor.contract.factory import SimulatorFactoryInterface
from refactor.constant import SimulationType
from refactor.simulation.basicsimulator import BasicSimulator
from refactor.simulation.cityweathersimulator import CityWeatherSimulator
from refactor.simerror.unknown import UnknownSimulatorException
from refactor.simerror.unknown import UnknownConfigException
from refactor.simlog.printlog import printlog
from refactor.config import Config


class SimulatorFactory(SimulatorFactoryInterface):

    def __init__(self, conf, city_meta_attributes):
        """
        Generic SimulatorFactory to create different Simulator Types. In this implementation we support
        only "SimpleSimulator" but a more complex simulator can be configured in conf and used.
        The restriction is that every simulator implementation should implement "SimulatorInterface"
        abstract class.
        :param conf: configuration file in form of yml format, which decides the type of simulator to invoke
        :param city_meta_attributes: CityMetaAttributes
        """
        self.simulation_config = conf
        self.simulator = None
        self.city_meta_attributes = city_meta_attributes
        self._configure_simulator()

    def _configure_simulator(self):
        """
        This function is helps in creating and configuring Simulator
        Reads "simulation_config" from config file. For example
        ###
        simulation_config:
           name: SimpleSimulator
           iterations: 1000
           maximum_task_to_run: 200
           city_config:
               default:
                   model_used: naive
        ####
          - name : Type of Simulator to create currently only "SimpleSimulator" is supported.
          - parameters: iterations          = number of iterations to run simulation
                        maximum_task_to_run = maximum capacity of simulator ( how many tasks it can run )

        The high-level architecture of "Simulator" works as follows:
                          per city                             contains
        SimpleSimulator ----------->  WeatherGeneratorProcess ----------> WeatherGenerationAlgorithm

        Each Simulator maintains a list of "WeatherGeneratorProcess" as tasks one for each city
        This task/process is created by delegating responsibility to "WeatherModelFactoryImpl"
        For task contains a specific "WeatherGenerationAlgorithm" to generate weather properties for
        that city.

        :return: None
        """

        if self.simulation_config is None:
            raise UnknownConfigException("Missing simulation_config in yaml")

        if self.simulation_config["name"] == SimulationType.SIMPLE_SIMULATOR.value:
            self.simulator = BasicSimulator()
        elif self.simulation_config["name"] == SimulationType.CITY_WEATHER_SIMULATOR.value:
            self.simulator = CityWeatherSimulator(self.simulation_config, self.city_meta_attributes)
        else:
            raise UnknownSimulatorException("Simulator provided does not exist {}".format(self.simulation_config["name"]))

        printlog("SimulatorFactory", "Using {} simulator".format(self.simulation_config["name"]))

        self.simulator.initialize(self.simulation_config["iterations"], self.simulation_config["maximum_task_to_run"])

    def get_simulator(self):
        """
        Returns the configured Simulator
        :return: Simulator Object
        """
        return self.simulator
