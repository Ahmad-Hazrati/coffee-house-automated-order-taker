# Required libraries
import requests
from datetime import datetime
from art import *

# Weather Condition Codes
# https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
THUNDERSTORM = range(200, 300)
DRIZZLE = range(300, 400)
RAIN = range(500, 600)
SNOW = range(600, 700)
ATMOSPHERE = range(700, 800)
CLEAR = range(800, 801)
CLOUDY = range(801, 900)

"""
#Request for user input
#location_one = input("Enter the 1st city name: \n")
#location_two = input("Enter the 2nd city name: \n")

#Weather url
complete_api_link_location_one = "https://api.openweathermap.org/data/2.5/"
"weather?q="+location_one+"&appid="+creds.user_api
complete_api_link_location_two = "https://api.openweathermap.org/data/2.5/"
"weather?q="
+location_two+"&appid="+creds.user_api
api_link_one = requests.get(complete_api_link_location_one)
api_link_two = requests.get(complete_api_link_location_two)

data = api_link_one.json()
api_d = api_link_two.json()
"""


def select_weather_display_params(weather_id):
    """
    Selects a weather symbol based on weather condition code
    extracted from the Openweather App.
    """
    if weather_id in THUNDERSTORM:
        display_params = "🌩️"
    elif weather_id in DRIZZLE:
        display_params = "🌧️"
    elif weather_id in RAIN:
        display_params = "🌦️"
    elif weather_id in SNOW:
        display_params = "⛄️"
    elif weather_id in ATMOSPHERE:
        display_params = "💨"
    elif weather_id in CLEAR:
        display_params = "☀️"
    elif weather_id in CLOUDY:
        display_params = "☁️"
    else:
        display_params = "🌈"
    return display_params


def display_weather_info_location_one(data, location_one):
    """
    Prints formatted weather information about a city.
    """
    if data["cod"] == "404":
        print("Invalid City: {}, Please check your city" +
              "name".format(location_one))
    elif data["cod"] == "401":
        print("Invalid API key, Please check your API key")
    else:
        temp_city = ((data['main']['temp']) - 273.15)
        feels_like = ((data["main"]["feels_like"]) - 273.15)
        country = data["sys"]["country"]
        weather_desc = data['weather'][0]['description']
        weather_id = data["weather"][0]["id"]
        humidity = data['main']['humidity']
        wind_spd = data['wind']['speed']
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
        tprint(location_one.upper())
        print("--------------------------------------------" +
              "--------------------")
        print("Weather Status for - {}  || {} || " +
              "{}".format(location_one.upper(), country, date_time))
        print("--------------------------------------------" +
              "--------------------")
        # Assign the the weather_display function
        # to the weather_symbol variable
        weather_symbol = select_weather_display_params(weather_id)
        print("Current temperature is  : {:.2f} deg C".format(temp_city))
        print("Currently it feels like : {:.2f} deg C".format(feels_like))
        print("Weather condition is    :", weather_desc)
        print("Current weather descrip :", weather_symbol)
        print("Current Humidity is     :", humidity, '%')
        print("Current wind speed is   :", wind_spd, 'kmph')
        print("----------------------------------------------------------"
              "------\n\n")


def display_weather_info_location_two(api_d, location_two):
    """
    Prints formatted weather information about a city.
    """
    if api_d["cod"] == "404":
        print("Invalid City: {}, Please check your city " +
              "name".format(location_two))
    elif api_d["cod"] == "401":
        print("Invalid API key, Please check your API key")
    else:
        temp_city_two = ((api_d['main']['temp']) - 273.15)
        feels_like_two = ((api_d["main"]["feels_like"]) - 273.15)
        country_two = api_d["sys"]["country"]
        weather_desc_two = api_d['weather'][0]['description']
        weather_id_two = api_d["weather"][0]["id"]
        humidity_two = api_d['main']['humidity']
        wind_spd_two = api_d['wind']['speed']
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

        tprint(location_two.upper())
        print("---------------------------------------------" +
              "-------------------")
        print("Weather Status for - {}  || {} || {}"
              .format(location_two.upper(), country_two, date_time))
        print("---------------------------------------------" +
              "-------------------")
        # Assign the the weather_display function
        # to the weather_symbol variable
        weather_symbol_two = select_weather_display_params(weather_id_two)
        print("Current temperature is  : {:.2f} deg C".format(temp_city_two))
        print("Currently it feels like : {:.2f} deg C".format(feels_like_two))
        print("Weather condition is    :", weather_desc_two)
        print("Current weather descrip :", weather_symbol_two)
        print("Current Humidity is     :", humidity_two, '%')
        print("Current wind speed is   :", wind_spd_two, 'kmph')
        print("----------------------------------------------" +
              "------------------\n")
