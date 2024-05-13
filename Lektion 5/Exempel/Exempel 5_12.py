import tkinter as tk

def select(value):
    label.config(text="Du har valt: " + value)

window = tk.Tk()
window.title("Dropdown")

options = ["Päron", "Äpple", "Banan"]

selected_option = tk.StringVar()
selected_option.set(options[0])  # Default

dropdown = tk.OptionMenu(window, selected_option, *options, command=select)
dropdown.pack()

label = tk.Label(window, text="Du har valt: " + options[0])
label.pack()

window.mainloop()






