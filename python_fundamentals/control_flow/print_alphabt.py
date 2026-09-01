#!/usr/bin/env python3

i = 'a'
alpha = ''

while i <= 'z':
    if i != 'q' and i != 'e':
        alpha += i
    i = chr(ord(i) + 1)

print(alpha)
