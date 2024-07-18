import tkinter as tk
from tkinter import ttk

class ReadmeGui:
    def __init__(self, parent):
        self.parent = parent
        self.info = (
            "This is an IoT application that retrieves data thru API calls in\"
            "weatherapi.com, you have to signup in https://www.weatherapi.com.\n"
            "After signingup, request for API key. Note it down for easy retrieval.\n"
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
