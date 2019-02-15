import argparse
import sys
sys.path.append("..")
from refactor.simulation.simulatorfactory import SimulatorFactory
from refactor.simulation.simulation_reporterfactory import SimulatorReporterFactory
from refactor.config import Config
from refactor.utils.citydetails import CityMetaAttributes
from refactor.simlog.printlog import printlog


class WeatherSimulationClient:

    def __init__(self, city_meta_details, configuration_path):
        """
        WeatherSimulationClient is responsible run Simulation.
        :param city_meta_details: This file as City Attributes like
        :param configuration_path: This is a yml file which has system configurations
        """
        self._simulation = None
        self.sim_handler = None
        self.city_meta_details = city_meta_details
        self.configuration_path = configuration_path
        self.conf = Config(self.configuration_path)

    def setup(self):
        """
        This function uses "SimulatorFactory" class to generate Simulation object. Currently, we have SimpleSimulator
        but SimulatorFactory abstracts the complexity of creating and configuring any simulator object by
        enforcing "SimulatorFactoryInterface".
        :return: None
        """
        self._simulation = SimulatorFactory(self.conf("simulation_config"), CityMetaAttributes(self.city_meta_details)).get_simulator()
        self.sim_handler = SimulatorReporterFactory(self.conf(("simulation_report"))).get_reporter()

    def run(self):
        self._simulation.simulate(self.sim_handler)


def get_args():
    parser = argparse.ArgumentParser(description='Weather Data Generation')

    parser.add_argument('--citymetafile',
                        required=True,
                        help='The city meta file describing the city details')

    parser.add_argument('--config',
                        required=True,
                        help='The config file contains simulation configuration, debugging details,'
                             'schema for meta details')

    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()

    city_meta_file = args.citymetafile
    configuration_path = args.config

    printlog("WeatherSimulationClient", "Weather Data Generation Simulator")
    client = WeatherSimulationClient(city_meta_file, configuration_path)
    printlog("WeatherSimulationClient", "Initializing Weather Data Generation Simulator")
    client.setup()
    printlog("WeatherSimulationClient", "Running Weather Data Generation Simulator")
    client.run()
    printlog("WeatherSimulationClient", "Terminating Weather Data Generation Simulator")

