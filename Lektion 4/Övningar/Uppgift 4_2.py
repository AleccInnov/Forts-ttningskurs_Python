class Shape:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        print(f"This shape is {self.color}.")

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def display_radius(self):
        print(f"The radius of this circle is {self.radius}.")

circle = Circle("Red", 5)
circle.display_color()
circle.display_radius()
