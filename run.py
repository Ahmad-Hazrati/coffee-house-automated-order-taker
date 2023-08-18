from current_weather import display_current_weather_info
from forecast_weather import display_forecast_weather_info
#import weather_history
#import classes

from simple_term_menu import TerminalMenu
from datetime import datetime
from os import system
from art import *
# import threading
# import constants
 

options = ["Current Weather", "Forecast Weather", "Weather History", "Exit"]
main_menu = TerminalMenu(options, title="Select your option")

if __name__ == "__main__":
    tprint("WEATHER\nFORECASTING\n", font="cybermedum")
    print("----------------------------------------------------------------------")
    print("You can check the current and forecast weather of your choice city.")
    print("You can also check the weather history of European Countries' capital")
    print("for the current year.")
    print("----------------------------------------------------------------------\n\n")
    choice = main_menu.show()
    # print("You chose: ", choice)
    
    def user_selection(choice):
        """
        Using selection passed in from PastWeather class instance,
        select appropriate menu.
        """
        if choice == None:
            choice = -1
        if options[choice] == "Current Weather":
            system('clear')
            print(current_weather_info)
        elif options[choice] == "Forecast Weather":
            system('clear')
            print(forecast_weather_info)
        elif options[choice] == "Weather History":
            system('clear')
            print(history_weather_info)
        else:
            choice = -1
        return
    
        
        



        

