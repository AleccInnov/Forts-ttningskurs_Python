import tkinter as tk

root = tk.Tk()
root.title("Exempel")

label = tk.Label(root, text="Hej världen!", bg="#FF0000", fg="navy")
label.pack(pady=200, padx=200)

root.mainloop()
