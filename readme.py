import tkinter as tk
from tkinter import ttk

class ReadmeGui:
    def __init__(self, parent):
        self.parent = parent
        self.info = (
            "This is an IoT application that retrieves data thru API calls in"
            "weatherapi.com.\n"
            "Follow these steps:\n"
            "Step 1. Signup to https://weatherapi.com\n"
            "Step 2. Request a key (Note it down for easy retrieval).\n"
            "Step 3. Get your location coordinates. Convert it to decimal degrees.\n"
            "Step 4. Run the application.\n"
            "Step 5. In the Edit menu, click Settings.\n"
            "Step 6. A pop up window will appear. Enter your latitude, longitude, api and refresh rate in seconds, minimum of 30\n"
            "Step 7. Click Submit.\n"
            "Step 8. Click Start Button.\n"
            "\n\n\n"
            "Note that this is not a substitute to sensors\n"

            
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
        style = ttk.Style()
        style.theme_use('clam')  

        window.mainloop()
