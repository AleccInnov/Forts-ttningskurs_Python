import random
import tkinter as tk

def create_new_ball(canvas, canvas_width, canvas_height, Ball, balls):
    ball_radius = 20
    ball_color = "#FF0000"
    new_ball = Ball(canvas, canvas_width, canvas_height, ball_color, ball_radius)
    balls.append(new_ball)

def move_ball(balls, root):
    for i, ball in enumerate(balls):
        ball.move()
        # Check collision with other balls
        for other_ball in balls[i+1:]:
            ball.check_collision(other_ball)
    root.after(50, move_ball, balls, root)

def end_program(root):
    root.destroy()

def view_highscore(root):
    # Create a new window
    highscore_window = tk.Toplevel(root)
    highscore_window.title("Highscore")

    # Add widgets to the new window
    label = tk.Label(highscore_window, text="Highscore:")
    label.pack()
