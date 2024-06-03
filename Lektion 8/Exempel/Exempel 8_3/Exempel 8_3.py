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
    
    # Create the initial ball
    ball_radius = 20
    ball_color = "#1122FF"
    ball = Ball(canvas, canvas_width, canvas_height, ball_color, ball_radius)
    
    # Create a new ball
    create_new_ball(canvas, canvas_width, canvas_height, Ball)

    # Start moving the ball
    move_ball(ball, root)


    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    main()
