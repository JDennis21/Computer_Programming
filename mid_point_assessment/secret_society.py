#!/usr/bin/env python3

if __name__ == '__main__':
    while True:
        password = input('Greetings! What is the password? ').lower()
        if password == 'parrot':
            print('Correct! you may enter.')
            break
        else:
            print('Incorrect! You may try again')
