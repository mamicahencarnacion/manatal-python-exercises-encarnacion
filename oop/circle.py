from math import pi

from shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius)
        if radius < 0:
            raise ValueError("Radius should not be negative.")

        self._radius = radius

    def get_area(self):
        return pi * self._radius**2

    def get_perimeter(self):
        return 2 * pi * self._radius
