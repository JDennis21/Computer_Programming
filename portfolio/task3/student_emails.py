#!/usr/bin/env python3

from string import digits
from random import choice
from sys import argv

if __name__ == '__main__':
    try:
        with open(argv[1]) as student_data:
            contents = [line.strip() for line in student_data]

        for data in contents:
            student_id = data[0:8]
            surname = data[9::].split(',', 1)[0]
            names = data[8::].split(',', 1)[1]
            initials = ''.join((f'{character}.' for character in data[8::].split(',')[1] if character.isupper()))
            rand_nums = ''.join(choice(digits) for length in range(4))

            with open('student_data_output.txt', 'a') as output:
                output.write(f'{student_id} {initials.lower()}{surname.lower()}{rand_nums}@poppleton.ac.uk\n')

    except FileNotFoundError:
        print('Error: File does not exist.')
    except IndexError:
        print('Error: Argument is missing.')
