import tkinter as tk

# Skapar ditt window
window = tk.Tk()
window.title("Button")

# Skapar en funktion som gör något då knappen blir tryckt
#def button_click():
#    print("Button clicked!")

# Skapar en widget för knappen
button = tk.Button(window, text="Klicka här!") #, command=button_click
button.pack()

# Kör Tkinters eventloop
window.mainloop()
