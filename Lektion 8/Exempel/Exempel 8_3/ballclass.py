import random

class Ball:
    def __init__(self, canvas, canvas_width, canvas_height, color, radius):
        self.canvas = canvas
        self.radius = radius
        self.color = color
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.x_speed = random.randint(1, 5)
        self.y_speed = random.randint(1, 5)
        self.x = random.randint(self.radius, self.canvas_width - self.radius)
        self.y = random.randint(self.radius, self.canvas_height - self.radius)
        self.ball = self.canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, fill=self.color)
        self.canvas.tag_bind(self.ball, '<Button-1>', self.change_color)

    def change_color(self, event):
        colors = ["red", "green", "blue", "yellow"]
        new_color = random.choice(colors)
        self.canvas.itemconfig(self.ball, fill=new_color)
        self.color = new_color   

    def move(self):
        self.canvas.move(self.ball, self.x_speed, self.y_speed)
        x1, y1, x2, y2 = self.canvas.coords(self.ball)
        
        if x1 <= 0 or x2 >= self.canvas_width:
            self.x_speed *= -1
        if y1 <= 0 or y2 >= self.canvas_height:
            self.y_speed *= -1


