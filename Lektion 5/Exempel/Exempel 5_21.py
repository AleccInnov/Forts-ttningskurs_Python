import tkinter as tk

win = tk.Tk()

canvas = tk.Canvas(win, width=200, height=100)
canvas.pack()  

canvas.create_rectangle(50, 20, 150, 80, fill="#476042")
canvas.create_rectangle(65, 35, 135, 65, fill="yellow")
canvas.create_line(0, 0, 50, 20, fill="#476042", width=3)
canvas.create_line(0, 100, 50, 80, fill="#476042", width=3)
canvas.create_line(150, 20, 200, 0, fill="#476042", width=3)
canvas.create_line(150, 80, 200, 100, fill="#476042", width=3)

win.mainloop()
