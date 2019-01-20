
"""
Different Weather Types Extracted from Kaggle Weather Data

https://www.kaggle.com/selfishgene/historical-hourly-weather-data

"""

from config import ConfigState

weather_mapping = {

    'mist': 'Foggy',
    'broken clouds': 'Cloudy',
    'sky is clear': 'Clearsky',
    'light rain': 'Rainy',
    'few clouds': 'Cloudy',
    'fog': 'Foggy',
    'overcast clouds': 'Cloudy',
    'light intensity shower rain': 'Rainy',
    'moderate rain': 'Rainy',
    'light intensity drizzle': 'Rainy',
    'scattered clouds': 'Cloudy',
    'proximity shower rain': 'Rainy',
    'heavy intensity rain': 'Rainy',
    'heavy snow': 'Snow',
    'shower rain': 'Rainy',
    'snow': 'Snow',
    'heavy shower snow': 'Snowstorm',
    'light intensity drizzle rain': 'Rainy',
    'light snow': 'Snow',
    'very heavy rain': 'Rainy',
    'smoke': 'Smog',
    'thunderstorm with heavy rain': 'Thunderstorm',
    'light shower snow': 'Snow',
    'thunderstorm': 'Thunderstorm',
    'thunderstorm with light rain': 'Thunderstorm',
    'haze': 'Smog',
    'dust': 'Smog',
    'volcanic ash': 'Smog',
    'heavy intensity shower rain': 'Rainy',
    'thunderstorm with rain': 'Thunderstorm',
    'sleet': 'Snow',
    'light rain and snow': 'Snow',
    'drizzle': 'Rainy',
    'shower snow': 'Snowstorm',
    'light shower sleet': 'Snow',
    'proximity thunderstorm': 'Thunderstorm',
    'ragged thunderstorm': 'Thunderstorm',
    'freezing rain': 'Snow',
    'heavy intensity drizzle': 'Rainy',
    'proximity thunderstorm with rain': 'Thunderstorm',
    'proximity thunderstorm with drizzle': 'Thunderstorm',
    'thunderstorm with drizzle': 'Thunderstorm',
    'thunderstorm with light drizzle': 'Thunderstorm',
    'thunderstorm with heavy drizzle': 'Thunderstorm',
    'heavy thunderstorm': 'Thunderstorm',
    'squalls': 'Windy',
    'proximity sand/dust whirls': 'Sandstorm',
    'proximity moderate rain': 'Rainy',
    'sand': 'Sandstorm',
    'sand/dust whirls': 'Sandstorm',
    'tornado': 'Tornado',
    'shower drizzle': 'Rainy',
    'rain and snow': 'Snow',
    'ragged shower rain': 'Rain'
}


class WeatherStateType(ConfigState):

    """
    Kaggle Dataset provides multiple types of weather condition
    to simplify we only pick handful of weather condtions.
    """
    pass


different_weather_types = WeatherStateType(**weather_mapping)