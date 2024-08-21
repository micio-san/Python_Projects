from dotenv import load_dotenv
import requests
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print("\n__________ Get current weather conditions in __________")
    city = input("\n____ Please enter a city name _____\n")
    if city=="" or city.isnumeric():
        print("\n____ Please enter a valid name _____\n")
        get_current_weather()
    else:
        request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
        print(request_url)
        weather_data= requests.get(request_url).json()
        if "message" in weather_data.keys():
            print("thee", weather_data.message)
        pprint(weather_data)

if __name__=="__main__":
   get_current_weather()