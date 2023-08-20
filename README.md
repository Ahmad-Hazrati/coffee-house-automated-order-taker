# Weather Forecasting

Weather Forecasting is a command line application that allows the user to check current and next 5 days weather forecasts of any location/ city directly from the terminal. The app can also compare the weather condition of 2 different locations / cities and show the result to the user.

This application is showcasing Python coding for Project Portfolio 3 and can be accessed by this [link.](https://weather-past-or-forecast.herokuapp.com/)

![Responsive Mockup Screenshot](views/README_files/mockup.png)

## Contents
<a name="contents"></a>

- [UX](#ux)
  - [Strategy](#strategy)
    - [User Stories](#user-stories)
  - [Scope](#scope)
    - [Essential Content](#essential-content)
    - [Optional Content](#optional-content)
  - [Structure](#structure)
  - [Skeleton](#structure)
    - [Wireframes](#wireframes)
  - [Surface(Design)](#surface-design)
    - [Imagery](#imagery)
    - [Typography](#typography)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
- [Testing](#testing)
  - [Development Testing](#development-testing)
  - [Testing User Stories](#testing-user-stories)
     - [User Goals](#user-goals)
     - [Site Administrator Goals](#site-administrator-goals)
  - [Validator Testing](#validator-testing)
  - [Bugs / Issues](#bugs--issues)
  - [Unresolved Bugs / Issues](#unresolved-bugs-or-issues)
- [Deployment](#deployment)
  - [Deploying to Heroku](#deploying-to-heroku)
  - [Making a Local Clone](#making-a-local-clone)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)

## UX
### Strategy
The objective of the site is to allow users to check the current and next 5 days weather condition for any geographic location. The user is also able to compare the weather condition of 2 different geographical locations / cities and see the result of comparison made based on the weather conditions. 
#### User Stories
- User Goals:
  - To check the current weather of a location / city.
  - To check the next 5 days weather forecast for any geographical location/ city. 
  - To see the weather condition comparison result of 2 different locations/ cities.
<br><br>
- Site Administrator Goals:
  - To give users the options to check current weather, weather forecasts and weather comparison result of 2 different locations / cities from the terminal.
  - To give users the ability to navigate through options back and forth easily.
  - To present data in more user friendly format as possible within the constraints of the terminal.
  - To create an application using Python with clean, resuable and commented code, utilising different functions and libraries. 
  - To handle any potential errors appropriately and consistently.
  - To keep security sensitive information hidden.

### Scope
#### Essential Content
 - The app will allow users to enter a location / city name and get the current weather information with a user friendly format.
 - The app will allow users to enter a location / city name and get the next 5 days weather information with a user friendly format.
  - The app will allow users to enter 2 different locations / cities and get the compared weather information result. 
#### Optional Content
- The app contains an introductory page containing app title, purpose and menu options.
### Structure
- The structure of the app was defined and mapped out on a [Flowchart](views/README_files/). This helped define the required interactions to develop a usuable app.
- The structure of the weather data fetching in to the app is done through API link. 
### Skeleton
#### Wireframes
- The project wireframe can be found [here.](views/README_files/wireframe.png)
### Surface (Design)
#### Imagery
- The emojis are used as weather symbol to describe the weather condition and are taken from [Pilliapp](https://www.piliapp.com/emoji/list/weather/).
![Weather Symbol](views/README_files/emojis.png)
#### Typography
- The python art library is used to for the Titles style.<br><br>
<a href="#contents">BACK TO CONTENTS 🔼</a>

## Features 

### Existing Features

- __Starting App__ 
  - When the app loads, a text art title appears followed by by 2 line text describing the purpose of the app. Subsequently main menu options appear to provide the user four options.
  - Each step is displayed with a delay of one second to add value to the user experience.
  ![App Start](views/README_files/app_start.png)<br><br>
- __Current Weather__ 
  - The current weather section starts with prompting the user to enter the name of a location / city and ends with displaying the result and sub menu options.
  - The user input is validated to be only alphabet / letters.
  ![Current Weather](views/README_files/current_weather.png)
 <br><br>
- __Forecast Weather__ 
  - The forecast weather section starts with prompting the user to enter the name of a location / city and ends with displaying the result and sub menu options.
  - The 5 days forecast weather will display with delay of 2 seconds to give the user the chance to glance over the data.
  - The user input is validated to be only alphabet / letters.
  ![Forecast Weather](views/README_files/forecast_weather.png)
 <br><br>
- __Weather Comparison__ 
  - The weather comparison section starts with prompting the user to enter the names of 2 different location / cities and ends with displaying the weather comparison result based on weather condition and sub menu options.
  - The user inputs are validated to be only alphabet / letters.
  ![Weather Comparison](views/README_files/weather_comparison.png.png)
 <br><br>
 
- __Menu Options__ 
  - The menu options provide the users with the ability to go to the main app page or quit the app.
  _ The up and down selection option give the user more convenient way to select the exact option and eliminates the incorrect input by the user.
  - There also appears an options menu beneath where the user can select to change their name, change their feedback, confirm they are happy with the feedback or delete it altogher.
  ![feedback-table-and-options](views/README_files/menu_options.png)<br><br>

### Features Left to Implement
- Initially, the idea was to present the historical weather data of European countries' capital based on the user date choice. But due to limitation of OpenWeathers API daily data request and time couldn't implemented.
<br><br>
<a href="#contents">BACK TO CONTENTS 🔼</a>

## Technologies Used

### Languages Used
- **Python**: used extensively during project.
- **Markdown**: Used exclusively for README.

### Frameworks, Libraries & Programs Used
- **simple-term-menu**: used to create the app menu options.
- **art**: used to give font style to the app titles.
- **requests**: used to request data through API from OpenWeatherMap.
- **datetime**: from the standard library, used to perform operations on date and time objects and strings.
- **time**: from the standard library used to access sleep method for pauses during pertinent points of relaying information to the user.
- **os**: from the standard library used to access system method to clear terminal screen at appropriate points whilst the program is running.
- **sys**: from the standard library used to access system method to quit the program.
- **system**: from the standard library used to clear the app screen before loading the new data.
- **Code Institute PEP8 Linter**: used to perform check of Python code.
- **Open Weather API** used to access weather forecast data for given location / city.A one call subscription was made for this service which enables 1000 calls per day free before entering the payment tier.
- **Wireframe** is used to sketch the app contents.
- **Visual Studio Code** IDE used to develop the project.
- **Git** used for version control.
- **GitHub** as cloud repository for Git version control.

<br><a href="#contents">BACK TO CONTENTS 🔼</a>

## Testing 
### Development Testing

- __Starting Options__
  - The app started successfully using the Run Program button with the title formated with art library and font "cybermedium" and with 2 lines text describing the app's purpose. Subsequently followed by the main menu options.
  - Select "Current Weather" or "Forecast Weather", or "Weather Comparison" or "Exit§ option to direct to the relevant section.
    <br><br>
- __Current Weather__
  - The current weather page loaded successfully prompting the user for input. 
  - When the input is correct, the current weather is displayed. 
  - The sub-menu option is presented afterwards with each one working satisfactorily. 
  - Various errors were purposefully entered into the terminal to check the app response as detailed below:
  - *Non-alphabet / letter entry*: a variety of non-letter entries were made with the expected response detailed below: ![Invalid Input](views/README_files/invalid_input.png).
    A while loop is run to reprompt the user until enters the valid input.
   <br><br>
- __Forecast Weather__
  - - The forecast weather page loaded successfully prompting the user for input. 
  - When the input is correct, the forecast weather is displayed. 
  - The sub-menu option is presented afterwards with each one working satisfactorily. 
  - Various errors were purposefully entered into the terminal to check the app response as detailed below:
  - *Non-alphabet / letter entry*: a variety of non-letter entries were made with the expected response detailed below: ![Invalid Input](views/README_files/invalid_input.png).
    A while loop is run to reprompt the user until enters the valid input.
   <br><br>
- __Weather Comparison__
   - The weather comparison page loaded successfully prompting the user for inputs. 
  - When the inputs are correct, the weather information is displayed with the result of compared weather conditions. 
  - The sub-menu option is presented afterwards with each one working satisfactorily. 
  - Various errors were purposefully entered into the terminal to check the app response as detailed below:
  - *Non-alphabet / letter entry*: a variety of non-letter entries were made with the expected response detailed below: ![Invalid Input](views/README_files/invalid_input.png).
    A while loop is run to reprompt the user until enters the valid input.
   <br><br>
- __User Options__
  - The two User Options formats - main menu and and sub-menu - were both presented at the appropriate time: current weather, forecast weather, and weather comparison respectively.
  - Each option was selected to confirm direction to the appropriate part of the app.

### Testing User Stories
#### User Goals
- **To check the current weather of a location / city.**
  - The app prompts the user to enter the name of any geographical location / city to display the current weather condition. 
  - The app then presents the data back to the user, fulfilling the requirements of this user goal.

- **To check the next 5 days weather forecast for any geographical location/ city.**

  - The user is prompted to enter the name of any geographical location / city to display the forecast weather for next 5 days. 
  - The user is then presented with the 5 days forecasts weather, achieving the objective of this goal.

- **To see the weather condition comparison result of 2 different locations/ cities.**

  - The user is prompted to enter the names of any geographical locations / cities to display the weather condition with a compared weather condition result. 
  - The user is then presented with the output, fulfilling this goal.

#### Site Administrator Goals
  - **To give users the options to check current weather, weather forecasts and weather comparison result of 2 different locations / cities from the terminal.**

    - The user can access current weather, forecast weather and weather comparison result data via via Open Weather API.

  - **To give users the ability to navigate through options back and forth easily.**

    - The menu and sub-menu options allows the user to go back and forth and experience different sections of the app.

  - **To present data in more user friendly format as possible within the constraints of the terminal.**

    - The font format, menu options, display data with a break of 1-2 seconds and validating the user inputs are some of the measures in this regard.

    - **To create an application using Python with clean, resuable and commented code, utilising different functions and libraries.**

    - code has been broken into discrete files to try and group together code in an ordered manner that seeks to follow the flow of the program.
    - The code has been broken into discrete files to try and group together code in an ordered manner that seeks to follow the flow of the program.
    - The functions have been written in a way such that they are atomic and perform discrete operations. The fun.py file has many examples of function calls in order to create the end result.
    - Code is commented throughout to provide future proofing and all functions are annotated with a docstring.

  - **To handle any potential errors appropriately and consistently.**

    - Throughout the app there are multiple points where error handling is required. This is achieved through try/except in most cases along with if/else statements. 

  - **To keep security sensitive information hidden.**

    - The Open Weather API key is stored as an environment variable in Heroku project config vars and testing API key added to gitignore file.

### Validator Testing 

- Python
  - Each Python file was passed through the Code Institute Linter. The initial results are detailed [here.](views/README-files/linter-results.pdf) After refactoring, the code was passed through the linter again and the results are shown below.
    - The classes.py file was passed through the linter with no warnings or errors returned.
  ![Classes File PEP8 Results](views/README-files/classes-file-pep8-results.png)<br><br> 
     - The constants.py file was passed through the linter with no warnings or errors returned.
  ![Constants File PEP8 Results](views/README-files/constants-file-pep8-results.png)<br><br> 
    - The functions.py file was passed through the linter with no warnings or errors returned.
  ![Functions File PEP8 Results](views/README-files/functions-file-pep8-results.png)<br><br> 
    - The past_weather.py file was passed through the linter with no warnings or errors returned.
  ![Past Weather File PEP8 Results](views/README-files/pastweather-file-PEP8-results.png)<br><br> 
    - The run.py file was passed through the linter with no warnings or errors returned.
  ![Run File PEP8 Results](views/README-files/run-file-PEP8-results.png)<br><br>  
    - The weather_forecast.py file was passed through the linter with no warnings or errors returned.
  ![Weather Forecast PEP8 Results](views/README-files/weatherforecast-file-PEP8-results.png)<br><br> 
 
<a href="#contents">BACK TO CONTENTS 🔼</a>

### Bugs / Issues

<table  width = 100% cellspacing="0" cellpadding="0">
   <tr>
   <th>Issue/Bug</th>
   <th>Solution</th>
   </tr>
   <tr>
   <td>Issue with simple-terminal-menu library not being supported by WINDOWS.</td>
   <td>Ubantu as virtual machine is installed and used as platform to run the VS Code on and then clone the repository to it.</td>
   </tr>
   <tr>
   <td>Issue with importing the API key.</td>
   <td>Windows environment variable and the function "os.getenv" is used to solve the issue.</td>
   </tr>
   <tr>
   <td>Issue with incorrect user input.</td>
   <td>Add get_user_input function with the use of try and except solve the issue.</td>
   </tr>
   <tr>
   <td> Tried to deploy to Heroku app but got failed due to requirements.txt file has been populated with template meta data.</td>
   <td>Regenerate the requirements.txt and then run the deployment and the issue is solved.</td>
   </tr>
   <tr>
   <td>Issue to get the weather condition for next 5 days.</td>
   <td>Run the for loop for date list and solve the issue.</td>
   </tr>
  </table>

### Unresolved Bugs or Issues
- 
 <br><br>
<a href="#contents">BACK TO CONTENTS 🔼</a>

## Deployment

### Deploying to Heroku
* This site was deployed by completing the following steps:

1. Log in to [Heroku](https://id.heroku.com) or create an account.
2. On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New App.
3. You must enter a unique app name.
4. Next select your region.
5. Click on the Create App button
6. The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars.
7. Click Reveal Config Vars and enter the following:
    - Add "PORT" into the Key box and 8000 into the Value box and click the Add button.
    - Enter "API_KEY" into the next available Key box and the API_KEY value into the corresponding Value box.
    - Enter API_KEY into the next available Key box and the Open Weather API key into the corresponding Value box.
8. Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes.
9. Repeat step 8 to add node.js. o Note: The Buildpacks must be in the correct order. If not click and drag them to move into the correct order.
10. Scroll to the top of the page and choose the Deploy tab.
11. Select Github as the deployment method.
12. Confirm you want to connect to GitHub.
13. Search for the repository name and click the connect button.
14. Scroll to the bottom of the deploy page and select the preferred deployment type.
15. Click either Enable Automatic Deploys for automatic deployment when you push updates to Github.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository.](https://github.com/Ahmad-Hazrati/weather-forecasting)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```
<br><br>
<a href="#contents">BACK TO CONTENTS 🔼</a>

## Credits 
### Content 
NOTE: Specific links are included within the Python files. The list below summarises content credits in general.
- Thanks to my Code Institute mentor Mr. Aleksei Konovalov for his guidance, insight and the constant confidence boost to help me in the right direction.
- Code Institute Tutor Assistance, Slack, other online resources and especially the Github of [Johnamdickson](https://github.com/johnamdickson/portfolio-project-3/)
 were a massive help for Python that enabled some of the functionality I was looking for.
- Weather codes and corresponding weather conditions from [Open Weather.](https://openweathermap.org/weather-conditions)
- Deployment information to Heroku is taken from Code Institute [Love Sandwiches - Essentials Project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/e3b664e16366444c8d722c5d8340b340/) and respective guidelines.

### Media
- The emojis are used as weather symbol to describe the weather condition and are taken from [Pilliapp](https://www.piliapp.com/emoji/list/weather/).
- The python art library is used to for the Titles style.
- The simple-terminal-menu is used to create the menu and sub-menu options in the app.
<br><br>
<a href="#contents">BACK TO CONTENTS 🔼</a>

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---
