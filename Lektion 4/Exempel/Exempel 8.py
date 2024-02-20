import tkinter as tk

# Create the main application window
window = tk.Tk()
window.title("Place Example")

# Create a label and place it at coordinates (100, 50)
label = tk.Label(window, text="This is a label")
label.place(x=100, y=50)

# Create a button and place it at coordinates (150, 100)
button = tk.Button(window, text="Click Me!")
button.place(x=150, y=100)

# Run the Tkinter event loop
window.mainloop()
