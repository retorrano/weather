import requests
import sqlite3
from settings import get_settings

def get_weather_data():
    # Retrieve settings from the database
    settings = get_settings()
    latitude = settings['latitude']
    longitude = settings['longitude']
    api_key = settings['api']

    # Construct the URL for the WeatherAPI
    url = f"https://api.weatherapi.com/v1/current.json?q={latitude},{longitude}&key={api_key}"

    # Make the API request
    response = requests.get(url)
    data = response.json()

    return data

def get_temperature():
    data = get_weather_data()
    return data['current']['temp_c']

def get_relative_humidity():
    data = get_weather_data()
    return data['current']['humidity']

def get_heat_index():
    data = get_weather_data()
    return data['current']['heatindex_c']

def get_wind_direction():
    data = get_weather_data()
    return data['current']['wind_dir']

def get_wind_speed():
    data = get_weather_data()
    return data['current']['wind_kph']

def get_wind_gust():
    data = get_weather_data()
    return data['current']['gust_kph']

def get_rain_gauge():
    data = get_weather_data()
    return data['current']['precip_mm']

def get_last_updated():
    data = get_weather_data()
    return data['current']['last_updated']
