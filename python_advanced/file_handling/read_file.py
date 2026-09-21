#!/usr/bin/env python3

def read_file(filename=""):

    with open("UTF8.txt", 'r', encoding="utf-8") as f:
        data = f.read()
    print(data)
