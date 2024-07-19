import tkinter as tk
from tkinter import ttk
from tokenize import Double
from weather_lib import get_wind_direction, get_wind_speed, get_wind_gust, get_rain_gauge, get_temperature, get_relative_humidity, get_heat_index, get_last_updated
from settings import check_or_create_settings_db, get_settings
from settings_main_gui import SettingsGUI
from about import AboutGui
from readme import ReadmeGui

# Function to update weather data
def update_weather_data():
    print("Updating weather data")
    
    temperature_textfield.config(state='normal')
    heat_index_textfield.config(state='normal')
    relative_humidity_textfield.config(state='normal')
    wind_direction_textfield.config(state='normal')
    wind_speed_textfield.config(state='normal')
    wind_gust_textfield.config(state='normal')
    rain_gauge_textfield.config(state='normal')
    last_updated_textfield.config(state='normal')
    
    temperature_textfield.delete(0, tk.END)
    heat_index_textfield.delete(0, tk.END)
    relative_humidity_textfield.delete(0, tk.END)
    wind_direction_textfield.delete(0, tk.END)
    wind_speed_textfield.delete(0, tk.END)
    wind_gust_textfield.delete(0, tk.END)
    rain_gauge_textfield.delete(0, tk.END)
    last_updated_textfield.delete(0, tk.END)
    
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

    last_updated = get_last_updated()
    last_updated_textfield.insert(0, str(last_updated))
    
    temperature_textfield.config(state='readonly')
    heat_index_textfield.config(state='readonly')
    relative_humidity_textfield.config(state='readonly')
    wind_direction_textfield.config(state='readonly')
    wind_speed_textfield.config(state='readonly')
    wind_gust_textfield.config(state='readonly')
    rain_gauge_textfield.config(state='readonly')
    last_updated_textfield.config(state='readonly')

    settings = get_settings()
    ref_rate = int(settings['refresh_rate']) * 1000

    window.after(ref_rate, update_weather_data)  # Schedule the function to be called again after ref_rate seconds

def start_button_clicked():
    print("Start button clicked")
    update_weather_data()

def on_edit_settings():
    print("Settings menu item clicked")
    settings_window = tk.Toplevel(window)
    settings_gui = SettingsGUI(settings_window)

def on_help_about():
    print("About menu item clicked")
    about_gui = AboutGui(window)
    about_gui.show_info()

def on_help_readme():
    print("Readme menu item clicked")
    readme_gui = ReadmeGui(window)
    readme_gui.show_info()

# Create settings
check_or_create_settings_db()

# Create the main window
print("Creating main window")
window = tk.Tk()
window.title("Weather Data Input")
window.geometry("600x600")  # Set the window size to double

# Apply a theme
style = ttk.Style()
style.theme_use('clam')  # 'clam', 'alt', 'default', 'classic' are some of the available themes

# Customize the theme to look more like GNOME
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TButton', font=('Helvetica', 12))
style.configure('TEntry', font=('Helvetica', 12))
style.configure('TMenu', font=('Helvetica', 12))

# Create the menu bar
menu_bar = tk.Menu(window)

# Create Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Settings", command=on_edit_settings)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Create Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=on_help_about)
help_menu.add_command(label="Readme", command=on_help_readme)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Set the menu bar to the window
window.config(menu=menu_bar)

# Create the start button
print("Creating start button")
start_button = ttk.Button(window, text="Start", command=start_button_clicked)
start_button.pack(pady=10)

# Create the Temperature label and textfield
print("Creating Temperature input")
temperature_label = ttk.Label(window, text="Temperature, Degree Celsius")
temperature_label.pack(pady=5)
temperature_textfield = ttk.Entry(window)
temperature_textfield.pack(pady=5, fill='x', padx=20)

# Create the Heat Index label and textfield
print("Creating Heat Index input")
heat_index_label = ttk.Label(window, text="Heat Index, Degree Celsius")
heat_index_label.pack(pady=5)
heat_index_textfield = ttk.Entry(window)
heat_index_textfield.pack(pady=5, fill='x', padx=20)

# Create the Relative Humidity label and textfield
print("Creating Relative Humidity input")
relative_humidity_label = ttk.Label(window, text="Relative Humidity, %")
relative_humidity_label.pack(pady=5)
relative_humidity_textfield = ttk.Entry(window)
relative_humidity_textfield.pack(pady=5, fill='x', padx=20)

# Create the Wind Direction label and textfield
print("Creating Wind Direction input")
wind_direction_label = ttk.Label(window, text="Wind Direction")
wind_direction_label.pack(pady=5)
wind_direction_textfield = ttk.Entry(window)
wind_direction_textfield.pack(pady=5, fill='x', padx=20)

# Create the Wind Speed label and textfield
print("Creating Wind Speed input")
wind_speed_label = ttk.Label(window, text="Wind Speed, kph")
wind_speed_label.pack(pady=5)
wind_speed_textfield = ttk.Entry(window)
wind_speed_textfield.pack(pady=5, fill='x', padx=20)

# Create the Wind Gust label and textfield
print("Creating Wind Gust input")
wind_gust_label = ttk.Label(window, text="Wind Gust, kph")
wind_gust_label.pack(pady=5)
wind_gust_textfield = ttk.Entry(window)
wind_gust_textfield.pack(pady=5, fill='x', padx=20)

# Create the Rain Gauge label and textfield
print("Creating Rain Gauge input")
rain_gauge_label = ttk.Label(window, text="Rain Gauge, mm")
rain_gauge_label.pack(pady=5)
rain_gauge_textfield = ttk.Entry(window)
rain_gauge_textfield.pack(pady=5, fill='x', padx=20)

# Create the Last Updated label and textfield
print("Creating Last Updated input")
last_updated_label = ttk.Label(window, text="Last Updated")
last_updated_label.pack(pady=5)
last_updated_textfield = ttk.Entry(window)
last_updated_textfield.pack(pady=5, fill='x', padx=20)

# Start the GUI event loop
print("Starting the GUI event loop")
window.mainloop()
print("GUI event loop has ended")
