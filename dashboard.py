import tkinter as tk

from add_expense import AddExpense
from view_expenses import ViewExpenses
from reports import Reports
from database import get_dashboard_data



class Dashboard:


    def __init__(self, window):


        self.window = window


        for widget in window.winfo_children():
            widget.destroy()



        window.configure(
            bg="#f4f7fb"
        )


        window.title(
            "ExpenseMate Dashboard"
        )


        window.geometry(
            "1100x700"
        )



        # Header

        header = tk.Frame(
            window,
            bg="#6C63FF",
            height=110
        )

        header.pack(
            fill="x"
        )



        title = tk.Label(
            header,
            text="💰 ExpenseMate",
            font=("Arial",28,"bold"),
            bg="#6C63FF",
            fg="white"
        )


        title.pack(
            side="left",
            padx=45,
            pady=30
        )



        welcome = tk.Label(
            header,
            text="Welcome 👋",
            font=("Arial",15,"bold"),
            bg="#6C63FF",
            fg="white"
        )


        welcome.pack(
            side="right",
            padx=45
        )




        # Data

        total, count = get_dashboard_data()



        # Cards

        cards = tk.Frame(
            window,
            bg="#f4f7fb"
        )


        cards.pack(
            pady=50
        )



        self.create_card(
            cards,
            "Total Expense",
            f"₹ {total}",
            "#00B894",
            0
        )



        self.create_card(
            cards,
            "Transactions",
            str(count),
            "#3498db",
            1
        )



        self.create_card(
            cards,
            "this month's expense",
            f"₹ {total}",
            "#8e44ad",
            2
        )





        # Buttons Frame

        button_frame = tk.Frame(
            window,
            bg="#f4f7fb"
        )


        button_frame.pack(
            pady=20
        )



        tk.Button(
            button_frame,
            text="➕ Add Expense",
            width=25,
            height=2,
            bg="#00B894",
            fg="white",
            font=("Arial",13,"bold"),
            bd=0,
            command=self.open_add_expense
        ).grid(
            row=0,
            column=0,
            padx=15
        )



        tk.Button(
            button_frame,
            text="📋 View Expenses",
            width=25,
            height=2,
            bg="#3498db",
            fg="white",
            font=("Arial",13,"bold"),
            bd=0,
            command=self.open_view_expenses
        ).grid(
            row=0,
            column=1,
            padx=15
        )



        tk.Button(
            button_frame,
            text="📊 Reports",
            width=25,
            height=2,
            bg="#8e44ad",
            fg="white",
            font=("Arial",13,"bold"),
            bd=0,
            command=self.open_reports
        ).grid(
            row=0,
            column=2,
            padx=15
        )






    def create_card(
        self,
        parent,
        title,
        value,
        color,
        column
    ):


        card = tk.Frame(
            parent,
            bg="white",
            width=250,
            height=150
        )


        card.grid(
            row=0,
            column=column,
            padx=25
        )


        card.pack_propagate(
            False
        )



        tk.Frame(
            card,
            bg=color,
            height=8
        ).pack(
            fill="x"
        )



        tk.Label(
            card,
            text=title,
            font=("Arial",14,"bold"),
            bg="white",
            fg="#555"
        ).pack(
            pady=20
        )



        tk.Label(
            card,
            text=value,
            font=("Arial",24,"bold"),
            bg="white",
            fg=color
        ).pack()





    def open_add_expense(self):

        AddExpense(
            self.window
        )





    def open_view_expenses(self):

        ViewExpenses(
            self.window
        )





    def open_reports(self):

        Reports(
            self.window
        )