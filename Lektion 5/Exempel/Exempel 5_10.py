import tkinter as tk

window = tk.Tk()
window.title("Checkbutton")

# Checkbutton
check_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(window, text="Checkbutton", variable=check_var)
checkbutton.pack()

window.mainloop()
