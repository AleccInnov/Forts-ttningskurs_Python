import tkinter as tk

def change_color(color):
    frame_top.config(bg=color)

root = tk.Tk()
root.geometry("300x200")  
root.title("Avancerad Layout")

# Ramar för olika sektioner av layouten
frame_top = tk.Frame(root, bg="lightgray", pady=20)
frame_top.pack(fill=tk.BOTH, expand=True)

frame_bottom = tk.Frame(root, bg="lightblue", pady=20)
frame_bottom.pack(fill=tk.BOTH, expand=True)

# Knappar för att ändra bakgrundsfärg
button_red = tk.Button(frame_bottom, text="Röd", command=lambda: change_color("red"))
button_red.pack(side=tk.LEFT, padx=10)

button_green = tk.Button(frame_bottom, text="Grön", command=lambda: change_color("green"))
button_green.pack(side=tk.LEFT, padx=10)

button_blue = tk.Button(frame_bottom, text="Blå", command=lambda: change_color("blue"))
button_blue.pack(side=tk.LEFT, padx=10)

# Knappar med olika ramdesign
button_raised = tk.Button(frame_top, text="Raised", relief=tk.RAISED)
button_raised.pack(side=tk.LEFT, padx=10)

button_sunken = tk.Button(frame_top, text="Sunken", relief=tk.SUNKEN)
button_sunken.pack(side=tk.LEFT, padx=10)

button_groove = tk.Button(frame_top, text="Groove", relief=tk.GROOVE)
button_groove.pack(side=tk.LEFT, padx=10)

button_ridge = tk.Button(frame_top, text="Ridge", relief=tk.RIDGE)
button_ridge.pack(side=tk.LEFT, padx=10)

root.mainloop()
