from refactor.simulation.simulatorfactory import SimulatorFactory
from refactor.config import Config
from refactor.simerror.unknown import UnknownCityAttributesException
from refactor.utils.citydetails import CityMetaAttributes


def get_config(conf_path):
    return Config(config_file_path=conf_path)


def test_Simulator():
    conf = get_config("../simulationconfig.yml")
    simulation_config = conf("simulation_config")
    try:
        simulation = SimulatorFactory(simulation_config, None).get_simulator()
        assert False
    except UnknownCityAttributesException:
        assert True

    city_meta_attributes = CityMetaAttributes("../data/city_attributes_zone.csv")
    simulation = SimulatorFactory(simulation_config, city_meta_attributes).get_simulator()


if __name__ == '__main__':
    test_Simulator()
