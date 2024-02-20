import tkinter as tk

window = tk.Tk()
window.title("Text")

# Text
text = tk.Text(window)
text.insert(tk.END, "Textwidget")
text.pack()

window.mainloop()
