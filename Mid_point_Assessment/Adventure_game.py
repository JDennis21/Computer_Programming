#!/usr/bin/env python3

if __name__ == '__main__':
    name = input('Greetings! How shall we call you? ')
    if name[0:4].lower() in ['lord', 'lady']:
        print(f'It shall be so, {name}!')
    else:
        print('You may not be known by that name!')
