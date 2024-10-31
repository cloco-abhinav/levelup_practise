from abc import ABC, abstractmethod

# Product Interface
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
        
    def calculate_area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, length: float):
        self.length = length
        
    def calculate_area(self):
        return self.length * self.length

# Factory Interface
class ShapeFactory(ABC):
    @abstractmethod
    def create_shape(self, *args):
        pass

class CircleFactory(ShapeFactory):
    def create_shape(self, radius: float) :
        return Circle(radius)

class SquareFactory(ShapeFactory):
    def create_shape(self, length: float) :
        return Square(length)


#  this will be clinet logic(client doenot know how class are created(and which))
def get_shape_factory(shape_type: str):
    if shape_type == "circle":
        return CircleFactory()
    elif shape_type == "square":
        return SquareFactory()
    else:
        raise ValueError(f"Unknown shape type: {shape_type}")

def calc_area(shape_type: str, *args):
    factory = get_shape_factory(shape_type)
    shape = factory.create_shape(*args)
    area = shape.calculate_area()
    print(f"The area of the {shape_type} is: {area}")

calc_area("circle", 5) 
calc_area("square", 4)  

# adv: more scalable(easy to add any master classes without touching client code)/// also light coupling