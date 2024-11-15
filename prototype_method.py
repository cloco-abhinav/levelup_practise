import copy

class Shape:
    def clone(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Circle with radius: {self.radius}"

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Square with side length: {self.side_length}"

def client_code():
    # Create a Circle and a Square
    circle1 = Circle(10)
    square1 = Square(5)

    print(f"Original {circle1}")
    print(f"Original {square1}")

    circle2 = circle1.clone()
    square2 = square1.clone()

    circle2.radius = 15
    square2.side_length = 7

    print("\nAfter cloning and modifying:")
    print(f"Cloned {circle2}")
    print(f"Cloned {square2}")

client_code()
