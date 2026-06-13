import tkinter as tk

from login import Login
from database import create_users_table


create_users_table()


window = tk.Tk()


window.title(
    "ExpenseMate"
)


window.geometry(
    "1100x700"
)


Login(window)


window.mainloop()