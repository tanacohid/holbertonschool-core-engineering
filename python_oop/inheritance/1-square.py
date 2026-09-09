#!/usr/bin/env python3
"""Defines the Rectangle class."""


Rectangle = __import__("2-rectangle").Rectangle


class Square(Rectangle):
    """Represents a Square."""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return the area of the Square."""
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
