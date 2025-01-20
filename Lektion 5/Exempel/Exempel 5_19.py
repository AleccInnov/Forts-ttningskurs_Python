import tkinter as tk

class MovingButton:
    def __init__(self, master):
        self.master = master
        self.button = tk.Button(self.master, text="Klicka här!", command=self.move)
        self.button.pack()
        self.dy = 1  # Hur snabbt den flyttar sig vertikalt
        self.move_button()  # Anropa funktionen move_button()

    def move_button(self):
        # Vad är positionerna?
        x, y = self.button.winfo_x(), self.button.winfo_y()

        # Räkna ut ny position
        new_y = y + self.dy

        # Byt riktning då man slår i tak eller golv
        if new_y <= 0 or new_y >= self.master.winfo_height() - self.button.winfo_height():
            self.dy *= -1

        # Flytta till ny plats med place
        self.button.place(x=x, y=new_y)

        # När ska den flyttas igen?
        self.master.after(10, self.move_button)

    def move(self):
        # Vad som händer då man trycker på knappen
        print("Träff!")

def main():
    root = tk.Tk()
    root.geometry("300x200")  # Hur stort ska mitt fönster vara?
    root.title("Den studsande knappen")

    moving_button = MovingButton(root)

    root.mainloop()

if __name__ == "__main__":
    main()
