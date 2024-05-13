import tkinter as tk

class CanvasDemo:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=300, height=200, bg="white")
        self.canvas.pack()

        # Skapa former
        self.rectangle = self.canvas.create_rectangle(50, 50, 150, 150, fill="blue")
        self.oval = self.canvas.create_oval(180, 50, 280, 150, fill="red")
        self.line = self.canvas.create_line(10, 100, 290, 100, fill="green", width=3)
        self.text = self.canvas.create_text(150, 180, text="Canvas Demo", fill="black")

        # Modifiera
        #self.canvas.itemconfig(self.rectangle, fill="lightblue")
        #self.canvas.itemconfig(self.oval, outline="orange", width=2)
        #self.canvas.itemconfig(self.text, font=("Arial", 12, "bold"))

        # Flytta
        self.canvas.move(self.line, 0, 20)

        # Vad händer om man trycker på en form (Binda event till den)
        self.canvas.tag_bind(self.rectangle, "<Button-1>", lambda event: self.change_color(self.rectangle))
        self.canvas.tag_bind(self.oval, "<Button-1>", lambda event: self.change_color(self.oval))

    def change_color(self, shape_id):
        current_color = self.canvas.itemcget(shape_id, "fill")
        new_color = "yellow" if current_color != "yellow" else "blue"
        self.canvas.itemconfig(shape_id, fill=new_color)

def main():
    root = tk.Tk()
    root.title("Canvas Demo")
    app = CanvasDemo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
