import tkinter as tk

win= tk.Tk()

frame1 = tk.Frame(win, height=80, bg="red")
# adding the fill argument with 
# horizontal fill value
frame1.pack(fill=tk.X)

frame2 = tk.Frame(win, height=50, bg="yellow")
frame2.pack(fill=tk.X)

frame3 = tk.Frame(win, height=40, bg="blue")
frame3.pack(fill=tk.X)

win.mainloop()
