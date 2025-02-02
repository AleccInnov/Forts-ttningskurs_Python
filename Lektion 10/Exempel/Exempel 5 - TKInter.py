import tkinter as tk

# Uppdatera displayen
def update_display(value):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current_text + value)

# Räkna och visa
def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.INSERT, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Main window
window = tk.Tk()
window.title("Kan du räkna 1+2?")

# Skapa display
display = tk.Entry(window, width=30, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Knappar
button1 = tk.Button(window, text='1', padx=20, pady=10, command=lambda t='1': update_display(t))
button1.grid(row=1, column=1)

button2 = tk.Button(window, text='2', padx=20, pady=10, command=lambda t='2': update_display(t))
button2.grid(row=1, column=3)

button3 = tk.Button(window, text='+', padx=20, pady=10, command=lambda t='+': update_display(t))
button3.grid(row=1, column=2)

equals_button = tk.Button(window, text='=', padx=20, pady=10, command=calculate)
equals_button.grid(row=1, column=4)


window.mainloop()
