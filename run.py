import requests
from configparser import ConfigParser

def _get_api_key():
    """ 
    Fetch the API key from the configuration (key.ini) file.
    """
    config = ConfigParser()
    config.read("key.ini")
    return config["openweather"]["api_key"]


city = input('Enter city name: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    feels = data ['main']['feels_like']
    desc = data['weather'][0]['description']
    min_temp = data['main']['temp_min']
    max_temp = data['main']['temp_max']
    pres = data['main']['pressure']
    moisture = data['main']['humidity']
    
    print(f'The temperature is {temp}°C and it feels like {feels}°C.')
    print(f'The weather is {desc} with minimum  temperature of {min_temp}°C and maximum of {max_temp}.°C')
    print(f'The humidity is {moisture}.')
else:
    print('Error fetching weather data')
    


    



