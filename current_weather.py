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
#location = input("Enter the city name: ")

#Weather url
#complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+creds.user_api
#api_link = requests.get(complete_api_link)
#api_data = api_link.json()


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



def display_current_weather_info(api_data, location):
    """
    Prints formatted weather information about a city.
    """
    temp_city = ((api_data['main']['temp']) - 273.15)
    feels_like = ((api_data["main"]["feels_like"]) - 273.15)
    country= api_data["sys"]["country"]
    weather_desc = api_data['weather'][0]['description']
    weather_id = api_data["weather"][0]["id"]
    humidity = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    tprint(location.upper())
    print ("----------------------------------------------------------------")
    print ("Weather Status for - {}  || {} || {}".format(location.upper(),country, date_time))
    print ("----------------------------------------------------------------")
    # Assign the the weather_display function to the weather_symbol variable 
    weather_symbol = select_weather_display_params(weather_id)
    print ("Current temperature is  : {:.2f} deg C".format(temp_city))
    print ("Currently it feels like : {:.2f} deg C".format(feels_like))
    print ("Weather condition is    :",weather_desc)
    print ("Current weather descrip :",weather_symbol)
    print ("Current Humidity is     :",humidity, '%')
    print ("Current wind speed is   :",wind_spd ,'kmph')

#current_weather_info = display_current_weather_info(api_data)