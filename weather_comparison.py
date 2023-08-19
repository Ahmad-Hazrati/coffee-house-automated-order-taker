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

#Request for user input
#location_one = input("Enter the 1st city name: \n")
#location_two = input("Enter the 2nd city name: \n")



#Weather url
# complete_api_link_location_one = "https://api.openweathermap.org/data/2.5/weather?q="+location_one+"&appid="+creds.user_api
# complete_api_link_location_two = "https://api.openweathermap.org/data/2.5/weather?q="+location_two+"&appid="+creds.user_api
# api_link_one = requests.get(complete_api_link_location_one)
# api_link_two = requests.get(complete_api_link_location_two)

# api_data_one = api_link_one.json()
# api_data_two = api_link_two.json()

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

def display_weather_info_location_one(api_data_one, location_one):
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
    
def display_weather_info_location_two(api_data_two, location_two):
    """
    Prints formatted weather information about a city.
    """
    temp_city_two = ((api_data_two['main']['temp']) - 273.15)
    feels_like_two = ((api_data_two["main"]["feels_like"]) - 273.15)
    country_two= api_data_two["sys"]["country"]
    weather_desc_two = api_data_two['weather'][0]['description']
    weather_id_two = api_data_two["weather"][0]["id"]
    humidity_two = api_data_two['main']['humidity']
    wind_spd_two = api_data_two['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    tprint(location_two.upper())
    print ("----------------------------------------------------------------")
    print ("Weather Status for - {}  || {} || {}".format(location_two.upper(),country_two, date_time))
    print ("----------------------------------------------------------------")
    # Assign the the weather_display function to the weather_symbol variable 
    weather_symbol_two = select_weather_display_params(weather_id_two)
    print ("Current temperature is  : {:.2f} deg C".format(temp_city_two))
    print ("Currently it feels like : {:.2f} deg C".format(feels_like_two))
    print ("Weather condition is    :",weather_desc_two)
    print ("Current weather descrip :",weather_symbol_two)
    print ("Current Humidity is     :",humidity_two, '%')
    print ("Current wind speed is   :",wind_spd_two ,'kmph')
    print ("----------------------------------------------------------------\n")

# display_weather_info_location_one(api_data_one, location_one)
# display_weather_info_location_two(api_data_two, location_two)


# def weather_comparison(location_one, location_two):
#     if api_data_one["weather"][0]["main"] == api_data_two["weather"][0]["main"]:
#         print (f"The weather of {location_one} and {location_two} are same.")
#         print(f"The weather condition of both cities are", api_data_one['weather'][0]['description'])
#         print ("----------------------------------------------------------------")
#     else:    
#         if api_data_one["weather"][0]["main"] == "Clear" and api_data_two["weather"][0]["main"] != "Clear":
#             print(f"The weather of {location_one} is better than the weather of {location_two}.")
#             print(f"The weather condition is", api_data_one['weather'][0]['description'])
#             print ("----------------------------------------------------------------")
#             #print(f"{location_one}, is sunny ☀️!")
#         elif api_data_one["weather"][0]["main"] == "Clouds" and api_data_two["weather"][0]["main"] != "Clouds" or "Clear":
#             print(f"The weather of {location_one} is better than the weather of {location_two}.")
#             print(f"The weather condition is", api_data_one['weather'][0]['description'])
#             print ("----------------------------------------------------------------")
#             #print(f"{location_one}, is cloudy ☁️!")
#         elif api_data_one["weather"][0]["main"] == "Rain" and api_data_two["weather"][0]["main"] != "Rain" or "Clouds" or "Clear":
#             print(f"The weather of {location_one} is better than the weather of {location_two}.")
#             print(f"The weather condition is", api_data_one['weather'][0]['description'])
#             print ("----------------------------------------------------------------")
#             #print(f"{location_one}, is rainy 🌦️!")
#         elif api_data_one["weather"][0]["main"] == "Drizzle" and api_data_two["weather"][0]["main"]  != "Drizzle" or "Rain" or "Clouds" or "Clear":
#             print(f"The weather of {location_one} is better than the weather of {location_two}.")
#             print(f"The weather condition is", api_data_one['weather'][0]['description'])
#             print ("----------------------------------------------------------------")
#             #print(f"{location_one} is drizzle 🌧️!")
#         elif api_data_one["weather"][0]["main"] == "Snow" and api_data_two["weather"][0]["main"]  != "Snow" or "Drizzle" or "Rain" or "Clouds" or "Clear":
#             print(f"The weather of {location_one} is better than the weather of {location_two}.")
#             print(f"The weather condition is", api_data_one['weather'][0]['description'])
#             print ("----------------------------------------------------------------")
#             #print(f"{location_one} is Snowy ⛄️!")
#         elif api_data_one["weather"][0]["main"] == "Thunderstorm" and api_data_two["weather"][0]["main"]  != "Thunderstorm" or "Snow" or "Drizzle" or "Rain" or "Clouds" or "Clear":
#             print(f"The weather of {location_one} is better than the weather of {location_two}.")
#             print(f"The weather is condition", api_data_one['weather'][0]['description'])
#             print ("----------------------------------------------------------------")
#             #print(f"{location_one} is Thunderstromy 🌩️!")
#         else:
#             print(f"The weather of {location_two} is better than the weather of {location_one}.")
#             print(f"The weather condition is", api_data_two['weather'][0]['description'])
#             print ("----------------------------------------------------------------")
            
            
    
#print(weather_comparison(location_one, location_two))