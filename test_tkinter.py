import tkinter as tk
from tkinter import ttk


# Main Window
window = tk.Tk()

window.title("ExpenseMate - Personal Expense Tracker")
window.geometry("700x600")
window.configure(bg="#f2f5f9")


# -------- Header --------

header = tk.Frame(
    window,
    bg="#2c3e50",
    height=100
)

header.pack(fill="x")


title = tk.Label(
    header,
    text="ExpenseMate",
    font=("Arial", 28, "bold"),
    bg="#2c3e50",
    fg="white"
)

title.pack(pady=15)


subtitle = tk.Label(
    header,
    text="Personal Expense Tracker",
    font=("Arial", 12),
    bg="#2c3e50",
    fg="#dfe6e9"
)

subtitle.pack()


# -------- Main Card --------

card = tk.Frame(
    window,
    bg="white",
    bd=0
)

card.pack(
    pady=30,
    padx=50,
    fill="both"
)


# Amount

amount_label = tk.Label(
    card,
    text="Amount",
    font=("Arial",14),
    bg="white"
)

amount_label.pack(anchor="w", padx=40)


amount_entry = ttk.Entry(
    card,
    width=40
)

amount_entry.pack(
    pady=10,
    padx=40
)


# Category

category_label = tk.Label(
    card,
    text="Category",
    font=("Arial",14),
    bg="white"
)

category_label.pack(anchor="w", padx=40)


category_entry = ttk.Entry(
    card,
    width=40
)

category_entry.pack(
    pady=10,
    padx=40
)



# Description

description_label = tk.Label(
    card,
    text="Description",
    font=("Arial",14),
    bg="white"
)

description_label.pack(anchor="w", padx=40)


description_entry = ttk.Entry(
    card,
    width=40
)

description_entry.pack(
    pady=10,
    padx=40
)



# Save Button

save_button = tk.Button(
    card,
    text="💾 Save Expense",
    font=("Arial",14,"bold"),
    bg="#27ae60",
    fg="white",
    width=20,
    height=2,
    relief="flat"
)

save_button.pack(
    pady=30
)



# Footer

footer = tk.Label(
    window,
    text="Track • Manage • Analyze your money",
    font=("Arial",11),
    bg="#f2f5f9",
    fg="#7f8c8d"
)

footer.pack(
    pady=10
)


window.mainloop()