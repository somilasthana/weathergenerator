from refactor.config import Config


def test_ConfigClass(conf_path):

    conf = Config(config_file_path=conf_path)
    assert conf("mysql") is not None

    mysql = conf("mysql")
    assert mysql["host"] == "localhost"
    assert mysql["user"] == "root"
    assert mysql["passwd"] == "secret"
    assert mysql["db"] == "write-math"
    assert "arbit" not in mysql

    other = conf("other")
    assert "preprocessing.scale_and_center" in other["preprocessing_queue"]


def test_SimulationConfig(conf_path):
    conf = Config(config_file_path=conf_path)

    assert conf("simulation_config") is not None
    assert conf("simulation_report") is not None

    simulation_config = conf("simulation_config")

    assert "city_config" in simulation_config
    if "default" in simulation_config["city_config"]:
        assert "model_used" in simulation_config["city_config"]["default"]

    assert simulation_config["city_config"]["Vancouver"]["model_used"] == "naive"
    assert simulation_config["city_config"]["Denver"]["model_used"] == "random"

    simulation_report = conf("simulation_report")
    assert simulation_report['type'] == "filebased"
    assert simulation_report['details']['filename'] == 'weather_data.output'

    assert simulation_report['details']["keys_separator"] == ['|', ',', ',', '|', '|', '|', '|', '|']


if __name__ == '__main__':
    conf_path = "./dummy.yml"
    test_ConfigClass(conf_path)
    conf_path = "../simulationconfig.yml"
    test_SimulationConfig(conf_path)
