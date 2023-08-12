import argparse
import json
import sys
from configparser import ConfigParser
from urllib import error, parse, request


BASE_WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"

def _get_api_key():
    """ 
    Fetch the API key from the configuration (key.ini) file.
    """
    config = ConfigParser()
    config.read("key.ini")
    return config["openweather"]["api_key"]

def get_user_args():
    """Handles the CLI user interactions.

    Returns:
        argparse.Namespace: Populated namespace object
    """
    parser = argparse.ArgumentParser(
        description="gets weather and temperature information for a city"
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

def weather_query(city_input, imperial=False):
    """Builds the URL for an API request to OpenWeather's weather API.

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

def get_weather_data(query_url):
    """Makes an API request to a URL and returns the data as a Python object.

    Args:
        query_url (str): URL formatted for OpenWeather's city name endpoint

    Returns:
        dict: Weather information for a specific city
    """
    response = request.urlopen(query_url)
    data = response.read()
    return json.loads(data)

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
        
    return json.loads(data)



if __name__ == "__main__":
    user_args = get_user_args()
    query_url = weather_query(user_args.city, user_args.imperial)
    weather_data = get_weather_data(query_url)
    print(weather_data)



# city = input('Enter city name: ')

# url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'

# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     temp = data['main']['temp']
#     feels = data ['main']['feels_like']
#     desc = data['weather']['description']
#     min_temp = data['main']['temp_min']
#     max_temp = data['main']['temp_max']
#     pres = data['main']['pressure']
#     moisture = data['main']['humidity']
    
#     print(f'The temperature is {temp}°C and it feels like {feels}°C.')
#     print(f'The weather is {desc} with minimum  temperature of {min_temp}°C and maximum of {max_temp}.°C')
#     print(f'The humidity is {moisture}.')
# else:
#     print('Error fetching weather data')
    


    



