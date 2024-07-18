# In weather-lib.py

def get_temperature():
    # Imagine this function fetches the temperature from a weather API
    temperature = 25.3  # Example value
    return temperature
def get_relative_humidity():
    # Imagine this function fetches the relative humidity from a weather API
    relative_humidity = 65.2  # Example value
    return relative_humidity

def get_heat_index():
    # Formula to calculate heat index
    humidity = get_relative_humidity()
    temperature = get_temperature()
    heat_index = -42.379 + 2.04901523 * temperature + 10.14333127 * humidity - 0.22475541 * temperature * humidity - 6.83783e-03 * temperature**2 - 5.481717e-02 * humidity**2 + 1.22874e-03 * temperature**2 * humidity + 8.5282e-04 * temperature * humidity**2 - 1.99e-06 * temperature**2 * humidity**2
    return heat_index

def get_wind_direction():
    # Imagine this function fetches the wind direction from a weather API
    wind_direction = "NE"  # Example value
    return wind_direction

def get_wind_speed():
    # Imagine this function fetches the wind speed from a weather API
    wind_speed = 10.5  # Example value
    return wind_speed

def get_wind_gust():
    # Imagine this function fetches the wind gust from a weather API
    wind_gust = 15.2  # Example value
    return wind_gust

def get_rain_gauge():
    # Imagine this function fetches the rain gauge measurement from a weather API
    rain_gauge = 5.7  # Example value
    return rain_gauge