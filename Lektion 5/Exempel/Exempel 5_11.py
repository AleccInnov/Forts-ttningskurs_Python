import tkinter as tk

window = tk.Tk()
window.title("Radiobutton")

# Radiobutton
radio_var = tk.StringVar(value="Option 1")
radio1 = tk.Radiobutton(window, text="Option 1", variable=radio_var, value="Option 1")
radio2 = tk.Radiobutton(window, text="Option 2", variable=radio_var, value="Option 2")
radio1.pack()
radio2.pack()


window.mainloop()
