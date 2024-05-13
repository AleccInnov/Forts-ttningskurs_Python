import tkinter as tk

# Skapar ditt window
window = tk.Tk()
window.title("Button")

# Skapar en funktion som gör något då knappen blir tryckt
def button_click():
    print("Button clicked!")

# Skapar en widget för knappen
button = tk.Button(window, text="Klicka här!", command=button_click) #, command=button_click
button.pack()

button2 = tk.Button(window, text="Klicka här igen!", command=button_click) #, command=button_click
button2.pack()

# Kör Tkinters eventloop
window.mainloop()
