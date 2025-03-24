import random

def create_new_ball(canvas, canvas_width, canvas_height, Ball):
    ball_radius = 20
    ball_color = "#FF0000"
    new_ball = Ball(canvas, canvas_width, canvas_height, ball_color, ball_radius)


def move_ball(ball, root):
    ball.move()
    root.after(50, move_ball, ball, root)
