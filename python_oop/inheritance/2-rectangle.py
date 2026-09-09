#!/usr/bin/env python3
"""Defines the BaseGeometry class."""


BaseGeometry = __import__("base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle."""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

