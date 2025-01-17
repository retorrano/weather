import tkinter as tk
from tkinter import ttk

class AboutGui:
    def __init__(self, parent):
        self.parent = parent
        self.info = (
            "Created by: Romano E. Torrano\n"
            "Email: romano.torrano@gmail.com\n"
            "Facebook: https://facebook.com/retorrano\n"
            "X: https://x.com/r_torrano\n\n"
            "Note: This is not an IoT application\n"
            "and not a substitute to sensors"

        )

    def show_info(self):
        window = tk.Toplevel(self.parent)
        window.title("Author Information")
        window.geometry("300x150")

        label = tk.Label(window, text=self.info, padx=10, pady=10)
        label.pack()
        style = ttk.Style()
        style.theme_use('clam')  

        window.mainloop()
