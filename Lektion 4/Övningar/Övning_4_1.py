class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def perimeter(self):
        return 4 * self.side_length

square = Square(5)
print("Area:", square.area())
print("Perimeter:", square.perimeter())
