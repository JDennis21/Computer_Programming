#!/usr/bin/env python3

from sys import argv


def shift_string(input_str, offset):
    shifted_str = ''
    for character in input_str:
        shifted_num = ord(character) + offset
        if character.islower() and shifted_num <= 122:
            shifted_str += chr(shifted_num)
        elif character.islower() and 122 <= shifted_num:
            reset = (shifted_num - 26) - 97
            shifted_str += chr(97 + reset)
        elif character.isupper() and shifted_num <= 90:
            shifted_str += chr(shifted_num)
        elif character.isupper() and 90 <= shifted_num:
            reset = (shifted_num - 26) - 65
            shifted_str += chr(65 + reset)
        else:
            shifted_str += character
    return ''.join(shifted_str)


COMMON_WORDS = ['that', 'have', 'with', 'this', 'from', 'they', 'there', 'would', 'their', 'what', 'about', 'your',
                "won't", "can't", 'make', 'which', 'when', 'some', 'take', 'could', 'look', 'want', 'because', 'you',
                'are', 'why', 'not', 'here', 'likely', 'does']

if __name__ == '__main__':
    try:
        argument = argv[1]
        with open(argument) as encrypted:
            encrypted_str = ''
            for line in encrypted:
                encrypted_str += ''.join(line)
        cipher = False
        for num in range(26):
            correct_word = 0
            for word in COMMON_WORDS:
                if word in shift_string(encrypted_str.lower(), num) and num > 0:
                    correct_word += 1
                    if correct_word == 3:
                        print(f'\n{shift_string(encrypted_str, num)}')
                        cipher = True
                        print(num)
                        break
            if num == 25 and cipher is False:
                print('Cannot decrypt. Most likely not a caesar cipher at work here.')
                break
    except FileNotFoundError:
        print('Error: File does not exist.')
    except IndexError:
        print('Error: Argument is missing.')
