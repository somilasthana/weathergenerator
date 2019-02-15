from refactor.utils.state import State
from refactor.utils.citydetails import CityInformation
from refactor.utils.pipeformatter import PipeFormatter
from refactor.utils.cbaformatter import CBAFormatter
from refactor.time.systime import SimulationSystemTime


def test_Formatter():
    city = CityInformation(cityname="Vancouver",
                           latitude=49.24,
                           longitude=-123.12,
                           country="Canada",
                           zone="America/Vancouver",
                           sealevel=10)

    state = State(temperature=10,
                  pressure=1200,
                  humidity=20,
                  weather_condition="Sunny",
                  cityname="Vancouver",
                  latitude=49.24,
                  longitude=-123.12,
                  country="Canada",
                  zone="America/Vancouver",
                  sea_level=10,
                  time = SimulationSystemTime().get_time()
                  )
    keys_used = ["cityname", "latitude", "longitude", "country"]
    p = PipeFormatter(keys_used, None)
    assert p(city) == "Vancouver|49.24|-123.12|Canada"

    keys_used = ["temperature", "pressure", "humidity", "weather_condition", "cityname"]
    p = PipeFormatter(keys_used, None)
    assert p(state) == "10|1200|20|Sunny|Vancouver"

    keys_used = ["cityname", "latitude", "longitude", "sea_level", "time", "weather_condition", "temperature", "pressure", "humidity"]
    p = PipeFormatter(keys_used, None)
    #print(p(state))


def test_CBAFormatter():

    state = State(temperature=10,
                  pressure=1200,
                  humidity=20,
                  weather_condition="Sunny",
                  cityname="Vancouver",
                  latitude=49.24,
                  longitude=-123.12,
                  country="Canada",
                  zone="America/Vancouver",
                  sea_level=10,
                  time = SimulationSystemTime().get_time()
                  )

    keys_used = ["cityname", "latitude", "longitude", "sea_level", "time", "weather_condition", "temperature",
                 "pressure", "humidity"]
    keys_separator = [ "|",
      ",",
      ",",
      "|",
      "|",
      "|",
      "|",
      "|"
    ]

    cba = CBAFormatter(keys_used, keys_separator)
    print(cba(state))

    state = State(temperature=-20, # Negative Temperature
                  pressure=1200,
                  humidity=20,
                  weather_condition="Sunny",
                  cityname="Vancouver",
                  latitude=49.24,
                  longitude=-123.12,
                  country="Canada",
                  zone="America/Vancouver",
                  sea_level=10,
                  time = SimulationSystemTime().get_time()
                  )

    keys_used = ["cityname", "latitude", "longitude", "sea_level", "time", "weather_condition", "temperature",
                 "pressure", "humidity"]

    cba = CBAFormatter(keys_used, keys_separator)
    print(cba(state))

    # less fields
    keys_used = ["cityname", "latitude", "longitude", "sea_level", "weather_condition"]

    cba = CBAFormatter(keys_used, keys_separator)
    assert cba(state) == "Vancouver|49.24,-123.12,10|Sunny"

    # more fields

    # less fields
    keys_used = ["cityname", "latitude", "longitude", "sea_level", "time", "weather_condition", "temperature",
                 "pressure", "humidity", "latitude", "latitude", "latitude", "latitude"]

    cba = CBAFormatter(keys_used, keys_separator)
    print(cba(state))


if __name__ == '__main__':
    test_Formatter()
    test_CBAFormatter()