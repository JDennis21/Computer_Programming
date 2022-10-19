#!/usr/bin/env python3
# TODO allow it to open files through the command line
from random import choice

NUMS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if __name__ == '__main__':

    with open('student data input') as student_data:
        contents = []
        for line in student_data:
            contents.append(line.strip())
        student_data.close()

    for data in contents:
        student_id = data[0:8]
        surname = data[9::].split(',', 1)[0]
        names = data[8::].split(',', 1)[1]
        initials = ''
        rand_nums = str(choice(NUMS)) + str(choice(NUMS)) + str(choice(NUMS)) + str(choice(NUMS))
        for character in names:
            if character.isupper():
                initials += f'{character}.'
        try:
            output = open('student_data_output', 'x')
            output.write(f'{student_id} {initials.lower()}{surname.lower()}{rand_nums}@poppleton.ac.uk\n')
        except FileExistsError:
            output = open('student_data_output', 'a')
            output.write(f'{student_id} {initials.lower()}{surname.lower()}{rand_nums}@poppleton.ac.uk\n')
        output.close()