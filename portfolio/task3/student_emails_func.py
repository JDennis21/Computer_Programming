#!/usr/bin/env python3

from random import choice
from sys import argv


def nums_choice():
    from string import digits
    return ''.join(choice(digits) for length in range(4))


def student_id(input_data):
    return input_data[0:8]


def initials(input_data):
    return ''.join((f'{character.lower()}.' for character in input_data[8::].split(',')[1] if character.isupper()))


def surname(input_data):
    return input_data[9::].split(',')[0].lower()


def email_generator(data):
    return f'{student_id(data)} {initials(data)}{surname(data)}{nums_choice()}@poppleton.ac.uk\n'


if __name__ == '__main__':
    try:
        with open(argv[1]) as student_data:
            user_info = [line.strip() for line in student_data]

        with open('student_data_output.txt', 'a') as output:
            [output.write(email_generator(info)) for info in user_info]

    except FileNotFoundError:
        print('Error: File does not exist.')
    except IndexError:
        print('Error: Argument is missing.')
