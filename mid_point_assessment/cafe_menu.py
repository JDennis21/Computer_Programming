#!/usr/bin/env python3

if __name__ == '__main__':
    spam_amount = int(input('How many slices of spam?\n'))
    print(f'Egg with spam{", spam" * (spam_amount - 2)} {"and spam " if spam_amount > 1 else ""}coming up!')
