#!/usr/bin/env python 3

if __name__ == '__main__':
    import random

    LIST_OF_WORDS = ['dog', 'ham', 'cat', 'knight', 'mighty', 'beast', 'bat', 'cheese', 'knuckles', 'mouse', 'black',
                     'white', 'red', 'purple', 'green', 'big', 'small', 'massive', 'tiny', 'round', 'square', 'minus',
                     'plus', 'course']

    print('Password Generator\n===================')
    num_students = input('How many passwords are required?\n')
    print('===================')

    count = 1

    while True:
        try:
            if 1 > int(num_students) or int(num_students) > 24:
                num_students = input('Please enter a number between 1 and 24.\n==================\n')
            else:
                password = random.choice(LIST_OF_WORDS) + random.choice(LIST_OF_WORDS) + random.choice(LIST_OF_WORDS)
                print(f'{count}-->{password}')
                count += 1
                if count - 1 == int(num_students):
                    break
        except ValueError:
            num_students = input('Error: Please enter an integer.\n')
