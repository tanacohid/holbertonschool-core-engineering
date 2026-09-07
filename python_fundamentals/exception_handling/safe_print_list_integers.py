#!/usr/bin/env python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError, NameError):
        return False
