import tkinter as tk
import sqlite3
from tkinter import ttk
from settings import get_settings

class SettingsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Settings")
        self.root.geometry("400x350")  # Set the window size to a larger size

        # Retrieve settings from the database
        settings = get_settings()
        
        # Latitude
        self.latitude_label = tk.Label(root, text="Latitude:")
        self.latitude_label.pack(pady=5)
        
        self.latitude_entry = tk.Entry(root)
        self.latitude_entry.pack(pady=5, fill='x', padx=20)
        self.latitude_entry.insert(0, str(settings['latitude']))
        
        # Longitude
        self.longitude_label = tk.Label(root, text="Longitude:")
        self.longitude_label.pack(pady=5)
        
        self.longitude_entry = tk.Entry(root)
        self.longitude_entry.pack(pady=5, fill='x', padx=20)
        self.longitude_entry.insert(0, str(settings['longitude']))
        
        # API
        self.api_label = tk.Label(root, text="API Key:")
        self.api_label.pack(pady=5)
        
        self.api_entry = tk.Entry(root)
        self.api_entry.pack(pady=5, fill='x', padx=20)
        self.api_entry.insert(0, str(settings['api']))
        
        # Refresh Rate
        self.refresh_rate_label = tk.Label(root, text="Refresh Rate (seconds):")
        self.refresh_rate_label.pack(pady=5)
        
        self.refresh_rate_entry = tk.Entry(root)
        self.refresh_rate_entry.pack(pady=5, fill='x', padx=20)
        self.refresh_rate_entry.insert(0, str(settings['refresh_rate']))
        
        # Submit button
        self.submit_button = tk.Button(root, text="Submit", command=self.submit)
        self.submit_button.pack(pady=10)
        style = ttk.Style()
        style.theme_use('clam')  
        
    def submit(self):
        latitude = self.latitude_entry.get()
        longitude = self.longitude_entry.get()
        api = self.api_entry.get()
        refresh_rate = self.refresh_rate_entry.get()
        
        # Save settings to the database
        conn = sqlite3.connect('settings.db')
        cursor = conn.cursor()
        
        # Check if a row already exists
        cursor.execute("SELECT COUNT(*) FROM main")
        count = cursor.fetchone()[0]
        
        if count > 0:
            # Update the existing row
            cursor.execute("UPDATE main SET latitude = ?, longitude = ?, api = ?, refresh_rate = ? WHERE rowid = 1",
                           (latitude, longitude, api, refresh_rate))
        else:
            # Insert a new row
            cursor.execute("INSERT INTO main (latitude, longitude, api, refresh_rate) VALUES (?, ?, ?, ?)",
                           (latitude, longitude, api, refresh_rate))
        
        conn.commit()
        conn.close()
        
