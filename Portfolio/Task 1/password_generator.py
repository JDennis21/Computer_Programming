#!/usr/bin/env python3

from random import choice

if __name__ == '__main__':

    LIST_OF_WORDS = ['dog', 'ham', 'cat', 'knight', 'mighty', 'beast', 'bat', 'cheese', 'knuckles', 'mouse', 'black',
                     'white', 'red', 'purple', 'green', 'big', 'small', 'massive', 'tiny', 'round', 'square', 'minus',
                     'plus', 'course', 'phone', 'home', 'feeling', 'happy', 'sad', 'safe', 'careless', 'unhappy']

    print('Password Generator\n==================')
    num_students = input('How many passwords are required?\n')

    while True:
        try:
            if 1 > int(num_students) or int(num_students) > 24:
                num_students = input('Please enter a number between 1 and 24.\n')
            else:
                for count in range(int(num_students)):
                    password = choice(LIST_OF_WORDS) + choice(LIST_OF_WORDS) + choice(LIST_OF_WORDS)
                    print(f'{count + 1}-->{password}')
                break
        except ValueError:
            num_students = input('Error: Please enter an integer.\n')
