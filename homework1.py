class Figure:
    unit = "cm"


class Square(Figure):
    def __init__(self, side_length):
        self.side_length = side_length

    def info(self):
        print(f"Square side length: {self.side_length}{self.unit}, area: {self.side_length ** 2}{self.unit}²")


class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def info(self):
        print(f"Rectangle length: {self.length}{self.unit}, width: {self.width}{self.unit}, area: {self.length * self.width}{self.unit}²")


shapes = [
    Square(5),
    Square(10),
    Rectangle(5, 8),
    Rectangle(3, 6),
    Rectangle(7, 2)
]

for shape in shapes:
    shape.info()