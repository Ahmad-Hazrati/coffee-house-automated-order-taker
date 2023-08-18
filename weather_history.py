import gspread
from google.oauth2.service_account import Credentials
from os import system
from tabulate import tabulate
import datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('weather_history')

kiel = SHEET.worksheet('kiel')


def calculate_date_range():
    """
    Calculate date range in worksheet to display to user before making their entry.
    """
    earliest_date = kiel.cell(2, 1).value
    row_count = len(kiel.get_all_values())
    latest_date = kiel.cell(row_count, 1).value
    return [earliest_date, latest_date]
    
print(calculate_date_range())



def find_historical_data_row(date, date_range):
    """
    Find row in weather_history spreadsheet and return data from row as list.
    """
    try:
        cell = kiel.find(date, in_column=1)
        weather_data = kiel.row_values(cell.row)
        return True, weather_data
    except AttributeError:
        error_message = (f"The date you selected is not available. "
                         f"You entered {date}\nDate should be between {date_range[0]}"
                         f"and {date_range[1]}.\n")
        return False, error_message
    
print(find_historical_data_row("2023-02-01","2023-08-31"))

def get_date(sheet_dates):
    """
    Request date from user to locate historical weather data.
    """
    system ("clear")
    while True:
        earliest_date = (sheet_dates[0])
        latest_date = (sheet_dates[1])
        print(f"Please enter the date to check the historical weather data\n")
        print(f"Available dates between {earliest_date} and {latest_date}. \n")
        print("The date format should be: YYYY-MM-DD e.g 2023-04-20\n")
        date = input("Enter your date below:\n")
        if validate_date(date):
            # Clear console for loading screen and break from
            # While loop to return date.
            system('clear')
            break
    return date


def validate_date(date):
    """Inside the try, creates a date object using datetime class strptime
    method. Raises ValueError if date does not conform to date format.
    """
    # The following tutorial was used to determine the correct date format.
    # https://www.tutorialspoint.com/How-to-do-date-validation-in-Python

    # giving the date format
    date_format = '%Y-%m-%d'

    # using try-except blocks for handling the exceptions
    try:
        # formatting the date using strptime() function
        datetime.datetime.strptime(date, date_format)
        return True

    # If the date validation goes wrong
    except ValueError:
        # printing the appropriate text if ValueError occurs
        print(f"Incorrect data format, you entered '{date}' "
                              "\nDate should be in the format YYYY-MM-DD "
                              "e.g. 2023-04-20\n", 3)
        return False
    else:
        return True
    