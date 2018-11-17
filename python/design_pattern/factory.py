"""
This shows create class from string, using **eval()** fucntion
"""

class Shape(object):
    def draw(self):
        return "abstract shape"

class Circle(Shape):
    def draw(self):
        return "circle"

class Rectangle(Shape):
    def draw(self):
        return "rectangle"


def factory(shape):
    return eval(shape + "()")


shape = factory("Circle")
print(shape.draw())

shape = factory("Rectangle")
print(shape.draw())
