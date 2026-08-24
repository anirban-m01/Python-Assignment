import math

class Shape:
    def __init__(self, radius):
        self.radius = radius


class Circle(Shape):
    def cal_area(self):
        return math.pi * self.radius * self.radius


class Sphere(Shape):
    def cal_volume(self):
        return (4/3) * math.pi * self.radius ** 3



c = Circle(5)
print("Area of Circle =", c.cal_area())


s = Sphere(5)
print("Volume of Sphere =", s.cal_volume())