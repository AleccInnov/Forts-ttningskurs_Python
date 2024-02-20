import tkinter as tk

# Main window
window = tk.Tk()
window.title("Frame med Grid")

# Skapa frame
frame = tk.Frame(window)
frame.grid()

# Lägg i widgets i frame
label = tk.Label(frame, text="Label")
label.grid(row=0, column=0)

button = tk.Button(frame, text="Button")
button.grid(row=1, column=0)


window.mainloop()
