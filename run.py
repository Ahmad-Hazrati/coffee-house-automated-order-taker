# Import functions from other python files
from current_weather import display_current_weather_info
from forecast_weather import display_forecast_weather_info
from weather_comparison import display_weather_info_location_one
from weather_comparison import display_weather_info_location_two
# Import api_key

# Import libraries
import sys
import requests
from urllib import error, parse, request
import json
from simple_term_menu import TerminalMenu
from time import sleep
from os import system
import os
from art import *

# code taken from https://github.com/johnamdickson/portfolio-project-3
API_KEY = os.getenv('API_KEY')


def get_user_input():
    """
    Get city name input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal. The loop will repeatedly request data, until it is valid.
    """
    while True:
        try:
            location = input("Enter the city name: \n")
            if location.isalpha():
                break
        except ValueError:
            pass
        print("Please enter letters only. \n")
    return location

def get_weather_data(query_url):
    """
    Makes an API request to a URL and returns the data as a Python object.
    """
    while True:
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
sub_menu = TerminalMenu(sub_options,
                        title="Please select to go to Main Page or Exit")


def user_selection():
    """
    Display user with choices to select and then run the relevant functions.
    """
    while True:
        choice = main_menu.show()
        if choice is None:
            choice = -1
        elif options[choice] == "Current Weather":
            system('clear')
            location = get_user_input()
            complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+str(API_KEY)
            api_link = requests.get(complete_api_link, timeout=5)
            api_data = api_link.json()
            #get_weather_data()
            display_current_weather_info(api_data, location)
            sleep(1)
            print("\n\n")
            user_sub_selection()
        elif options[choice] == "Forecast Weather":
            system('clear')
            location = get_user_input()
            complete_api_link = "https://api.openweathermap.org/data/2.5/forecast?q="+location+"&appid="+str(API_KEY)
            api_link = requests.get(complete_api_link, timeout=5)
            api_data = api_link.json()
            display_forecast_weather_info(api_data, location)
            sleep(1)
            print("\n\n")
            user_sub_selection()
        elif options[choice] == "Weather Comparison":
            system('clear')
            location_one = get_user_input()
            location_two = get_user_input()
            complete_api_link_location_one = "https://api.openweathermap.org/data/2.5/weather?q="+location_one+"&appid="+str(API_KEY)
            complete_api_link_location_two = "https://api.openweathermap.org/data/2.5/weather?q="+location_two+"&appid="+str(API_KEY)
            api_link_one = requests.get(complete_api_link_location_one)
            api_link_two = requests.get(complete_api_link_location_two)
            data = api_link_one.json()
            api_d = api_link_two.json()
            display_weather_info_location_one(data, location_one)
            sleep(1)
            display_weather_info_location_two(api_d, location_two)
            sleep(1)

            def weather_comparison(location_one, location_two):
                """
                Compare the weather of 2 different cities and print the output.
                """
                if data["weather"][0]["main"] == api_d["weather"][0]["main"]:
                    print(f"The weather of {location_one} "
                          f"and {location_two} are same.")
                    print(f"The weather condition of both "
                          "cities are", data['weath'
                                                     'er'][0]['description'])
                    print("-----------------------------------"
                          "-----------------------------")
                else:
                    if data["weather"][0]["mai""n"] == "Clear" and api_d["weather"][0]["main"] != "Clear":
                        print(f"The weather of {location_one} is better than the weather of {location_two}.")
                        print(f"The weather condition is", data['weather'][0]['description'])
                        print("----------------------------------------------------------------")
                    elif data["weather"][0]["main"] == "Clouds" and api_d["weather"][0]["main"] != "Clouds" or "Clear":
                        print(f"The weather of {location_one} is better than the weather of {location_two}.")
                        print(f"The weather condition is", data['weather'][0]['description'])
                        print("--------------------------"
                              "--------------------------------------")
                    elif data["weather"][0]["main"] == "Rain" and api_d["weather"][0]["main"] != "Rain" or "Clouds" or "Clear":
                        print(f"The weather of {location_one} is better than the weather of {location_two}.")
                        print(f"The weather condition is", data['weather'][0]['description'])
                        print("--------------------------"
                              "--------------------------------------")
                    elif data["weather"][0]["main"] == "Drizzle" and api_d["weather"][0]["main"] != "Drizzle" or "Rain" or "Clouds" or "Clear":
                        print(f"The weather of {location_one} is better than the weather of {location_two}.")
                        print(f"The weather condition is", data['weather'][0]['description'])
                        print("---------------------------"
                              "-------------------------------------")
                    elif data["weather"][0]["main"] == "Snow" and api_d["weather"][0]["main"] != "Snow" or "Drizzle" or "Rain" or "Clouds" or "Clear":
                        print(f"The weather of {location_one} is better than the weather of {location_two}.")
                        print(f"The weather condition is", data['weather'][0]['description'])
                        print("-----------------------------"
                              "-----------------------------------")
                    elif data["weather"][0]["main"] == "Thunderstorm" and api_d["weather"][0]["main"] != "Thunderstorm" or "Snow" or "Drizzle" or "Rain" or "Clouds" or "Clear":
                        print(f"The weather of {location_one} is better than "
                              "the weather of {location_two}.")
                        print(f"The weather is conditio"
                              f"n", data['weather'][0]['description'])
                        print("-----------------------------"
                              "-----------------------------------")
                    else:
                        print(f"The weather of {location_two} is better than "
                              f"the weather of {location_one}.")
                        print(f"The weather condition "
                              "is", api_d['weather'][0]['description'])
                        print("-------------------------------------"
                              "---------------------------")
            weather_comparison(location_one, location_two)
            sleep(1)
            print("\n\n")
            user_sub_selection()
        else:
            choice = -1
        return


if __name__ == "__main__":
    tprint("WEATHER\nFORECASTING\n", font="cybermedium")
    sleep(1)
    print("----------------------------------------------"
          "---------------------")
    print("You can check the current "
          "and forecast weather of your choice city.")
    print("You can also compare the current weather of 2 locations.")
    print("-----------------------------------------------"
          "--------------------\n\n")
    sleep(1)
    user_selection()
