from refactor.simulation.simulation_reporterfactory import SimulatorReporterFactory
from refactor.simerror.unknown import UnknownConfigException
from refactor.config import Config


def get_config(conf_path):
    return Config(config_file_path=conf_path)


def test_Reporter():
    f = SimulatorReporterFactory(None)
    assert f is not None

    try:
        f.get_reporter()
        assert False
    except UnknownConfigException:
        assert True

    conf = get_config("../simulationconfig.yml")
    simulation_config = conf("simulation_report")

    f = SimulatorReporterFactory(simulation_config)
    r = f.get_reporter()


if __name__ == '__main__':

    test_Reporter()