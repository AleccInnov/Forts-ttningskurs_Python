import tkinter as tk

def print_button():
    print("Vald:", radio_var.get())

window = tk.Tk()
window.title("Radiobutton")

# Hur många radiobuttons som ska skapas
num_radiobuttons = 5

# Vilket val som väljs
radio_var = tk.StringVar(value = "Option 1")

# Skapa radiobuttons
def create_radiobutton(value):
    return tk.Radiobutton(window, text=f"Option {value}", variable=radio_var, value=f"Option {value}")

# Packa radiobuttons
for i in range(1, num_radiobuttons+1):
    radiobutton = create_radiobutton(i)
    radiobutton.pack()

chosen_button = tk.Button(window, text="Val", command=print_button)
chosen_button.pack()

window.mainloop()
