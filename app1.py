import tkinter as tk
from tkinter import ttk
from financial_functions import FinancialFactors

fc = FinancialFactors()

def on_entry_click(event, entry):
    if entry.get() == entry.placeholder:
        entry.delete(0, tk.END)
        entry.config(fg='black')

def on_focus_out(event, entry):
    if not entry.get():
        entry.insert(0, entry.placeholder)
        entry.config(fg='grey')  

def calculate():
    interest_rate = float(entry_interest_rate.get())
    amount = float(entry_amount.get())
    interest_rate = interest_rate / 100
    year = int(entry_year.get())
    month = int(entry_month.get())
    periods = year + (month / 12) 
    selected_scenario = option_scenario.get()

    if selected_scenario == "F/A":
        future_amount = fc.F_A_given_A(interest_rate, periods, amount)
        result_label.config(text=f"Future Amount (F): {future_amount:.5f}")
    elif selected_scenario == "F/P":
        future_amount = fc.F_P_given_P(interest_rate, periods, amount)
        result_label.config(text=f"Future Amount (F): {future_amount:.5f}")
    elif selected_scenario == "P/F":
        future_amount = fc.P_F_given_F(interest_rate, periods, amount)
        result_label.config(text=f"Present Amount (P): {future_amount:.5f}")
    elif selected_scenario == "A/F":
        future_amount = fc.A_F_given_F(interest_rate, periods, amount)
        result_label.config(text=f"Annual Amount (A): {future_amount:.5f}")
    elif selected_scenario == "A/P":
        future_amount = fc.A_P_given_P(interest_rate, periods, amount)
        result_label.config(text=f"Annual Amount (A): {future_amount:.5f}")
    elif selected_scenario == "P/A":
        future_amount = fc.P_A_given_A(interest_rate, periods, amount)
        result_label.config(text=f"Present Amount (P): {future_amount:.5f}")

def update_labels(*args):
    selected_scenario = option_scenario.get()

    if selected_scenario == "F/A":
        label_amount.config(text="Annual Amount (A):")
    elif selected_scenario == "F/P":
        label_amount.config(text="Present Amount (P):")
    elif selected_scenario == "P/F":
        label_amount.config(text="Future Amount (F):")
    elif selected_scenario == "A/F":
        label_amount.config(text="Future Amount (F):")
    elif selected_scenario == "A/P":
        label_amount.config(text="Present Amount (P):")
    elif selected_scenario == "P/A":
        label_amount.config(text="Annual Amount (A):")

# Initialize Tkinter window
root = tk.Tk()
root.title("Financial Calculator")

# Tab control
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Financial Calculator')
tab_control.add(tab2, text='RoR Calculator')
tab_control.pack(expand=1, fill='both')

# Tab 1: Financial Calculator
label_scenario = tk.Label(tab1, text="Select Scenario:")
label_interest_rate = tk.Label(tab1, text="Interest Rate (i%):")
label_date = tk.Label(tab1, text="Select Period:")
label_amount = tk.Label(tab1, text="Present Amount (P):")
result_label = tk.Label(tab1, text="")
entry_interest_rate = tk.Entry(tab1)
entry_interest_rate.placeholder = "i%"
entry_interest_rate.config(fg='grey')  
entry_interest_rate.insert(0, entry_interest_rate.placeholder)
entry_interest_rate.bind('<FocusIn>', lambda event, entry=entry_interest_rate: on_entry_click(event, entry))
entry_interest_rate.bind('<FocusOut>', lambda event, entry=entry_interest_rate: on_focus_out(event, entry))
entry_year = tk.Entry(tab1)
entry_year.placeholder = "Year"
entry_year.config(fg='grey')  
entry_year.insert(0, entry_year.placeholder)
entry_year.bind('<FocusIn>', lambda event, entry=entry_year: on_entry_click(event, entry))
entry_year.bind('<FocusOut>', lambda event, entry=entry_year: on_focus_out(event, entry))
entry_month = tk.Entry(tab1)
entry_month.placeholder = "Month"
entry_month.config(fg='grey')  
entry_month.insert(0, entry_month.placeholder)
entry_month.bind('<FocusIn>', lambda event, entry=entry_month: on_entry_click(event, entry))
entry_month.bind('<FocusOut>', lambda event, entry=entry_month: on_focus_out(event, entry))
entry_amount = tk.Entry(tab1)
option_scenario = tk.StringVar(tab1)
option_scenario.set("F/P")  
scenario_choices = ["F/P", "P/F", "A/F", "F/A", "A/P", "P/A"]
scenario_menu = tk.OptionMenu(tab1, option_scenario, *scenario_choices)
calculate_button = tk.Button(tab1, text="Calculate", command=calculate)

# Layout for Tab 1
label_scenario.grid(row=0, column=0, padx=10, pady=5)
label_interest_rate.grid(row=1, column=0, padx=10, pady=5)
label_date.grid(row=2, column=0, padx=10, pady=5)
label_amount.grid(row=3, column=0, padx=10, pady=5)
scenario_menu.grid(row=0, column=1, padx=10, pady=5)
entry_interest_rate.grid(row=1, column=1, padx=10)
entry_year.grid(row=2, column=1, padx=10, pady=5)
entry_month.grid(row=2, column=2, padx=10, pady=5)
entry_amount.grid(row=3, column=1, padx=10, pady=5)
calculate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

option_scenario.trace_add("write", update_labels)

# Tab 2: RoR Calculator
label_ror = tk.Label(tab2, text="RoR Calculator")
label_ror.grid(row=0, column=0, padx=10, pady=5)

# Run the application
root.mainloop()
