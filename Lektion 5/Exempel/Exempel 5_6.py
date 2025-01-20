import tkinter as tk

# Main window
window = tk.Tk()
window.title("Frame Example med pack")

# Skapa frame
frame = tk.Frame(window)
frame.pack()

# Lägg till widgets i frame
label = tk.Label(frame, text="Här är en label")
label.pack()

button = tk.Button(frame, text="Klick!")
button.pack()

# Event loop
window.mainloop()
