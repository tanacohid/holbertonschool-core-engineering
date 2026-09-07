#!/usr/bin/env python3

def raise_exception():
    x = 'a'
    try:
        x + 2
    except TypeError:
        print("Exception has been raised")
        return None
