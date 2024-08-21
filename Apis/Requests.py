from dotenv import load_dotenv
import requests
import os

load_dotenv()


def get_current_weather():
    print("\n__________ Get current weather conditions in __________")
    city = input("\n____ Please enter a city name _____\n")
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    print(request_url)

get_current_weather()