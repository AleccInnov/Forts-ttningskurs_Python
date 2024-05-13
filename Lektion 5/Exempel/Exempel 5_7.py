import tkinter as tk

# Main window
window = tk.Tk()
window.title("Frame med Grid")

# Skapa frame
frame = tk.Frame(window)
frame.grid()

# Lägg i widgets i frame
label = tk.Label(frame, text="Label")
label.grid(row=2, column=2)

button = tk.Button(frame, text="Button")
button.grid(row=1, column=10)


window.mainloop()
