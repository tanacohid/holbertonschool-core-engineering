#!/usr/bin/python3

if __name__ == "__main__":

    def add(a, b):
        print("{} + {} = {}".format(a, b, add(a, b)))

    def sub(a, b):
        print("{} - {} = {}".format(a, b, sub(a, b)))

    def mul(a, b):
        print("{} * {} = {}".format(a, b, mul(a, b)))

    def div(a, b):
        print("{} / {} = {}".format(a, b, div(a, b)))
