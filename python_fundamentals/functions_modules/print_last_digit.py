#!/usr/bin/env python3

def print_last_digit(number):
	if number > 0:
		print(number %1) 
	else:
		print(-number %1)
	return True