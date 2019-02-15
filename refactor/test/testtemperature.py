from refactor.constant import WeatherPropertiesRange


def test_Constant():

    assert WeatherPropertiesRange.MAX_TEMPERATURE.value == 50.0
    assert WeatherPropertiesRange.MIN_TEMPERATURE.value == 0


if __name__ == '__main__':
    test_Constant()