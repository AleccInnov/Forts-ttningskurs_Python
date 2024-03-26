import random
class Ball:
    def __init__(self, canvas, canvas_width, canvas_height, color, radius, balls):
        self.canvas = canvas
        self.radius = radius
        self.color = color
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.x_speed = random.randint(1, 5)
        self.y_speed = random.randint(1, 5)
        x = random.randint(self.radius, self.canvas_width - self.radius)
        y = random.randint(self.radius, self.canvas_height - self.radius)
        self.ball = self.canvas.create_oval(x - self.radius, y - self.radius, x + self.radius, y + self.radius, fill=self.color)
        self.canvas.tag_bind(self.ball, '<Button-1>', self.on_click)
        self.balls = balls
        
    def on_click(self, event):
        if self.color == "red":
            self.create_random_ball()
        elif self.color == "yellow":
            self.change_color()
        elif self.color == "blue":
            self.change_direction()
            
    def change_direction(self):
        self.x_speed *= -1
        self.y_speed *= -1

    def create_random_ball(self):
        ball_radius = 20
        colors = ["red", "green", "blue", "yellow"]
        ball_color = random.choice(colors)
        new_ball = Ball(self.canvas, self.canvas_width, self.canvas_height, ball_color, ball_radius, self.balls)
        self.balls.append(new_ball)

    def change_color(self):
        new_color = "green"
        self.canvas.itemconfig(self.ball, fill=new_color)
        self.color = new_color   

    def move(self):
        self.canvas.move(self.ball, self.x_speed, self.y_speed)
        x1, y1, x2, y2 = self.canvas.coords(self.ball)
        
        if x1 <= 0 or x2 >= self.canvas_width:
            self.x_speed *= -1
        if y1 <= 0 or y2 >= self.canvas_height:
            self.y_speed *= -1

    def check_collision(self, other_ball):
        x1, y1, x2, y2 = self.canvas.coords(self.ball)
        x1_other, y1_other, x2_other, y2_other = self.canvas.coords(other_ball.ball)

        if (x1 < x2_other and x2 > x1_other and y1 < y2_other and y2 > y1_other):
            # Om kollision ändra riktning
            self.x_speed *= -1
            self.y_speed *= -1
            other_ball.x_speed *= -1
            other_ball.y_speed *= -1
