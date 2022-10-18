#!/usr/bin/env python3

def findmin(a, b):
    """finds the smaller of two numbers and returns it"""
    return f'{a} is smaller than {b}' if int(a) < int(b) else f'{b} is smaller than {a}'


print(findmin(input('enter a number: '), input('enter another: ')))
