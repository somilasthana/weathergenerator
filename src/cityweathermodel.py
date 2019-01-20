import random
from sklearn.neighbors import KernelDensity
import datetime
import pytz

from weatherstate import WeatherTransitions


class CityWeatherMeasureModel:
    """
    For each city this class keeps 3 measure models .
    The implementation uses Kernel Density Model to create probability distribution daily measures
    Since there are 366 days in leap year.
    daily_model_temperature contains 366 KDE models for temperature projection
    daily_model_pressure contains 366 KDE models for pressure projection
    daily_model_humidity 366 KDE models for humidity projection
    """

    def __init__(self, cityname, daily_model_temperature, daily_model_pressure, daily_model_humidity):
        self.cityname = cityname

        self.model = {
            "temperature": daily_model_temperature,
            "pressure": daily_model_pressure,
            "humidity": daily_model_humidity
        }
        
    @property
    def getmodel(self):
        return self.model


class CityWeatherModel:
    """
    For each city this class consist of
    temperature,pressure,humidity model
    weather condition model  as city_weather_condition_model
    city details
    Basically all the information needed to generate new weather records
    """

    def __init__(self, cityname, city_measure_model, city_weather_condition_model, city_details):
        self.cityname = cityname
        self.city_measure_model = city_measure_model
        self.weather_type_transition_model = city_weather_condition_model[0]
        self.weather_type_initial_transitions = city_weather_condition_model[1]
        self.city_details = city_details
        self.current_weather_condition = None
        self.current_specific_date = None

    @property
    def name(self):
        return self.cityname

    def generate_measure(self, specific_date):
        return self.sample(specific_date)
    
    def generate_time(self):
        # Consider Zones as cities belong to different zones 
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        pst_now = utc_now.astimezone(pytz.timezone(self.city_details.timezone))
        return pst_now.isoformat(),pst_now.strftime("%m-%d")

    def generate_record(self, config):

        currtime,specific_date = self.generate_time()
        
        if config.specific_date is not None:
            # Needs to generate records for particular day of the month
            specific_date = config.specific_date
            
        sample_measure = self.generate_measure(specific_date)

        record = list()
        record.append(self.city_details.name)
        record.append(",".join(map(str,[ "{0:.2f}".format(self.city_details.latitude), "{0:.2f}".format(self.city_details.longitude), 0])))
        record.append(currtime)

        for measure_type in ["conditions", "temperature", "pressure", "humidity"]:
            record.append(sample_measure[measure_type])

        return record

    def sample(self, specific_date):

        # Pick one for error checking ; It wont happen as we create models for all dates
        if specific_date not in self.city_measure_model.getmodel["temperature"].keys():
            specific_date = None

        if specific_date is None:
            print("Date {} not appropriate exiting...".format(specific_date))
            raise Exception()

        sample_measure = {}
        for measure_type in ["temperature", "pressure", "humidity"]:
            sample_measure[measure_type] = self.city_measure_model.getmodel[measure_type][specific_date].sample().flatten()[0]

        ctemperature = sample_measure["temperature"] - 273.15
        
        if ctemperature > 0:
            sample_measure["temperature"] = "+"+ "{0:.1f}".format(ctemperature)
        else:
            sample_measure["temperature"] = "{0:.1f}".format(ctemperature)
            
        sample_measure["pressure"] = "{0:.1f}".format(sample_measure["pressure"])   
        sample_measure["humidity"] = "{0:.0f}".format(sample_measure["humidity"])

        if self.current_specific_date != specific_date and self.current_weather_condition is None:
            # If the date doesnt change then no need to find the initial weather condition
            # or if current weather condition is already assigned then use that.
            self.current_specific_date = specific_date
            self.current_weather_condition = random.choices(population=self.weather_type_initial_transitions.columns,
                                                 weights=self.weather_type_initial_transitions.loc[specific_date].values, k=1)
            self.current_weather_condition = self.current_weather_condition[0]

        condition = random.choices(population=self.weather_type_transition_model.columns,
                                                      weights=self.weather_type_transition_model.loc[
                                                          self.current_weather_condition].values,
                                                      k=1)
        
        sample_measure["conditions"] = condition[0]

        return sample_measure


class CityWeatherConditionModel:

    def __init__(self, config, city_name, pd_weather):
        self.city_name = city_name
        self.config = config
        self.pd_weather = pd_weather
        self._process()

    def compute_daily_weather_transition_states(self, pd_weather_city):
        """
        This is used
        """
        df = pd_weather_city.pivot_table(index='month_day', columns=self.city_name, aggfunc='size', fill_value=0)

        df["marginal_day"] = df.sum(axis=1)
        df.loc["marginal_wtype"] = df.sum(axis=0)
        largest_value = df["marginal_day"].max()

        if largest_value != 0:
            df = df / largest_value
        else:
            raise Exception()

        for col_name in df.columns:
            if col_name != "marginal_day":
                df[col_name] = df[col_name] / df["marginal_day"]
        sstate = list(df.columns)
        sstate.remove("marginal_day")
        print("<cityweathermodel.py>:Calculating Initial Probabilities for city {0} for weather conditions [{1}]".format(self.city_name, ",".join(sstate)))
        
        
        df.drop(columns=["marginal_day"], inplace=True)

        return df

    def compute_weather_transition_states(self, pd_weather_city):
        vv_prev = pd_weather_city[self.city_name].values

        state_change = {}
        for curr, ncurr in zip(vv_prev, vv_prev[1:]):
            state_change.setdefault(curr, {})
            state_change[curr].setdefault(ncurr, 0)
            state_change[curr][ncurr] += 1
        hmap = {key: cnt for cnt, key in enumerate(state_change.keys())}
        
        print("<cityweathermodel.py>:Calculating Conditional Probabilities for city {0} for weather conditions [{1}]".format(self.city_name, ",".join(hmap.keys())))

        weather_type_info = {}
        for state in state_change:
            weather_type_info.setdefault(state, [0] * len(hmap))
            for transit_state, transit_value in state_change[state].items():
                weather_type_info[state][hmap[transit_state]] = transit_value

        weather_states = WeatherTransitions(weather_type_info, index=weather_type_info.keys(),
                                                  columns=hmap.keys())

        def compute_marginal_probabilities_for_states(weather_states_table):
            weather_states_table["marginal_previous"] = weather_states_table.sum(axis=1)
            weather_states_table.loc["marginal_next"] = weather_states_table.sum(axis=0)

            largest_value = weather_states_table["marginal_previous"].max()
            if largest_value != 0:
                weather_states_table = weather_states_table / largest_value
            else:
                raise Exception()

            for col_name in weather_states_table.columns:
                if col_name != "marginal_previous":
                    weather_states_table[col_name] = weather_states_table[col_name] / weather_states_table[
                        "marginal_previous"]
            weather_states_table.drop(columns=["marginal_previous"], inplace=True)
            return weather_states_table

        return compute_marginal_probabilities_for_states(weather_states)

    def _process(self):
        pd_weather_city = self.pd_weather[["datetime", self.city_name]]
        pd_weather_city["month_day"] = pd_weather_city["datetime"].apply(lambda x: x[5:10])
        self.weather_transitions = self.compute_weather_transition_states(pd_weather_city)
        self.weather_daily_transitions = self.compute_daily_weather_transition_states(pd_weather_city)

    @property
    def transitions(self):
        return self.weather_transitions, self.weather_daily_transitions