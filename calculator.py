import tkinter as tk
from tkinter import messagebox

def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def divide():
    try:
        num2 = float(entry2.get())
        if num2 == 0:
            result_label.config(text="Result: Error! Division by zero.")
        else:
            result = float(entry1.get()) / num2
            result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input fields
label1 = tk.Label(root, text="Enter first number:")
label1.grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="Enter second number:")
label2.grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Create buttons for operations
add_button = tk.Button(root, text="Add", command=add)
add_button.grid(row=2, column=0)

subtract_button = tk.Button(root, text="Subtract", command=subtract)
subtract_button.grid(row=2, column=1)

multiply_button = tk.Button(root, text="Multiply", command=multiply)
multiply_button.grid(row=3, column=0)

divide_button = tk.Button(root, text="Divide", command=divide)
divide_button.grid(row=3, column=1)

# Display the result
result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, columnspan=2)

root.mainloop()
