import webbrowser
from settings import get_settings

def show_map():
    settings = get_settings()
    latitude = settings['latitude']
    longitude = settings['longitude']
    
    # Construct the Windy.com URL with the latitude and longitude
    url = f"https://www.windy.com/?{latitude},{longitude},11"
    
    # Open the URL in the default web browser
    webbrowser.open(url)
