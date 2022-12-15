#!/usr/bin/env python3

from random import choice

LIST_OF_WORDS = ['dog', 'ham', 'cat', 'knight', 'mighty', 'beast', 'bat', 'cheese', 'knuckles', 'mouse', 'black',
                 'white', 'red', 'purple', 'green', 'big', 'small', 'massive', 'tiny', 'round', 'square', 'minus',
                 'plus', 'course', 'phone', 'home', 'feeling', 'happy', 'sad', 'safe', 'careless', 'unhappy']

if __name__ == '__main__':

    print('Password Generator\n==================\n')
    num_students = input('How many passwords are needed?: ')

    try:
        if 1 > int(num_students) or int(num_students) > 24:
            print('Please enter a number between 1 and 24.')
        else:
            print('')
            for count in range(int(num_students)):
                print(f'{count + 1:>3} --> {"".join(choice(LIST_OF_WORDS) for num in range(3))}')
    except ValueError:
        print('Please enter a number.\n')
