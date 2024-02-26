import tkinter as tk

root = tk.Tk()
root.title("Exempel")

label = tk.Label(root, text="Hej världen!", bg="lightblue", fg="navy")
label.pack(pady=20, padx=20)

root.mainloop()
