
from refactor.time.systime import SimulationSystemTime
import pytz

def test_systime():
    s = SimulationSystemTime().get_time()
    assert s is not None

    s = SimulationSystemTime().get_time("America/Los_Angeles")
    assert s is not None

    try:
        # misspelled zone
        s = SimulationSystemTime().get_time("America/Lo_Angeles")
        assert False
    except pytz.exceptions.UnknownTimeZoneError:
        assert True


def test_systime_details():
    h = SimulationSystemTime().get_hour()
    assert isinstance(h, int)

if __name__ == '__main__':
    test_systime()
    test_systime_details()