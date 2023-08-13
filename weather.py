# Required libraries
import argparse
import json
import sys
from configparser import ConfigParser
from urllib import error, parse, request


#import the style.py file
import style

#weather URL
BASE_WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"


#map the weather codes to weather icons
weather_icons = {
    #day icons
    "01d" : "☀️",
    "02d" : "⛅",
    "03d" : "☁️",
    "04d" : "☁️",
    "09d" : "🌧️",
    "10d" : "🌦️",
    "11d" : "🌩️",
    "13d" : "☃️",
    "50d" : "💨",
    #night icons
    "01n" : "🌙",
    "02n" : "☁️",
    "03n" : "☁️",
    "04n" : "☁️",
    "09n" : "🌧️",
    "10n" : "🌧️",
    "11n" : "🌩️",
    "13n" : "☃️",
    "50n" : "💨",
}


# Weather Condition Codes
# https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
THUNDERSTORM = range(200, 300)
DRIZZLE = range(300, 400)
RAIN = range(500, 600)
SNOW = range(600, 700)
ATMOSPHERE = range(700, 800)
CLEAR = range(800, 801)
CLOUDY = range(801, 900)


def read_user_cli_args():
    """Handles the CLI user interactions.

    Returns:
        argparse.Namespace: Populated namespace object
    """
    parser = argparse.ArgumentParser(
        description="checks weather and temperature for a certain city"
    )
    parser.add_argument(
        "city", nargs="+", type=str, help="enter the city name"
    )
    parser.add_argument(
        "-i",
        "--imperial",
        action="store_true",
        help="display the temperature in imperial units",
    )
    return parser.parse_args()


def build_weather_query(city_input, imperial=False):
    """Builds the URL for an API request to OpenWeather's Weather API.

    Args:
        city_input (List[str]): Name of a city as collected by argparse
        imperial (bool): Whether or not to use imperial units for temperature

    Returns:
        str: URL formatted for a call to OpenWeather's city name endpoint
    """
    api_key = _get_api_key()
    city_name = " ".join(city_input)
    url_encoded_city_name = parse.quote_plus(city_name)
    units = "imperial" if imperial else "metric"
    url = (
        f"{BASE_WEATHER_API_URL}?q={url_encoded_city_name}"
        f"&units={units}&appid={api_key}"
    )
    return url


def _get_api_key():
    """Fetch the API key from your configuration file.

    Expects a configuration file named "key.ini" with structure:

        [openweather]
        api_key=<YOUR-OPENWEATHER-API-KEY>
    """
    config = ConfigParser()
    config.read("key.ini")
    return config["openweather"]["api_key"]


def get_weather_data(query_url):
    """Makes an API request to a URL and returns the data as a Python object.

    Args:
        query_url (str): URL formatted for OpenWeather's city name endpoint

    Returns:
        dict: Weather information for a specific city
    """
    try:
        response = request.urlopen(query_url)
    except error.HTTPError as http_error:
        if http_error.code == 401:  # 401 - Unauthorized
            sys.exit("Access denied. Check your API key.")
        elif http_error.code == 404:  # 404 - Not Found
            sys.exit("Can't find weather data for this city.")
        else:
            sys.exit(f"Something went wrong... ({http_error.code})")

    data = response.read()

    try:
        return json.loads(data)
    except json.JSONDecodeError:
        sys.exit("Couldn't read the server response.")


def display_weather_info(weather_data, imperial=False):
    """Prints formatted weather information about a city.

    Args:
        weather_data (dict): API response from OpenWeather by city name
        imperial (bool): Whether or not to use imperial units for temperature

    More information at https://openweathermap.org/current#name
    """
    city = weather_data["name"]
    country = weather_data["sys"]["country"]
    weather_id = weather_data["weather"][0]["id"]
    weather_description = weather_data["weather"][0]["description"]
    temperature = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    
    style.change_color(style.REVERSE)
    print(f"{city:^{style.PADDING}}, {country} ", end="")
    style.change_color(style.RESET)
    
    weather_symbol, color = _select_weather_display_params(weather_id)
    style.change_color(color)
    print(f"\t{weather_symbol}", end=" ")
    print(
    f"\t{weather_description.capitalize():^{style.PADDING}}",
    end=" ",
    )
    style.change_color(style.RESET)
    print(f"({temperature}°{'F' if imperial else 'C'}) & feels like ({feels_like}°{'F' if imperial else 'C'})")


def _select_weather_display_params(weather_id):
    """Selects a weather symbol and a display color for a weather state
    Args:
        weather_id (int): Weather condition code from the OpenWeather AP
    Returns:
        tuple[str]: Contains a weather symbol and a display color
    """
    
#     # match weather_id:
#     #     case "THUNDERSTORM":
#     #         display_params = ("💥", style.RED)
#     #     case "DRIZZLE":
#     #         display_params = ("💧", style.CYAN)
#     #     case "RAIN":
#     #         display_params = ("💦", style.BLUE)
#     #     case "SNOW":
#     #         display_params = ("⛄️", style.WHITE)
#     #     case "ATMOSPHERE":
#     #         display_params = ("🌀", style.BLUE)
#     #     case "CLEAR":
#     #         display_params = ("🔆", style.YELLOW)
#     #     case "CLOUDY":
#     #         display_params = ("💨", style.WHITE)
#     #     case _:
#     #         display_params = ("🌈", style.RESET)
            
            
    
    if weather_id in THUNDERSTORM:
        display_params = ("💥", style.RED)
    elif weather_id in DRIZZLE:
        display_params = ("💧", style.CYAN)
    elif weather_id in RAIN:
        display_params = ("💦", style.BLUE)
    elif weather_id in SNOW:
        display_params = ("⛄️", style.WHITE)
    elif weather_id in ATMOSPHERE:
        display_params = ("🌀", style.BLUE)
    elif weather_id in CLEAR:
        display_params = ("🔆", style.YELLOW)
    elif weather_id in CLOUDY:
        display_params = ("💨", style.WHITE)
    else:  # In case the API adds new weather codes
        display_params = ("🌈", style.RESET)
    return display_params
