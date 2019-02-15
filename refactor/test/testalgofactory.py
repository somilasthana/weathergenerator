from refactor.library.weatheralgofactory import WeatherModelFactoryImpl
from refactor.simerror.unknown import UnknownAlgoException
from refactor.utils.citydetails import CityMetaAttributes


def test_AlgoFactory():
    f = WeatherModelFactoryImpl()

    try:
        m = f.get_model(None, None)
        assert False
    except UnknownAlgoException:
        assert True

    m = f.get_model("naive", None)

    assert m is not None

    city_meta_attributes = CityMetaAttributes("../data/city_attributes_zone.csv")
    m = f.get_model("random", city_meta_attributes("Vancouver"))

    assert m is not None


if __name__ == '__main__':
    test_AlgoFactory()