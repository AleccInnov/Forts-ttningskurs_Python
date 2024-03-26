import tkinter as tk
import random
from Ballclass import Ball
from Ballfunc import create_new_ball, move_ball


def main():
    # Create the main window
    root = tk.Tk()
    root.title("Bollklickspelet")

    # Create the canvas
    canvas_width = 500
    canvas_height = 500
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()

    # Create a list to hold the balls
    balls = []

    # Create and append the initial balls
    ball_radius = 20
    ball_color = "red"
    ball = Ball(canvas, canvas_width, canvas_height, ball_color, ball_radius, balls)
    balls.append(ball)

    # Boll 1 rör sig
    move_ball(balls, root)

    root.mainloop()

if __name__ == "__main__":
    main()
