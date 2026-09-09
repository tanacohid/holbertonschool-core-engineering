#!/usr/bin/env python3
"""Defines the BaseGeometry class."""


class BaseGeometry:
    """Represents the base geometry."""

    def area(self):
        """Calculate the area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """Represents a rectangle."""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = height
