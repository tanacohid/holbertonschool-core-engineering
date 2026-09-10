#!/usr/bin/env python3
"""Shapes, interfaces and duck typing."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract shape class."""

    @abstractmethod
    def area(self):
        """Calculate the area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter."""
        pass


class Circle(Shape):
    """Represents a circle."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the circle area."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate the circle perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Represents a rectangle."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calculate the rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the rectangle perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))


if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    shape_info(circle)
    shape_info(rectangle)

