import tkinter as tk

# Create the main application window
window = tk.Tk()
window.title("Label")

# Create a label widget
label = tk.Label(window, text="Hello world!")
label.pack()

# Run the Tkinter event loop
window.mainloop()
