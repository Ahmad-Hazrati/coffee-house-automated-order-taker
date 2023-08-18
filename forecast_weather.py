

# Required libraries
import requests
from datetime import datetime
import creds
from art import *


#Request for user input
#location = input("Enter the city name: ")

#Weather url
# complete_api_link = "https://api.openweathermap.org/data/2.5/forecast?q="+location+"&appid="+creds.user_api
# api_link = requests.get(complete_api_link)
# api_data = api_link.json()



def select_weather_display_params(weather_id):
    """
    Selects a weather symbol based on weather condition code extracted from the Openweather App.
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


def display_forecast_weather_info(api_data):
    """
    Prints formatted weather information about a city.
    """
    tprint(location.upper())
    
    dates = []
    for el in api_data["list"]:
        date = el["dt_txt"].split(" ")[0]
        if date in dates:
            continue
        dates.append(date)
        temp_city = (el["main"]["temp"] - 273.15)
        feels_like = (el["main"]["feels_like"] - 273.15)
        weather_desc = el["weather"][0]["description"]
        weather_id = el["weather"][0]["id"]
        humidity = el["main"]['humidity']
        wind_spd = el["wind"]["speed"]
        print ("-----------------------------------------")
        print ("Weather Status on - {}  ".format(date))
        print ("-----------------------------------------")
        # Assign the the weather_display function to the weather_symbol variable
        weather_symbol = select_weather_display_params(weather_id)
        print ("Temperature will be         : {:.2f} deg C".format(temp_city))
        print ("It will feel like           : {:.2f} deg C".format(feels_like))
        print ("Weather condition will be   :",weather_desc)
        print ("Weather description will be :",weather_symbol)
        print ("Humidity will be            :",humidity, '%')
        print ("And Wind speed will be      :",wind_spd ,'kmph\n\n')
        

#forecast_weather_info = display_forecast_weather_info(api_data)


    