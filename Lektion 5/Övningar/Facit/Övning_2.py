import tkinter as tk

def change_color():
    color = radio_var.get()
    label.config(background=color)

root = tk.Tk()

radio_var = tk.StringVar()
radio_var.set("black")

radio1 = tk.Radiobutton(root, text="Röd", variable=radio_var, value="red", command=change_color)
radio2 = tk.Radiobutton(root, text="Grön", variable=radio_var, value="green", command=change_color)
radio3 = tk.Radiobutton(root, text="Blå", variable=radio_var, value="blue", command=change_color)
radio4 = tk.Radiobutton(root, text="Gul", variable=radio_var, value="yellow", command=change_color)

radio1.pack()
radio2.pack()
radio3.pack()
radio4.pack()

label = tk.Label(root, text="Hello, world!", foreground="black")
label.pack()

root.mainloop()
