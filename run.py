import requests
from configparser import ConfigParser
import argparse

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

# ...

if __name__ == "__main__":
    user_args = get_user_args()
    print(user_args.city, user_args.imperial)



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
    


    



