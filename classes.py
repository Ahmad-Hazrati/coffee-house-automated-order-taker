import weather_history
import datetime
from time import sleep
from os import system




class PastWeather:
    """
    Class for historical weather data and associated methods
    """
    def __init__(self, weather_data, date):
        self.weather_data = weather_data
        self.date = date
        
    def parse_data(self):
        """
        Select the required data from weather historical data spreadsheet 
        and returns a string detailing all information.
        """
        data = self.weather_data
        max_temp =  (data[1] + "°C")
        min_temp =  (data[2] + "°C")
        temp =  (data[3] + "°C")
        feels_like = (data[4] + "°C")
        humidity = (data[5] + "%")
        snow = (data[6])
        windspeed = (data[7] + "km/h")
        condition = (data[8])
        date_format = datetime.now().strftime("%Y-%m-%d")
        date = day.datetime.strptime(self.date, date_format)
        day = (date.strftime('%A'))
         
        return {'day': day, 'max_temp': max_temp, 'min_temp': min_temp,
                'temp': temp, 'feels_like': feels_like, 'humidity': humidity,
                'snow': snow, 'windspeed': windspeed, 'condition':condition}
        
        
    def print_weather_to_console(self, data):
        """
        Print past weather to the console using data from 'data' dictionary.
        """ 
        system("clear")
        print(f"{self.date} was a {data['day']}")
        sleep(1)
        print("On that day at Kiel the maximum temperature was "
              f"{data['max_temp']} and the \n minimum temperature was "
              f"{data['min_temp']}.")
        sleep(1)
        print(f"The temperature was {data['temp']} and it feels like {data['feels_like']}.")
        sleep(1)
        print(f"The humidity was {data['humidity']} and the wind speed was {data['windspeed']}.")
        sleep(1)
        print(f"The weather condition was {data['condition']}.")
        sleep(1)
        return
        
print(PastWeatheras())
        
        
