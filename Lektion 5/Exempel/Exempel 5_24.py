import tkinter as tk

class CanvasDemo:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=300, height=200, bg="white")
        self.canvas.pack()

        # Create rectangles with the same tag
        self.rect1 = self.canvas.create_rectangle(50, 50, 100, 100, fill="blue", tags="my_tag")
        self.rect2 = self.canvas.create_rectangle(150, 50, 200, 100, fill="green", tags="my_tag")
        self.rect3 = self.canvas.create_rectangle(250, 50, 300, 100, fill="red", tags="my_tag")

        # Create a button to change color of rectangles
        self.button = tk.Button(self.master, text="Change Color", command=self.change_color)
        self.button.pack()

    def change_color(self):
        # Get all objects with the tag "my_tag"
        objects_with_tag = self.canvas.find_withtag("my_tag")
        #print(objects_with_tag)
        # Configure all objects with the tag to have the same fill color
        self.canvas.itemconfig("my_tag", fill="yellow")

def main():
    root = tk.Tk()
    root.title("Canvas Demo")
    app = CanvasDemo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
