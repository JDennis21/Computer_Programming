#!/usr/bin/env python 3

if __name__ == '__main__':
    x = int(input('Insert an integer.\n'))
    y = int(input('Insert another integer.\n'))
    if x == 0 or y == 0:
        print('Division of or by zero is not possible.')
    else:
        print('The result of', x, 'divided by', y, 'equals', x / y)
