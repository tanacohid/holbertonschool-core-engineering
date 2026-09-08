#!/usr/bin/env python3
"""Defines a square."""


class Square:
    """Represents a square."""
    def __init__(self, size:int):
        self.__size = size

try:
    carree = Square(int)
except TypeError:
    print("size must be an integer")
except ValueError:
    print("size must be >= 0")
