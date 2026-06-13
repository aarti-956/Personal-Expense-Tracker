import tkinter as tk
from tkinter import messagebox

from database import (
    login_user,
    register_user
)

from dashboard import Dashboard



class Login:


    def __init__(self, window):

        self.window = window


        for widget in window.winfo_children():
            widget.destroy()


        window.title(
            "ExpenseMate Login"
        )


        window.geometry(
            "1100x700"
        )


        # Background

        window.configure(
            bg="#6C63FF"
        )


        # Background title

        heading = tk.Label(
            window,
            text="ExpenseMate",
            font=("Arial",34,"bold"),
            bg="#6C63FF",
            fg="white"
        )

        heading.pack(
            pady=40
        )



        subtitle = tk.Label(
            window,
            text="Smart Expense Management System",
            font=("Arial",14),
            bg="#6C63FF",
            fg="white"
        )

        subtitle.pack()



        # Card

        card = tk.Frame(
            window,
            bg="white",
            width=420,
            height=430
        )

        card.place(
            relx=0.5,
            rely=0.55,
            anchor="center"
        )



        title = tk.Label(
            card,
            text="Welcome Back 👋",
            font=("Arial",22,"bold"),
            bg="white",
            fg="#333333"
        )

        title.pack(
            pady=30
        )



        # Username Label

        tk.Label(
            card,
            text="Username",
            bg="white",
            fg="#444",
            font=("Arial",11,"bold")
        ).pack(
            anchor="w",
            padx=60,
            pady=(10,5)
        )


        username_frame = tk.Frame(
            card,
            bg="#eeeeff"
        )

        username_frame.pack(
            padx=60,
            pady=5
        )


        self.username = tk.Entry(
            username_frame,
            width=28,
            font=("Arial",12),
            bd=0,
            bg="#eeeeff"
        )

        self.username.pack(
            ipady=8,
            ipadx=5
        )


        self.username.bind(
            "<Return>",
            lambda event: self.password.focus()
        )



        # Password Label

        tk.Label(
            card,
            text="Password",
            bg="white",
            fg="#444",
            font=("Arial",11,"bold")
        ).pack(
            anchor="w",
            padx=60,
            pady=(15,5)
        )



        password_frame = tk.Frame(
            card,
            bg="#eeeeff"
        )

        password_frame.pack(
            padx=60,
            pady=5
        )



        self.password = tk.Entry(
            password_frame,
            width=28,
            font=("Arial",12),
            bd=0,
            bg="#eeeeff",
            show="*"
        )

        self.password.pack(
            ipady=8,
            ipadx=5
        )


        self.password.bind(
            "<Return>",
            lambda event: self.login()
        )


        # Login button

        login_btn = tk.Button(
            card,
            text="🔐 Login",
            width=25,
            height=2,
            bg="#6C63FF",
            fg="white",
            font=("Arial",12,"bold"),
            bd=0,
            command=self.login
        )

        login_btn.pack(
            pady=15
        )



        # Register button

        register_btn = tk.Button(
            card,
            text="✨ Create Account",
            width=25,
            height=2,
            bg="#00B894",
            fg="white",
            font=("Arial",12,"bold"),
            bd=0,
            command=self.register
        )

        register_btn.pack()




    def login(self):

        user = login_user(
            self.username.get(),
            self.password.get()
        )


        if user:

            Dashboard(self.window)


        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid Username or Password"
            )




    def register(self):

        result = register_user(
            self.username.get(),
            self.password.get()
        )


        if result:

            messagebox.showinfo(
                "Success",
                "Account Created Successfully"
            )


        else:

            messagebox.showerror(
                "Error",
                "Username already exists"
            )