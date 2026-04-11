import math

class Cylinder:
    def __init__(self, height, radius):
        self.height = height
        self.radius = radius

    def volume(self):
        return math.pi * self.radius ** 2 * self.height

    def area_surface(self):
        return 2 * math.pi * self.radius * self.height + 2 * math.pi * self.radius ** 2

c = Cylinder(10, 10)
print(c.volume())
print(c.area_surface())