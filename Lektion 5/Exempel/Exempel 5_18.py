import tkinter as tk

win = tk.Tk()

frame1 = tk.Frame(win, bg="Yellow", width=200, height=100)
# setting fill, side and expand
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(win, width=100, bg="blue")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(win, width=50, bg="green")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

win.mainloop()
