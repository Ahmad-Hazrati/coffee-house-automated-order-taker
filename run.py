
from current_weather import display_current_weather_info
from forecast_weather import display_forecast_weather_info
from weather_comparison import display_weather_info_location_one, display_weather_info_location_two, weather_comparison
import sys
import requests
import requests
from simple_term_menu import TerminalMenu
from datetime import datetime
from time import sleep
from os import system
import sys
from art import *
import creds
 


def get_user_input():
    """
    Get city name input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal. The loop will repeatedly request data, until it is valid.
    """
    while True:
        try:
            location = input("Enter the city name: ")
            if location.isalpha():
                break
        except:
                pass
        print("Please enter letters only. \n")
    return location


def user_sub_selection():
    """
    Function to display sub menu to the user.
    """
    choice = sub_menu.show()
    if sub_options[choice] == "Main Menu":
        system('clear')
        tprint("WEATHER\nFORECASTING\n\n")
        user_selection()
    elif sub_options[choice] == "Quit":
        sys.exit(0)
    return

options = ["Current Weather", "Forecast Weather", "Weather Comparison", "Exit"]
main_menu = TerminalMenu(options, title="Select your option")

sub_options = ["Main Menu", "Quit"]
sub_menu = TerminalMenu(sub_options, title="Please select to go to Main Page or Exit")

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
            location= get_user_input()
            #location = input("Enter the city name: ")                     
            complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+creds.user_api
            api_link = requests.get(complete_api_link, timeout=5)
            api_data = api_link.json()
            display_current_weather_info(api_data, location)
            sleep(2)
            print("\n\n")
            user_sub_selection()
        elif options[choice] == "Forecast Weather":
            system('clear')
            location = get_user_input()
            #location = input("Enter the city name: ")
            complete_api_link = "https://api.openweathermap.org/data/2.5/forecast?q="+location+"&appid="+creds.user_api
            api_link = requests.get(complete_api_link, timeout=5)
            api_data = api_link.json()
            display_forecast_weather_info(api_data, location)
            sleep(2)
            print("\n\n")
            user_sub_selection()
        elif options[choice] == "Weather Comparison":
            system('clear')
            location_one = get_user_input()
            location_two = get_user_input()
            #location1 = input("Enter the 1st city name: ")
            #location2 = input("Enter the 2nd city name: ")
            complete_api_link_location_one = "https://api.openweathermap.org/data/2.5/weather?q="+location_one+"&appid="+creds.user_api
            complete_api_link_location_two = "https://api.openweathermap.org/data/2.5/weather?q="+location_two+"&appid="+creds.user_api
            api_link_one = requests.get(complete_api_link_location_one)
            api_link_two = requests.get(complete_api_link_location_two)
            print(weather_comparison(location_one, location_two))

            api_data_one = api_link_one.json()
            api_data_two = api_link_two.json()
            display_weather_info_location_one(api_data_one, location_one)
            display_weather_info_location_two(api_data_two, location_two)
            sleep(2)
            print("\n\n")
            user_sub_selection()
        else:
            choice = -1
        return


    

if __name__ == "__main__":
    tprint("WEATHER\nFORECASTING\n", font="cybermedium")
    sleep(1)
    print("-------------------------------------------------------------------")
    print("You can check the current and forecast weather of your choice city.")
    print("You can also compare the current weather of 2 locations.")
    print("-------------------------------------------------------------------\n\n")
    sleep(2)
    user_selection()



    





    
    
        
        



        

