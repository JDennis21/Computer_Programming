#!/usr/bin/env python3

from sys import argv
from enchant import Dict


def shift_string(input_str, offset):
    output_string = ''
    for character in input_str:
        if character.isupper():
            from string import ascii_uppercase as alpha
            shifted_alpha = alpha[offset:] + alpha[:offset]
            output_string += shifted_alpha[alpha.find(character)]
        elif character.islower():
            from string import ascii_lowercase as alpha
            shifted_alpha = alpha[offset:] + alpha[:offset]
            output_string += shifted_alpha[alpha.find(character)]
        else:
            output_string += character
    return ''.join(output_string)


eng_dict = Dict('en_GB')

if __name__ == '__main__':
    try:
        with open(argv[1]) as encrypted:
            encrypted_str = ''
            for line in encrypted:
                encrypted_str += ''.join(line)

        cipher = False

        for num in range(26):
            shifted_str_list = shift_string(encrypted_str, num).split()
            correct_word = 0
            for word in shifted_str_list:
                if eng_dict.check(word) and num > 0:
                    correct_word += 1
                    if correct_word / len(shifted_str_list) >= 0.85:
                        print(f'\n{shift_string(encrypted_str, num)}')
                        cipher = True
                        break
            if num == 25 and cipher is False:
                print('Cannot decrypt. Most likely not a caesar cipher at work here.')
                break

    except FileNotFoundError:
        print('Error: File does not exist.')
    except IndexError:
        print('Error: Argument is missing.')
