import tkinter as tk
import random
from Ballclass4 import Ball
from Ballfunc4 import create_new_ball, move_ball

def main():
    root = tk.Tk()
    root.title("Bollklickspelet")
    
    # Skapa canvas
    canvas_width = 400
    canvas_height = 400
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()

    # Lista med flera bollar
    balls = []

    # Skapa boll och lägga till boll i listan
    ball_radius = 20
    ball_color = "#1122FF"
    ball = Ball(canvas, canvas_width, canvas_height, ball_color, ball_radius)
    
    # Lägga till ball i listan balls
    balls.append(ball)
    
    create_new_ball(canvas, canvas_width, canvas_height, Ball, balls)

    # Bollarna rör sig
    move_ball(balls, root)

    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    main()
