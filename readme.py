import tkinter as tk
from tkinter import ttk

class ReadmeGui:
    def __init__(self, parent):
        self.parent = parent
        self.info = (
            "This application is designed to provide weather data input functionality.\n\n"
            "Instructions:\n"
            "1. Click the 'Start' button to begin updating weather data.\n"
            "2. The data will be fetched and displayed every 5 minutes.\n"
            "3. You can edit settings through the 'Settings' option in the 'Edit' menu.\n\n"
            "Features:\n"
            "- Displays temperature in Celsius.\n"
            "- Shows heat index and relative humidity.\n"
            "- Provides wind direction, speed, and gust information.\n"
            "- Includes a rain gauge measurement.\n"
            "- Displays the last updated time.\n\n"
            "Note: This is not an IoT application and not a substitute to sensors.\n\n"
            "Contact Information:\n"
            "Created by: Romano E. Torrano\n"
            "Email: romano.torrano@gmail.com\n"
            "Facebook: https://facebook.com/retorrano\n"
            "X: https://x.com/r_torrano\n"
        )

    def show_info(self):
        window = tk.Toplevel(self.parent)
        window.title("Readme")
        window.geometry("400x300")

        # Create a frame for the Text widget and Scrollbar
        frame = ttk.Frame(window)
        frame.pack(fill='both', expand=True)

        # Create a Text widget with a vertical scrollbar
        text_widget = tk.Text(frame, wrap='word', padx=10, pady=10)
        scrollbar = ttk.Scrollbar(frame, orient='vertical', command=text_widget.yview)
        text_widget['yscrollcommand'] = scrollbar.set

        # Pack the Text widget and Scrollbar
        scrollbar.pack(side='right', fill='y')
        text_widget.pack(side='left', fill='both', expand=True)

        # Insert the long text into the Text widget
        text_widget.insert('1.0', self.info)

        # Make the text widget read-only
        text_widget.config(state='disabled')

        window.mainloop()
