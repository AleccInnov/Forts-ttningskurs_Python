import tkinter as tk

win = tk.Tk()

# add an orange frame
frame1 = tk.Frame(win, width=100, height=100, bg="orange")
frame1.pack()

# add blue frame
frame2 = tk.Frame(win, width=50, height=50, bg="blue")
frame2.pack()

# add green frame
frame3 = tk.Frame(win, width=25, height=25, bg="green")
frame3.pack()

win.mainloop()
