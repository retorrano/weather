import tkinter as tk

class AboutGui:
    def __init__(self, parent):
        self.parent = parent
        self.info = (
            "Created by: Romano E. Torrano\n"
            "Email: romano.torrano@gmail.com\n"
            "Facebook: https://facebook.com/retorrano\n"
            "X: https://x.com/r_torrano"
        )

    def show_info(self):
        window = tk.Toplevel(self.parent)
        window.title("Information")
        window.geometry("300x150")

        label = tk.Label(window, text=self.info, padx=10, pady=10)
        label.pack()

        window.mainloop()
