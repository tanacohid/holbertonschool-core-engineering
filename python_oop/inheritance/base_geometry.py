#!/usr/bin/env python3

class BaseGeometry:

def area(self):
    raise Exception("area() is not implemented")

def integer_validator(self, name, value)
    if type(value) is not int:
        raise ValueError("<name> must be an integer")
    if value <= 0:
        raise ValueError("<name> must be greater than 0")
