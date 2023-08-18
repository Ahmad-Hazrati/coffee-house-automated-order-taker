import requests
from current_weather import display_current_weather_info
from forecast_weather import display_forecast_weather_info
import weather_history
import weather_history_class

from simple_term_menu import TerminalMenu
from datetime import datetime
from time import sleep
from os import system
import sys
from art import *
import creds
# import threading
# import constants
 

options = ["Current Weather", "Forecast Weather", "Weather History", "Exit"]
main_menu = TerminalMenu(options, title="Select your option")

sub_options = ["Main Menu", "Quit"]
sub_menu = TerminalMenu(sub_options, title="Please select to go to Main Page or Exit")

    

if __name__ == "__main__":
    tprint("WEATHER\nFORECASTING\n")
    sleep(1)
    print("----------------------------------------------------------------------")
    print("You can check the current and forecast weather of your choice city.")
    print("You can also check the weather history of European Countries' capital")
    print("for the current year.")
    print("----------------------------------------------------------------------\n\n")
    sleep(1)



    def user_sub_selection():
        choice = sub_menu.show()
        if sub_options[choice] == "Main Menu":
            system('clear')
            tprint("WEATHER\nFORECASTING\n\n")
            user_selection()
        elif sub_options[choice] == "Quit":
            sys.exit(0)
        return


    def user_selection():
        """
        Display user with choices to select and then run the relevant functions.
        """
        while True:
            choice = main_menu.show()
            if choice == None:
                choice = -1
            elif options[choice] == "Current Weather":
                system('clear')
                location = input("Enter the city name: ")
                complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+creds.user_api
                api_link = requests.get(complete_api_link, timeout=5)
                api_data = api_link.json()
                display_current_weather_info(api_data, location)
                sleep(2)
                print("\n\n")
                user_sub_selection()
            elif options[choice] == "Forecast Weather":
                system('clear')
                location = input("Enter the city name: ")
                complete_api_link = "https://api.openweathermap.org/data/2.5/forecast?q="+location+"&appid="+creds.user_api
                api_link = requests.get(complete_api_link, timeout=5)
                api_data = api_link.json()
                display_forecast_weather_info(api_data, location)
                sleep(2)
                print("\n\n")
                user_sub_selection()
            elif options[choice] == "Weather History":
                system('clear')
                PastWeather.print_weather_to_console()
                sleep(2)
                print("\n\n")
                user_sub_selection()
                        
            else:
                choice = -1
            return

user_selection()



    
    
        
        



        

