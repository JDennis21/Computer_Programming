#!/usr/bin/env python 3

if __name__ == '__main__':
    BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
    pass1 = input('Choose a password to secure your account\n*')
    while True:
        if 8 <= len(pass1) <= 12:
            pass2 = input('Verify password\n*')
            if pass1 in BAD_PASSWORDS and pass1 == pass2:
                pass1 = input('Insecure password try again\n*')
            elif pass1 == pass2:
                print('Password has been set.')
                break
            else:
                pass1 = input('Passwords do not match try again\n*')
        else:
            pass1 = input('Password must be between 8-12 characters\n*')