import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from financial_functions import FinancialFactors

# Initialize FinancialFactors
fc = FinancialFactors()

# Copyright information
copyright_info = "@Mozafary 2024"

def irr():
    if len(cash_flows) == 0:
        messagebox.showerror("Error", "There are no cash flows to calculate IRR.")
        return
    irr_value = fc.Irr(cash_flows)
    if irr_value is np.nan or irr_value is np.inf or irr_value is -np.inf:
        messagebox.showerror('Error','IRR is not possible')
    else:
        messagebox.showinfo("IRR Calculation", f"The Internal Rate of Return (IRR) is: {irr_value*100:.2f}%")

def on_entry_click(event, entry):
    if entry.get() == entry.placeholder:
        entry.delete(0, tk.END)

def add_cash_flow():
    try:
        cash_flow = float(entry_cash_flow.get())
        cash_flows.append(cash_flow)
        update_plot()
        entry_cash_flow.delete(0, tk.END)  # Clear the entry field after adding cash flow
        if len(cash_flows) > 10:
            shift_plot('next')
            update_plot()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def update_plot():
    plt.clf()
    plt.axhline(0, color='midnightblue', lw=2)
    start_index = current_index
    end_index = min(len(cash_flows), current_index + 10)
    for i in range(start_index, end_index):
        plt.arrow(i - start_index, 0, 0, cash_flows[i], head_width=0.3 if cash_flows[i] >= 0 else -0.3, head_length=0.05 * abs(cash_flows[i]), color='springgreen' if cash_flows[i] >= 0 else 'coral', lw=2)
    if len(cash_flows) < 11:
        plt.xticks(range(11))
        plt.xlim(-0.5, 10.5)
        prev_button.config(state=tk.DISABLED)  # Disable the "Previous" button
        next_button.config(state=tk.DISABLED)  # Disable the "Next" button
    else:
        plt.xticks(range(end_index - start_index), range(start_index, end_index))
        prev_button.config(state=tk.NORMAL)   # Enable the "Previous" button
        next_button.config(state=tk.DISABLED if end_index == len(cash_flows) else tk.NORMAL)  # Disable "Next" button when at the end of cash flow list
    plt.xlabel('Time')
    plt.ylabel('Cash Flow')
    plt.title('Cash Flow Over Time')
    canvas.draw()

def clear_cash_flows():
    cash_flows.clear()
    entry_cash_flow.delete(0, tk.END)  # Clear the entry field after clearing cash flows
    update_plot()

def shift_plot(direction):
    global current_index
    if len(cash_flows) < 10:  # Check if cash flow length is less than 10
        return  # Do nothing if cash flow length is less than 10
    if direction == 'next' and current_index + 10 < len(cash_flows):
        current_index += 1
    elif direction == 'previous':
        current_index -= 1
        current_index = max(0, current_index)
    update_plot()

def edit_cash_flow_dialog():
    if len(cash_flows) == 0:
        messagebox.showerror("Error", "There are no cash flows to edit.")
        return
    index = simpledialog.askinteger("Edit Cash Flow", "Which Cashflow do you want to edit?", parent=app2)
    if index is not None and 0 <= index < len(cash_flows):
        new_cash_flow = simpledialog.askfloat("Edit Cash Flow", f"Enter the new cash flow value for cashflow number {index}:", parent=app2)
        if new_cash_flow is not None:
            edit_cash_flow(new_cash_flow, index)
        

def delete_cash_flow_dialog():
    if len(cash_flows) == 0:
        messagebox.showerror("Error", "There are no cash flows to delete.")
        return
    index = simpledialog.askinteger("Delete Cash Flow", "Which Cashflow do you want to delete?", parent=app2)
    if index is not None and 0 <= index < len(cash_flows):
        del cash_flows[index]
        update_plot()

def edit_cash_flow(new, index):
    cash_flows[index] = new
    update_plot()

app2 = tk.Tk()
app2.title("RoR Calculator")
app2.configure(bg="#EEEEEE")  # Set background color

label_cash_flow = tk.Label(app2, text="Cash Flow:", bg="#EEEEEE")
entry_cash_flow = tk.Entry(app2, bg="white")
entry_cash_flow.placeholder = "Enter Cash Flow"
entry_cash_flow.insert(0, entry_cash_flow.placeholder)
entry_cash_flow.bind('<FocusIn>', lambda event, entry=entry_cash_flow: on_entry_click(event, entry))
add_button = tk.Button(app2, text="Add", command=add_cash_flow, width=10)
clear_button = tk.Button(app2, text="Start/Clear", command=clear_cash_flows, width=10)
prev_button = tk.Button(app2, text="Previous", command=lambda: shift_plot('previous'), width=10)
next_button = tk.Button(app2, text="Next", command=lambda: shift_plot('next'), width=10)
edit_button = tk.Button(app2, text="Edit", command=edit_cash_flow_dialog, width=10)
delete_button = tk.Button(app2, text="Delete", command=delete_cash_flow_dialog, width=10)
calculate_button = tk.Button(app2, text="Calculate IRR", command=irr, width=30)
fig= plt.figure(facecolor="#EEEEEE")

canvas = FigureCanvasTkAgg(fig, master=app2)

label_cash_flow.grid(row=0, column=0, padx=10, pady=5)
entry_cash_flow.grid(row=0, column=1, padx=10, pady=5)
add_button.grid(row=0, column=2, padx=5, pady=5)
clear_button.grid(row=0, column=3, padx=5, pady=5)
prev_button.grid(row=2, column=1, padx=5, pady=5)
next_button.grid(row=2, column=2, padx=5, pady=5)
edit_button.grid(row=2, column=0, padx=5, pady=5)
delete_button.grid(row=3, column=0, padx=5, pady=5)
calculate_button.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

canvas.get_tk_widget().grid(row=1, column=0, columnspan=4, padx=10, pady=5)
tk.Label(app2, text=copyright_info, bg="#EEEEEE").grid(row=4, column=0, columnspan=4, pady=5)

cash_flows = []
current_index = 0

app2.mainloop()
