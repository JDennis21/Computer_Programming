#!/usr/bin/env python3

from sys import argv
from pickle import load


def shift_string(input_str, offset):
    from string import ascii_uppercase as alpha
    shifted_alpha = alpha[offset:] + alpha[:offset]
    output_string = ''
    for character in input_str:
        if character.isupper():
            output_string += shifted_alpha[alpha.find(character)]
        elif character.islower():
            output_string += shifted_alpha.lower()[alpha.lower().find(character)]
        else:
            output_string += character
    return ''.join(output_string)


if __name__ == '__main__':
    try:
        with open('eng_dict.pickle', 'rb') as f:
            eng_dict = load(f)

        with open(argv[1]) as encrypted:
            original_str = ''
            no_spec_str = ''
            for line in encrypted:
                original_str += ''.join(line)
                no_spec_str += ''.join(char for char in line if char.isalpha() or char == ' ')

        for num in range(1, 26):
            shifted_str_list = shift_string(no_spec_str.lower(), num).split()
            correct_word = 0

            for word in shifted_str_list[:]:
                if len(word) <= 1:
                    shifted_str_list.remove(word)
                elif word in eng_dict[word[:2]] and num > 0:
                    correct_word += 1

            if correct_word / len(shifted_str_list) >= 0.70:
                print(f'\n{shift_string(original_str, num)}')
                break
            elif num == 25 and correct_word / len(shifted_str_list) < 0.70:
                print('Cannot decrypt. Most likely not a caesar cipher at work here.')
                break

    except FileNotFoundError:
        print(f'Cannot open "{argv[1]}". Sorry about that.')
    except IndexError:
        print('Error: Argument is missing.')
