from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, *args):
        print(args)
        self.length = args[0]
        self.breadth = args[1]

    def area(self):
        return self.length * self.breadth
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
rectangle = Rectangle(length, breadth)
circle = Circle(float(input("Enter the radius of the circle: ")))
print(f"The area of the rectangle is {rectangle.area()}")
print(f"The area of the circle is {circle.area()}")

