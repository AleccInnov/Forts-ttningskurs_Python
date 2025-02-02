import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

circle = canvas.create_oval(50, 50, 100, 100, fill="purple")
rectangle = canvas.create_rectangle(120, 50, 170, 100, fill="green")

root.mainloop()
