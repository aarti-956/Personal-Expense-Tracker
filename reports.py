import tkinter as tk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from database import view_expenses



class Reports:


    def __init__(self, window):


        self.window = window



        for widget in window.winfo_children():
            widget.destroy()



        window.configure(
            bg="#f4f7fb"
        )


        window.title(
            "ExpenseMate - Reports"
        )


        window.geometry(
            "1000x700"
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
            text="📊 Expense Reports",
            font=("Arial",26,"bold"),
            bg="#6C63FF",
            fg="white"
        )


        title.pack(
            pady=30
        )






        # Chart Card

        chart_card = tk.Frame(
            window,
            bg="white",
            width=750,
            height=500
        )


        chart_card.pack(
            pady=30
        )


        chart_card.pack_propagate(
            False
        )



        self.chart_frame = chart_card



        self.create_chart()





        # Back Button

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
            pady=15
        )







    def back_dashboard(self):


        from dashboard import Dashboard


        Dashboard(
            self.window
        )









    def create_chart(self):


        records = view_expenses()



        categories = {}





        for row in records:


            category = row[2]

            amount = float(row[1])



            if category in categories:


                categories[category] += amount


            else:


                categories[category] = amount








        figure = Figure(
            figsize=(6,5),
            dpi=100,
            facecolor="white"
        )



        chart = figure.add_subplot(111)





        if categories:


            chart.pie(
                categories.values(),
                labels=categories.keys(),
                autopct="%1.1f%%"
            )



        else:


            chart.text(
                0.5,
                0.5,
                "No Expenses Yet",
                ha="center",
                va="center",
                fontsize=14
            )





        chart.set_title(
            "Expense Distribution",
            fontsize=14,
            fontweight="bold"
        )






        canvas = FigureCanvasTkAgg(
            figure,
            self.chart_frame
        )


        canvas.draw()



        canvas.get_tk_widget().pack(
            pady=25
        )