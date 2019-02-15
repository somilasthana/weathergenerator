from refactor.utils.citydetails import CityMetaAttributes


def test_city_details(csvfile):

    city_meta_details_handler = CityMetaAttributes(csvfile)

    Vancouver = city_meta_details_handler("Vancouver")
    assert Vancouver["cityname"] == "Vancouver"
    assert float(Vancouver["latitude"]) == 49.24966
    assert float(Vancouver["longitude"]) == -123.119339
    assert Vancouver["country"] == "Canada"
    assert Vancouver["zone"] == "America/Vancouver"
    assert int(Vancouver["sea_level"]) == 10


if __name__ == '__main__':
    test_city_details("../data/city_attributes_zone.csv")
