import tkinter as tk
from tkinter import ttk, messagebox
from database import add_expense
from datetime import date



class AddExpense:


    def __init__(self, window):


        self.window = window



        for widget in window.winfo_children():
            widget.destroy()



        window.configure(
            bg="#f4f7fb"
        )


        window.title(
            "ExpenseMate - Add Expense"
        )



        # Header

        header = tk.Frame(
            window,
            bg="#6C63FF",
            height=100
        )

        header.pack(
            fill="x"
        )



        title = tk.Label(
            header,
            text="➕ Add Expense",
            font=("Arial",26,"bold"),
            bg="#6C63FF",
            fg="white"
        )

        title.pack(
            pady=30
        )




        # Card

        card = tk.Frame(
            window,
            bg="white",
            width=500,
            height=430
        )

        card.pack(
            pady=35
        )


        card.pack_propagate(
            False
        )




        # Amount

        tk.Label(
            card,
            text="Amount",
            font=("Arial",14,"bold"),
            bg="white",
            fg="#2c3e50"
        ).pack(
            anchor="w",
            padx=60,
            pady=(35,5)
        )



        self.amount_entry = ttk.Entry(
            card,
            width=35
        )

        self.amount_entry.pack(
            pady=8,
            ipady=4
        )



        self.amount_entry.bind(
            "<Return>",
            lambda event:self.category_entry.focus()
        )





        # Category

        tk.Label(
            card,
            text="Category",
            font=("Arial",14,"bold"),
            bg="white",
            fg="#2c3e50"
        ).pack(
            anchor="w",
            padx=60,
            pady=(15,5)
        )



        self.category_entry = ttk.Entry(
            card,
            width=35
        )


        self.category_entry.pack(
            pady=8,
            ipady=4
        )



        self.category_entry.bind(
            "<Return>",
            lambda event:self.description_entry.focus()
        )





        # Description

        tk.Label(
            card,
            text="Description",
            font=("Arial",14,"bold"),
            bg="white",
            fg="#2c3e50"
        ).pack(
            anchor="w",
            padx=60,
            pady=(15,5)
        )



        self.description_entry = ttk.Entry(
            card,
            width=35
        )


        self.description_entry.pack(
            pady=8,
            ipady=4
        )



        self.description_entry.bind(
            "<Return>",
            lambda event:self.save_expense()
        )






        # Buttons

        button_frame = tk.Frame(
            card,
            bg="white"
        )

        button_frame.pack(
            pady=30
        )




        save_button = tk.Button(
            button_frame,
            text="💾 Save Expense",
            font=("Arial",12,"bold"),
            bg="#00B894",
            fg="white",
            width=18,
            height=2,
            bd=0,
            command=self.save_expense
        )


        save_button.grid(
            row=0,
            column=0,
            padx=10
        )





        back_button = tk.Button(
            button_frame,
            text="← Dashboard",
            font=("Arial",12,"bold"),
            bg="#34495e",
            fg="white",
            width=18,
            height=2,
            bd=0,
            command=self.back_dashboard
        )


        back_button.grid(
            row=0,
            column=1,
            padx=10
        )







    def save_expense(self):


        amount = self.amount_entry.get()

        category = self.category_entry.get()

        description = self.description_entry.get()




        if amount == "" or category == "":


            messagebox.showwarning(
                "Missing Data",
                "Please enter amount and category"
            )

            return





        try:


            amount = float(amount)



        except ValueError:


            messagebox.showerror(
                "Invalid Amount",
                "Amount must contain numbers only"
            )

            return





        if amount <= 0:


            messagebox.showerror(
                "Invalid Amount",
                "Amount must be greater than zero"
            )

            return





        today = str(date.today())




        add_expense(
            amount,
            category,
            today,
            description
        )




        messagebox.showinfo(
            "Success",
            "Expense Saved Successfully"
        )




        self.amount_entry.delete(
            0,
            tk.END
        )


        self.category_entry.delete(
            0,
            tk.END
        )


        self.description_entry.delete(
            0,
            tk.END
        )


        self.amount_entry.focus()





    def back_dashboard(self):


        from dashboard import Dashboard


        Dashboard(
            self.window
        )