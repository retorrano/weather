import tkinter as tk
from weather_lib import get_wind_direction, get_wind_speed, get_wind_gust, get_rain_gauge, get_temperature, get_relative_humidity, get_heat_index

def start_button_clicked():
    print("Start button clicked")
    temperature = get_temperature()
    temperature_textfield.insert(0, str(temperature))
    heat_index = get_heat_index()
    heat_index_textfield.insert(0, str(heat_index))
    relative_humidity = get_relative_humidity()
    relative_humidity_textfield.insert(0, str(relative_humidity))
    wind_direction = get_wind_direction()
    wind_direction_textfield.insert(0, str(wind_direction))
    wind_speed = get_wind_speed()
    wind_speed_textfield.insert(0, str(wind_speed))
    wind_gust = get_wind_gust()
    wind_gust_textfield.insert(0, str(wind_gust))
    rain_gauge = get_rain_gauge()
    rain_gauge_textfield.insert(0, str(rain_gauge))
    # Add your code here to handle the wind speed input
    # Add your code here to handle the start button click event


# Create the main window
print("Creating main window")
window = tk.Tk()
window.title("Weather Data Input")
window.geometry("600x600")  # Set the window size to double

# Create the start button
print("Creating start button")
start_button = tk.Button(window, text="Start", command=start_button_clicked)
start_button.pack(pady=10)

# Create the Temperature label and textfield
print("Creating Temperature input")
temperature_label = tk.Label(window, text="Temperature")
temperature_label.pack(pady=5)
temperature_textfield = tk.Entry(window)
temperature_textfield.pack(pady=5, fill='x', padx=20)

# Create the Heat Index label and textfield
print("Creating Heat Index input")
heat_index_label = tk.Label(window, text="Heat Index")
heat_index_label.pack(pady=5)
heat_index_textfield = tk.Entry(window)
heat_index_textfield.pack(pady=5, fill='x', padx=20)

# Create the Relative Humidity label and textfield
print("Creating Relative Humidity input")
relative_humidity_label = tk.Label(window, text="Relative Humidity")
relative_humidity_label.pack(pady=5)
relative_humidity_textfield = tk.Entry(window)
relative_humidity_textfield.pack(pady=5, fill='x', padx=20)

# Create the Wind Direction label and textfield
print("Creating Wind Direction input")
wind_direction_label = tk.Label(window, text="Wind Direction")
wind_direction_label.pack(pady=5)
wind_direction_textfield = tk.Entry(window)
wind_direction_textfield.pack(pady=5, fill='x', padx=20)

# Create the Wind Speed label and textfield
print("Creating Wind Speed input")
wind_speed_label = tk.Label(window, text="Wind Speed")
wind_speed_label.pack(pady=5)
wind_speed_textfield = tk.Entry(window)
wind_speed_textfield.pack(pady=5, fill='x', padx=20)

# Create the Wind Gust label and textfield
print("Creating Wind Gust input")
wind_gust_label = tk.Label(window, text="Wind Gust")
wind_gust_label.pack(pady=5)
wind_gust_textfield = tk.Entry(window)
wind_gust_textfield.pack(pady=5, fill='x', padx=20)

# Create the Rain Gauge label and textfield
print("Creating Rain Gauge input")
rain_gauge_label = tk.Label(window, text="Rain Gauge")
rain_gauge_label.pack(pady=5)
rain_gauge_textfield = tk.Entry(window)
rain_gauge_textfield.pack(pady=5, fill='x', padx=20)

# Start the GUI event loop
print("Starting the GUI event loop")
window.mainloop()
print("GUI event loop has ended")
