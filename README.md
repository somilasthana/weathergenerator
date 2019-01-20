# Generate Weather Data Using Kaggle Dataset
This mini project generates weather data for cities. 

However, Our earth we used to generate or project weather data is only limited to 36 cities. These are the same cities provided
by Kaggle https://www.kaggle.com/selfishgene/historical-hourly-weather-data. 

Kaggle was nice to provide latitude, longitude, weather condition, temperature, pressure, humidity details for 36 cities from 2012 till 2017.

## List of Cities
These 36 cities are 
```
['Vancouver', 'Portland', 'San Francisco', 'Seattle', 'Los Angeles',
       'San Diego', 'Las Vegas', 'Phoenix', 'Albuquerque', 'Denver',
       'San Antonio', 'Dallas', 'Houston', 'Kansas City', 'Minneapolis',
       'Saint Louis', 'Chicago', 'Nashville', 'Indianapolis', 'Atlanta',
       'Detroit', 'Jacksonville', 'Charlotte', 'Miami', 'Pittsburgh',
       'Toronto', 'Philadelphia', 'New York', 'Montreal', 'Boston',
       'Beersheba', 'Tel Aviv District', 'Eilat', 'Haifa', 'Nahariyya',
       'Jerusalem']
```


## Kaggle Data Details
Kaggle provides:
* Weather Condtion: ( Rainy, Clearsky, Snow etc ) for all 36 cities per hour. However, the category used by Kaggle dataset is way to granular we narrowed it down to handle full categories 
```
['Tornado', 'Rainy', 'Sandstorm', 'Snow', 'Foggy', 'Cloudy', 'Windy', 'Rain', 'Snowstorm', 'Clearsky', 'Smog', 'Thunderstorm']
```
For example, 'thunderstorm with light drizzle', 'thunderstorm with heavy drizzle','heavy thunderstorm' where all mapped as 'Thunderstorm' in our system.

* Temperature, Pressure, Humidity Details for all 36 cities per hour. However, few Nan where removed.

## Reason for Using Kaggle Data
The reason for learning from past data and projecting weather data is that it makes simulation easy and far more superior to implement. 
*  weather_description.csv: provides Weather Condtions for all 36 cities in following form
![Weather Condtion](https://github.com/somilasthana/weathergenerator/blob/master/pics/weather_description.png)

After converting into handful of weather conditions ( src/weathertype.py ) we could use **Bayes Probability** to develop a simple model which answers

give "01-20" ie January month, 20th if it was **Cloudy** in "Chicago" what is probability that next condition to be 
Cloudy, Rainy, Snow, Clearsky. This can be calculated by applying Bayes probability formula. which cases
```
P(next_condition = Snow | present_condition = Cloudy ) 
            = P ( next_condition = Snow and present_condition = Cloudy) / P( present_condition = Cloudy )
```
We build these models for every day of the year for all cities and for all weather conditions. Listing all probabilities we use numpy random function with list of proabililites as weights to decide the next weather condition.

* temperature.csv, pressure.csv, humidity.csv
For illustration purpose here is snapshot of temperature dataset
![Temperature Details](https://github.com/somilasthana/weathergenerator/blob/master/pics/temperature_details.png)

One can group temperature measures ( it is measured in Kelvin ) for each day of the month and if we plot a histogram we see something like this. We plotted for city Vancouver for 01-01 ( 1 Jan )

![Temperature Histogram](https://github.com/somilasthana/weathergenerator/blob/master/pics/temperature_distribution.png)
One can easily make out some form of distribution and can use Kernel Density Model ( which is a generative model ) to smoothen the curve as shown below

![Temperature Smooth](https://github.com/somilasthana/weathergenerator/blob/master/pics/temperature_smooth.png)

This KDE model can use be used randomly generate temperature for that particular month day. Similar KDE models where build for Pressure and Humidity measures.

