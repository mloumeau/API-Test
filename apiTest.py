import requests
from datetime import datetime
import time #For timezone

apiID = "b702a4286daab5d7af2a7409d0a68275"

#Kelvin to Farenheit
def KtoF(temp):
    return str(round((temp - 273.15) * 9/5 + 32, 2)) #Convert to string to be able to concat with print statements

while True:   #Have this run as long as the user wants
    try:
        city = input("\nChoose location:\nCity   or   City,ct  or   City,st,ct\n").lower().capitalize()   #The API needs first letter capital, the rest lower
        response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + apiID)
        weather_JSON = response.json()
        weather_JSON['name']   #Checking to see if the city worked in the API

    except KeyError:  #KeyError will be the error code for a wrongly inputted location

        print("\nThe city you requested does not exist.")
        tryAgain = input("\nTry again? (y/n)")
        if tryAgain == 'y':
            continue
        break  #No need for an else statement since it will only get here if the user doesn't want to continue

    else:
        print("\nLocation: " + weather_JSON['name'] + ", " + weather_JSON['sys']['country'],
            "Description: " + weather_JSON['weather'][0]['description'].title(), #Title capitalizes the first letter of every word
            "Current Temp in F: " + KtoF(weather_JSON['main']['temp']) + " -- High: " + KtoF(weather_JSON['main']['temp_max']) + ", Low: " + KtoF(weather_JSON['main']['temp_min']),
            "Sunrise: " + str(datetime.fromtimestamp(weather_JSON['sys']['sunrise'] + (time.timezone + (weather_JSON['timezone']))))[11:], #Convert back to epoch, then take difference
            "Sunset: " + str(datetime.fromtimestamp(weather_JSON['sys']['sunset'] + (time.timezone + (weather_JSON['timezone']))))[11:], sep="\n")

        tryAgain = input("\n\nWould you like to examine another city? (y/n)")
        if tryAgain == 'y':
            continue
        break  #No need for an else statement since it will only get here if the user doesn't want to continue
