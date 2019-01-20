from sklearn.neighbors import KernelDensity
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import LeaveOneOut
import pandas as pd
import numpy as np

from weatherstate import EarthDailyWeatherMeasureModel
from weatherstate import DailyWeatherMeasureModel
"""
This class using KDE to generate temperature, pressure and humidity distribution on each day for each city
It uses Kaggle Dataset to learn this distribution. 
One models are generated the data used to create these tables are no longer required.
"""


class GenericModel:
    def build_model(self, city_name_list, pd_data, measure=None):
        earth_daily_weather_model = EarthDailyWeatherMeasureModel()

        for city in city_name_list:
            print("Building KDE model city {0} measure {1}".format(city,measure))
            pd_city_daily_measure = pd_data.groupby("datetime")[city].apply(list)

            ts = DailyWeatherMeasureModel()

            for month_day in pd_city_daily_measure.index:
                kde = KernelDensity(bandwidth=1.0, kernel='gaussian')
                x = np.array(pd_city_daily_measure[month_day])
                x = x[~np.isnan(x)].astype(int)
                kde.fit(x[:, None])
                ts[month_day] = kde
            earth_daily_weather_model[city] = ts
        return earth_daily_weather_model


class TemperatureModel(GenericModel):
    def __init__(self, pd_temperature, city_name_list):
        self.pd_temperature = pd_temperature
        self.city_name_list = city_name_list
        self.pd_temperature["datetime"] = self.pd_temperature["datetime"].apply(lambda x: x[5:10])
        self.earth_daily_temperature_model = self.build_model(self.city_name_list, self.pd_temperature, "temperature")
        print("===================================================")

    @property
    def represent(self):
        return self.earth_daily_temperature_model


class PressureModel(GenericModel):
    def __init__(self, pd_pressure, city_name_list):
        self.pd_pressure = pd_pressure
        self.city_name_list = city_name_list
        self.pd_pressure["datetime"] = self.pd_pressure["datetime"].apply(lambda x: x[5:10])
        self.earth_daily_pressure_model = self.build_model(self.city_name_list, self.pd_pressure, "pressure")
        print("===================================================")

    @property
    def represent(self):
        return self.earth_daily_pressure_model


class HumidityModel(GenericModel):
    def __init__(self, pd_humidity, city_name_list):
        self.pd_humidity = pd_humidity
        self.city_name_list = city_name_list
        self.pd_humidity["datetime"] = self.pd_humidity["datetime"].apply(lambda x: x[5:10])
        self.earth_daily_humdity_model = self.build_model(self.city_name_list, self.pd_humidity, "humidity")
        print("===================================================")

    @property
    def represent(self):
        return self.earth_daily_humdity_model
