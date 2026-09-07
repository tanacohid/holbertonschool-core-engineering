#!/usr/bin/env python3

def raise_exception():
    x = 'a'
    try:
        x + 2
    except TypeError:
        return None
