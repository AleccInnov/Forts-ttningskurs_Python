import tkinter as tk
import random

class Ball:
    def __init__(self, canvas, color, radius):
        self.canvas = canvas
        self.radius = radius
        self.color = color
        self.x_speed = random.randint(1, 5)
        self.y_speed = random.randint(1, 5)
        self.create_ball()

    def create_ball(self):
        x = random.randint(self.radius, canvas_width - self.radius)
        y = random.randint(self.radius, canvas_height - self.radius)
        self.ball = self.canvas.create_oval(x - self.radius, y - self.radius, x + self.radius, y + self.radius, fill=self.color)

    def move(self):
        self.canvas.move(self.ball, self.x_speed, self.y_speed)
        x1, y1, x2, y2 = self.canvas.coords(self.ball)
        
        if x1 <= 0 or x2 >= canvas_width:
            self.x_speed *= -1
        if y1 <= 0 or y2 >= canvas_height:
            self.y_speed *= -1


def move_ball():
    ball.move()
    root.after(50, move_ball)

def main():
    global root, canvas, ball, canvas_width, canvas_height
    
    # Fönstret
    root = tk.Tk()
    root.title("Bouncing Ball")

    # Canvas
    canvas_width = 500
    canvas_height = 500
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()

    # Skapa boll
    ball_radius = 20
    ball_color = "#1122FF"
    ball = Ball(canvas, ball_color, ball_radius)
    

    # Bollen rör sig
    move_ball()

    root.mainloop()

if __name__ == "__main__":
    main()
