import tkinter as tk

def change_color():
    if button.cget("foreground") == "red":
        button.config(foreground="blue")
    else:
        button.config(foreground="red")

root = tk.Tk()
button = tk.Button(root, text="Byt färg!", foreground="blue", command=change_color)
button.pack()
root.mainloop()
