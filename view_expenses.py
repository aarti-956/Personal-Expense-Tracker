import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv

from database import (
    view_expenses,
    delete_expense,
    update_expense
)



class ViewExpenses:


    def __init__(self, window):


        self.window = window



        for widget in window.winfo_children():
            widget.destroy()



        window.configure(
            bg="#f4f7fb"
        )


        window.title(
            "ExpenseMate - View Expenses"
        )


        window.geometry(
            "1100x700"
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
            text="📋 Expense History",
            font=("Arial",26,"bold"),
            bg="#6C63FF",
            fg="white"
        )


        title.pack(
            pady=30
        )





        # Main Card

        main_card = tk.Frame(
            window,
            bg="white"
        )


        main_card.pack(
            pady=25,
            padx=40
        )





        # Search Area

        search_frame = tk.Frame(
            main_card,
            bg="white"
        )


        search_frame.pack(
            pady=15
        )



        tk.Label(
            search_frame,
            text="🔍 Search",
            font=("Arial",13,"bold"),
            bg="white",
            fg="#2c3e50"
        ).pack(
            side="left",
            padx=10
        )



        self.search_entry = ttk.Entry(
            search_frame,
            width=35
        )


        self.search_entry.pack(
            side="left",
            padx=10
        )



        search_btn = tk.Button(
            search_frame,
            text="Search",
            font=("Arial",12,"bold"),
            bg="#3498db",
            fg="white",
            width=12,
            bd=0,
            command=self.search_expense
        )


        search_btn.pack(
            side="left"
        )





        # Table Area

        table_frame = tk.Frame(
            main_card,
            bg="white"
        )


        table_frame.pack(
            pady=15
        )




        columns = (
            "ID",
            "Amount",
            "Category",
            "Date",
            "Description"
        )



        self.table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=12
        )




        for col in columns:


            self.table.heading(
                col,
                text=col
            )


            self.table.column(
                col,
                anchor="center",
                width=130
            )



        self.table.column(
            "Description",
            width=220
        )




        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.table.yview
        )



        self.table.configure(
            yscrollcommand=scrollbar.set
        )



        self.table.pack(
            side="left"
        )


        scrollbar.pack(
            side="right",
            fill="y"
        )



        self.load_expenses()




        # Buttons

        button_frame = tk.Frame(
            window,
            bg="#f4f7fb"
        )


        button_frame.pack(
            pady=20
        )



        delete_btn = tk.Button(
            button_frame,
            text="🗑 Delete",
            font=("Arial",12,"bold"),
            bg="#e74c3c",
            fg="white",
            width=15,
            height=2,
            bd=0,
            command=self.delete_selected
        )


        delete_btn.grid(
            row=0,
            column=0,
            padx=10
        )




        edit_btn = tk.Button(
            button_frame,
            text="✏ Edit",
            font=("Arial",12,"bold"),
            bg="#2980b9",
            fg="white",
            width=15,
            height=2,
            bd=0,
            command=self.edit_selected
        )


        edit_btn.grid(
            row=0,
            column=1,
            padx=10
        )
        export_btn = tk.Button(
            button_frame,
            text="📤 Export CSV",
            font=("Arial",12,"bold"),
            bg="#8e44ad",
            fg="white",
            width=15,
            height=2,
            bd=0,
            command=self.export_csv
        )


        export_btn.grid(
            row=0,
            column=2,
            padx=10
        )



        back_button = tk.Button(
            window,
            text="← Back to Dashboard",
            font=("Arial",12,"bold"),
            bg="#34495e",
            fg="white",
            width=22,
            height=2,
            bd=0,
            command=self.back_dashboard
        )


        back_button.pack(
            pady=10
        )




    def delete_selected(self):


        selected = self.table.selection()



        if not selected:


            messagebox.showwarning(
                "Warning",
                "Select an expense first"
            )

            return





        item = self.table.item(
            selected[0]
        )



        expense_id = item["values"][0]



        delete_expense(
            expense_id
        )



        for row in self.table.get_children():

            self.table.delete(row)



        self.load_expenses()



        messagebox.showinfo(
            "Deleted",
            "Expense deleted successfully"
        )







    def edit_selected(self):


        selected = self.table.selection()



        if not selected:


            messagebox.showwarning(
                "Warning",
                "Select an expense first"
            )

            return





        item = self.table.item(
            selected[0]
        )


        data = item["values"]




        edit_window = tk.Toplevel(
            self.window
        )


        edit_window.title(
            "Edit Expense"
        )


        edit_window.geometry(
            "450x450"
        )


        edit_window.configure(
            bg="#f4f7fb"
        )





        card = tk.Frame(
            edit_window,
            bg="white"
        )


        card.pack(
            pady=30,
            padx=30
        )





        tk.Label(
            card,
            text="Amount",
            font=("Arial",13,"bold"),
            bg="white"
        ).pack(
            pady=5
        )



        amount_entry = ttk.Entry(
            card,
            width=30
        )


        amount_entry.pack(
            pady=5
        )


        amount_entry.insert(
            0,
            data[1]
        )





        tk.Label(
            card,
            text="Category",
            font=("Arial",13,"bold"),
            bg="white"
        ).pack(
            pady=5
        )



        category_entry = ttk.Entry(
            card,
            width=30
        )


        category_entry.pack(
            pady=5
        )


        category_entry.insert(
            0,
            data[2]
        )






        tk.Label(
            card,
            text="Description",
            font=("Arial",13,"bold"),
            bg="white"
        ).pack(
            pady=5
        )



        description_entry = ttk.Entry(
            card,
            width=30
        )


        description_entry.pack(
            pady=5
        )


        description_entry.insert(
            0,
            data[4]
        )







        def update():


            update_expense(
                data[0],
                amount_entry.get(),
                category_entry.get(),
                data[3],
                description_entry.get()
            )


            edit_window.destroy()



            for row in self.table.get_children():

                self.table.delete(row)



            self.load_expenses()



            messagebox.showinfo(
                "Updated",
                "Expense updated successfully"
            )






        update_btn = tk.Button(
            card,
            text="Update Expense",
            font=("Arial",12,"bold"),
            bg="#00B894",
            fg="white",
            width=20,
            height=2,
            command=update
        )


        update_btn.pack(
            pady=20
        )






    def back_dashboard(self):


        from dashboard import Dashboard


        Dashboard(
            self.window
        )







    def export_csv(self):


        file = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[
                ("CSV Files","*.csv")
            ]
        )



        if file == "":

            return





        rows = []



        for row in self.table.get_children():


            data = self.table.item(row)["values"]

            rows.append(data)





        with open(
            file,
            mode="w",
            newline=""
        ) as f:


            writer = csv.writer(f)



            writer.writerow(
                [
                    "ID",
                    "Amount",
                    "Category",
                    "Date",
                    "Description"
                ]
            )


            writer.writerows(
                rows
            )



        messagebox.showinfo(
            "Export Complete",
            "Expenses exported successfully"
        )







    def search_expense(self):


        keyword = self.search_entry.get().lower()



        for row in self.table.get_children():

            self.table.delete(row)





        records = view_expenses()




        for expense in records:


            if keyword in str(expense).lower():


                self.table.insert(
                    "",
                    tk.END,
                    values=expense
                )







    def load_expenses(self):


        records = view_expenses()



        for expense in records:


            self.table.insert(
                "",
                tk.END,
                values=expense
            )