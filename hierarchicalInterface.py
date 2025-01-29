#Parent class
class Shape:
    def area(self):
        pass

#child Class 1
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
#Child Class 2
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
    
obj = Square(5)
print(obj.area())
obj = Circle(5)
print(obj.area())