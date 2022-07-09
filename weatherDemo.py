import requests
import json
from pprint import pprint

API_KEY = "bd9baf5dfdc99b4f37ccd60e69f3f789"

#LOCATION_API_URL = "http://api.openweathermap.org/geo/1.0/direct?q={city name},{country code}&appid={API key}"
#country = input("Enter a country: ")

city = input("Enter a city: ")
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather?units=metric&appid="+API_KEY+"&q="+city

weather_report = requests.get(WEATHER_API_URL).json()
main_weather = weather_report['main']

for key in main_weather:
    print(key, ":", main_weather[key])