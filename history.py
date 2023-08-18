
import requests
import sys

import json
                
#Request for user inputs
#location = input("Enter the city name: ")


response = requests.request("GET", "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/kiel/2023-02-01/2023-08-31?unitGroup=metric&elements=datetime%2CdatetimeEpoch%2Ctempmax%2Ctempmin%2Ctemp%2Cfeelslike%2Chumidity%2Csnow%2Cwindspeed%2Cconditions&include=days&key=PSYBMZRXYTXYUQ7L7WCC7LKYC&contentType=json")
if response.status_code!=200:
  print('Unexpected Status code: ', response.status_code)
  sys.exit()  


# Parse the results as JSON
api_data = response.json()
               


# Create variables to store and display data
def display_past_weather_info(api_data):
    """
    Prints formatted weather information about a city for past 6 months.
    """
    temp_city = (api_data["days"])
    print ("Temperature was         : {:.2f} deg C".format(temp_city))
    # loops = 0
    # for el in api_data["days"]:
    #     if loops >= 40:
    #         break
    #     date = (el["days"]["datetime"])
    #     temp_city = (el["days"]["temp"])
    #     feels_like = (el["days"]["feelslike"])
    #     max_temp = (el["days"]["tempmax"])
    #     min_temp = (el["days"]["tempmin"])
    #     weather_desc = el["days"]["condition"]
    #     humidity = el["days"]['humidity']
    #     wind_spd = el["days"]["windspeed"]
    #     print ("----------------------------------------------------------------")
    #     print ("Weather Status for - {}  ".format(date))
    #     print ("----------------------------------------------------------------")
    #     # Assign the the weather_display function to the weather_symbol variable
    #     print ("Temperature was         : {:.2f} deg C".format(temp_city))
    #     print ("It was felt like        : {:.2f} deg C".format(feels_like))
    #     print ("Maximum temperature was : {:.2f} deg C".format(temp_city))
    #     print ("Minimum temperature was : {:.2f} deg C".format(feels_like))
    #     print ("Weather condition was   :",weather_desc)
    #     print ("Humidity was            :",humidity, '%')
    #     print ("And Wind speed was      :",wind_spd ,'kmph\n\n')
    #     loops += 1 

weather_info = display_past_weather_info(api_data)
