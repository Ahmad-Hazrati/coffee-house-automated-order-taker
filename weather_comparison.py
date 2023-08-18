# Required libraries
import requests
from datetime import datetime
import creds
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

#Request for user input
location_one = input("Enter the 1st city name: ")
location_two = input("Enter the 2nd city name: ")



#Weather url
complete_api_link_location_one = "https://api.openweathermap.org/data/2.5/weather?q="+location_one+"&appid="+creds.user_api
complete_api_link_location_two = "https://api.openweathermap.org/data/2.5/weather?q="+location_two+"&appid="+creds.user_api
api_link_one = requests.get(complete_api_link_location_one)
api_link_two = requests.get(complete_api_link_location_two)

api_data_one = api_link_one.json()
api_data_two = api_link_two.json()

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

def display_comparison_weather_info_one(api_data_one, location_one):
    """
    Prints formatted weather information about a city.
    """
    temp_city = ((api_data_one['main']['temp']) - 273.15)
    feels_like = ((api_data_one["main"]["feels_like"]) - 273.15)
    country= api_data_one["sys"]["country"]
    weather_desc = api_data_one['weather'][0]['description']
    weather_id = api_data_one["weather"][0]["id"]
    humidity = api_data_one['main']['humidity']
    wind_spd = api_data_one['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    tprint(location_one.upper())
    print ("----------------------------------------------------------------")
    print ("Weather Status for - {}  || {} || {}".format(location_one.upper(),country, date_time))
    print ("----------------------------------------------------------------")
    # Assign the the weather_display function to the weather_symbol variable 
    weather_symbol = select_weather_display_params(weather_id)
    print ("Current temperature is  : {:.2f} deg C".format(temp_city))
    print ("Currently it feels like : {:.2f} deg C".format(feels_like))
    print ("Weather condition is    :",weather_desc)
    print ("Current weather descrip :",weather_symbol)
    print ("Current Humidity is     :",humidity, '%')
    print ("Current wind speed is   :",wind_spd ,'kmph')
    print ("----------------------------------------------------------------\n\n")
    
def display_comparison_weather_info_two(api_data_two, location_two):
    """
    Prints formatted weather information about a city.
    """
    temp_city = ((api_data_two['main']['temp']) - 273.15)
    feels_like = ((api_data_two["main"]["feels_like"]) - 273.15)
    country= api_data_two["sys"]["country"]
    weather_desc = api_data_two['weather'][0]['description']
    weather_id = api_data_two["weather"][0]["id"]
    humidity = api_data_two['main']['humidity']
    wind_spd = api_data_two['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    tprint(location_two.upper())
    print ("----------------------------------------------------------------")
    print ("Weather Status for - {}  || {} || {}".format(location_two.upper(),country, date_time))
    print ("----------------------------------------------------------------")
    # Assign the the weather_display function to the weather_symbol variable 
    weather_symbol = select_weather_display_params(weather_id)
    print ("Current temperature is  : {:.2f} deg C".format(temp_city))
    print ("Currently it feels like : {:.2f} deg C".format(feels_like))
    print ("Weather condition is    :",weather_desc)
    print ("Current weather descrip :",weather_symbol)
    print ("Current Humidity is     :",humidity, '%')
    print ("Current wind speed is   :",wind_spd ,'kmph')
    print ("----------------------------------------------------------------")

display_comparison_weather_info_one(api_data_two, location_one)
display_comparison_weather_info_two(api_data_two, location_two)


    
