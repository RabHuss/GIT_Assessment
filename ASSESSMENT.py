import tkinter as tk
from tkinter import ttk, messagebox

# Initialize root window
root = tk.Tk()
root.title("Personal Finance Tracker")
root.geometry("500x400")

# Transaction storage
transactions = []

# Functions
def add_transaction():
    date = date_entry.get()
    category = category_entry.get()
    amount = amount_entry.get()
    trans_type = trans_type_var.get()

    if not date or not category or not amount:
        messagebox.showerror("Input Error", "All fields are required!")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Input Error", "Amount must be a number!")
        return

    transactions.append({"date": date, "category": category, "amount": amount, "type": trans_type})
    update_summary()
    refresh_list()
    clear_entries()

def delete_transaction():
    selected = transaction_listbox.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a transaction to delete.")
        return

    index = selected[0]
    transactions.pop(index)
    update_summary()
    refresh_list()

def update_summary():
    total_income = sum(t["amount"] for t in transactions if t["type"] == "Income")
    total_expenses = sum(t["amount"] for t in transactions if t["type"] == "Expense")
    balance = total_income - total_expenses

    summary_label.config(text=f"Income: ${total_income:.2f}  |  Expenses: ${total_expenses:.2f}  |  Balance: ${balance:.2f}")

def refresh_list():
    transaction_listbox.delete(0, tk.END)
    for t in transactions:
        transaction_listbox.insert(tk.END, f"{t['date']} | {t['category']} | {t['type']} | ${t['amount']}")

def clear_entries():
    date_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

# UI Layout
tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
date_entry = tk.Entry(root)
date_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Category:").grid(row=1, column=0, padx=5, pady=5)
category_entry = tk.Entry(root)
category_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Amount:").grid(row=2, column=0, padx=5, pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(row=2, column=1, padx=5, pady=5)

trans_type_var = tk.StringVar(value="Income")
tk.Radiobutton(root, text="Income", variable=trans_type_var, value="Income").grid(row=3, column=0, padx=5, pady=5)
tk.Radiobutton(root, text="Expense", variable=trans_type_var, value="Expense").grid(row=3, column=1, padx=5, pady=5)

tk.Button(root, text="Add Transaction", command=add_transaction).grid(row=4, column=0, columnspan=2, pady=5)
tk.Button(root, text="Delete Selected", command=delete_transaction).grid(row=5, column=0, columnspan=2, pady=5)

transaction_listbox = tk.Listbox(root, width=50)
transaction_listbox.grid(row=6, column=0, columnspan=2, pady=5)

summary_label = tk.Label(root, text="Income: $0.00  |  Expenses: $0.00  |  Balance: $0.00", font=("Arial", 10, "bold"))
summary_label.grid(row=7, column=0, columnspan=2, pady=10)

# Run application
root.mainloop()
