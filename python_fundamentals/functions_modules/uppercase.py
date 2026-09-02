#!/usr/bin/env python3

def uppercase(str):
    j = ''
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            j += chr(ord(i) - 32)
        else:
            j += i
