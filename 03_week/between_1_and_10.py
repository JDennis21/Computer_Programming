#!/usr/bin/env python 3

if __name__ == '__main__':
    num = input('Enter a number between 1 and 10\n')

    while True:
        try:
            if 1 <= int(num) <= 10:
                print(num, 'is between 1 and 10')
                break
            else:
                print(num, 'is not between 1 and 10')
                break
        except ValueError:
            num = input('Please enter an integer\n')
