#!/usr/bin/env python3

from random import choice
from sys import argv


def nums_choice():
    from string import digits
    new_nums = ''
    for i in range(4):
        new_nums += choice(digits)
    return new_nums


def student_id(input_data):
    return input_data[0:8]


def initials(input_data):
    initial = ''
    first_names = input_data[8::].split(',', 1)[1]
    for character in first_names:
        if character.isupper():
            initial += f'{character}.'
    return initial.lower()


def surname(input_data):
    return input_data[9::].split(',', 1)[0].lower()


if __name__ == '__main__':
    try:
        with open(argv[1]) as student_data:
            contents = []
            for line in student_data:
                contents.append(line.strip())
            student_data.close()

        for data in contents:
            with open('student_data_output.txt', 'a') as output:
                output.write(f'{student_id(data)} {initials(data)}{surname(data)}{nums_choice()}@poppleton.ac.uk\n')

    except FileNotFoundError:
        print('Error: File does not exist.')
    except IndexError:
        print('Error: Argument is missing.')
