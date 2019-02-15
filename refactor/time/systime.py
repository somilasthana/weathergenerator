from refactor.contract.time import SimulationTick
import datetime
import pytz


class SimulationSystemTime(SimulationTick):

    """
    This class provides current time in isoformat it considers timezone of each cities
    For instance, Sydney is in Australia/Sydney zone while New York is in America/New_York
    zone which means the same system time will be adjusted
    Sydney Time   is '2019-02-09T19:02:16.479108+11:00'  ie 7:02 pm
    New York Time is '2019-02-09T03:02:16.479108-05:00'  ie 3:02 am

    In addition the implementation needs only one instance of SimulationSystemTime to avoid any
    discrepancies. Therefore SimulationSystemTime is implemented as Singleton.

    s1 = SimulationSystemTime()
    s2 = SimulationSystemTime()

    assert s1 == s2

    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SimulationSystemTime, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance

    def get_time(self, timezone = "UTC"):
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        pst_now = utc_now.astimezone(pytz.timezone(timezone))
        return pst_now.isoformat()

    def get_hour(self, timezone = "UTC"):
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        pst_now = utc_now.astimezone(pytz.timezone(timezone))
        return pst_now.hour

    def get_day(self, timezone="UTC"):
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        pst_now = utc_now.astimezone(pytz.timezone(timezone))
        return pst_now.day

    def get_month(self, timezone="UTC"):
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        pst_now = utc_now.astimezone(pytz.timezone(timezone))
        return pst_now.month

    def get_year(self, timezone="UTC"):
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        pst_now = utc_now.astimezone(pytz.timezone(timezone))
        return pst_now.year
