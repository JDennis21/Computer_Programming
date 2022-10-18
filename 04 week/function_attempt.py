#!/usr/bin/env python3

def print_header(msg):
    """Prints 'msg' prefixed by 5 asterisks"""
    print(f'*****{msg}')


name = input('What is your name?\n')

print_header(name)
