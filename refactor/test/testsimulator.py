from refactor.simulation.basicsimulator import BasicSimulator
from refactor.simulation.cityweathersimulator import CityWeatherSimulator
from refactor.contract.process import Process
from refactor.simulation.stringreporter import StringBasedReporter
from refactor.simerror.unknown import UnknownCityAttributesException
from refactor.config import Config
from refactor.utils.citydetails import CityMetaAttributes
from refactor.simerror.unknown import UnknownConfigException
from refactor.simulation.simulation_reporterfactory import SimulatorReporterFactory


def test_BasicSimulator():

    class MyTask(Process):
        def __init__(self):
            pass

        def run_method(self):
            pass

        def get_state(self):
            return "1"

        def cleanup(self):
            pass

    b = BasicSimulator()

    b.initialize(1)
    task = MyTask()
    b.activate(task)
    b.simulate(None)
    b.stop()


def test_BasicSimulator_Reporter():

    class AddTask(Process):
        def __init__(self):
            self.i = 5
            self.y = 10

        def run_method(self):
            self.i = self.i + self.y

        def get_state(self):
            return str(self.i)

        def cleanup(self):
            pass

    reporter = StringBasedReporter(None)

    b = BasicSimulator()

    b.initialize(1)
    task = AddTask()
    b.activate(task)
    b.simulate(reporter)
    b.stop()

    assert reporter.string_save == str(15)

    ## Adding 2 tasks

    b = BasicSimulator()
    b.initialize(1)
    task = AddTask()
    b.activate(task)
    task = AddTask()
    b.activate(task)
    b.simulate(reporter)
    b.stop()

    assert len(b.tasklet) == 2


def get_config(conf_path):
    return Config(config_file_path=conf_path)


def test_CitySimulator():

    try:
        c = CityWeatherSimulator(None, None)
        assert False
    except UnknownCityAttributesException or UnknownConfigException:
        assert True

    conf = get_config("../simulationconfig.yml")
    simulation_config = conf("simulation_config")

    city_meta_attributes = CityMetaAttributes("../data/city_attributes_zone.csv")
    c = CityWeatherSimulator(simulation_config,
                             city_meta_attributes)

    assert c is not None
    assert (len(c.tasklet) == 36)


def test_RunSimulation():

    conf = get_config("../simulationconfig.yml")
    simulation_config = conf("simulation_config")

    city_meta_attributes = CityMetaAttributes("../data/city_attributes_zone.csv")
    c = CityWeatherSimulator(simulation_config,
                             city_meta_attributes)

    c.simulate(None)


def test_RunSimulationReporter():

    conf = get_config("../simulationconfig.yml")
    simulation_config = conf("simulation_config")
    simulation_report = conf("simulation_report")

    city_meta_attributes = CityMetaAttributes("../data/city_attributes_zone.csv")

    c = CityWeatherSimulator(simulation_config,
                             city_meta_attributes)

    f = SimulatorReporterFactory(simulation_report)
    r = f.get_reporter()
    c.simulate(r)


if __name__ == '__main__':
    test_BasicSimulator()
    print("==================Basic with Reporter============================")
    test_BasicSimulator_Reporter()
    print("===================City Simulator===========================")
    test_CitySimulator()
    print("====================City Simulator==========================")
    test_RunSimulation()
    print("====================City Simulator with reporter==========================")
    test_RunSimulationReporter()

