from refactor.utils.state import State


def test_StateClass():

    s = State(temperature=10, pressure=23, humidity=100, weather_condition="Sunny", city=())

    assert s["temperature"] == 10
    assert s["pressure"] == 23
    assert s["humidity"] == 100
    assert s["weather_condition"] == "Sunny"
    print(s.repr(["temperature", "pressure", "humidity", "weather_condition", "city"]))

    assert s.repr(["temperature", "pressure"]) == ['10', '23']
    assert s.repr(["temperature", "pressure", "humidity", "weather_condition"]) == ['10', '23', '100', 'Sunny']
    #assert s.repr(["temperature", "pressure", "humidity", "weather_condition", "city"]) == "10|23|100|Sunny|1.0|2.0"


if __name__ == '__main__':
    test_StateClass()