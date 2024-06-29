import tkinter as tk
from tkinter import ttk

def calculate_bmi():
    try:
        height = float(height_entry.get()) / 100  # Convert height from cm to meters
        weight = float(weight_entry.get())
        
        if height > 0 and weight > 0:
            bmi = weight / (height ** 2)
            result_label.config(text=f'BMI: {bmi:.2f}')
            if bmi < 18.5:
                status_label.config(text='Underweight', foreground='blue')
            elif bmi >= 18.5 and bmi < 25:
                status_label.config(text='Normal weight', foreground='green')
            elif bmi >= 25 and bmi < 30:
                status_label.config(text='Overweight', foreground='orange')
            else:
                status_label.config(text='Obesity', foreground='red')
        else:
            result_label.config(text='Invalid input')
            status_label.config(text='')
    except ValueError:
        result_label.config(text='Invalid input')
        status_label.config(text='')

def reset_fields():
    height_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    result_label.config(text='BMI: ')
    status_label.config(text='')

root = tk.Tk()
root.title('BMI Calculator')

# Customizing the style
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TButton', font=('Helvetica', 12), foreground='black', background='#4CAF50')
style.configure('TEntry', font=('Helvetica', 12))

# Background color and padding
root.configure(background='#f0f0f0')
root.geometry('300x300')

# Labels
height_label = ttk.Label(root, text='Height (cm):')
height_label.grid(row=0, column=0, padx=10, pady=10)

weight_label = ttk.Label(root, text='Weight (kg):')
weight_label.grid(row=1, column=0, padx=10, pady=10)

result_label = ttk.Label(root, text='BMI: ', font=('Helvetica', 14, 'bold'))
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

status_label = ttk.Label(root, text='', font=('Helvetica', 12))
status_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Entry widgets
height_entry = ttk.Entry(root, width=20)
height_entry.grid(row=0, column=1, padx=10, pady=10)

weight_entry = ttk.Entry(root, width=20)
weight_entry.grid(row=1, column=1, padx=10, pady=10)

# Buttons
calculate_button = ttk.Button(root, text='Calculate BMI', command=calculate_bmi, style='TButton')
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

reset_button = ttk.Button(root, text='Reset', command=reset_fields, style='TButton')
reset_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
