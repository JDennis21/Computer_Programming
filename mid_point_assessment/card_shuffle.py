#!/usr/bin/env python3

from random import shuffle

if __name__ == '__main__':

    cards = ['8S', '6S', 'TD', 'KC', 'TC', 'AH', '3H', 'AS', 'JS', '5C', '2D', '4D', 'AC', 'TH', 'KH', '2S', '8C', '6H',
             '6C', '8D', '2C', 'JH', '4H', 'KD', '3S', 'AD', '2H', '7D', '5D', '9D', '4S', '5H', 'TS', 'JC', '7C', 'QH',
             '3D', 'QC', '7H', '5S', 'QD', '9S', '3C', '9C', 'QS', '4C', '9H', '8H', '6D', 'KS', 'JD', '7S']

    shuffle(cards)
    north = cards[0:13]
    south = cards[13:26]
    east = cards[26:39]
    west = cards[39:52]

    print('Creating pack of cards ...\nShuffling and Dealing  ...\n')
    print(f'North --> {", ".join(north)}\nSouth --> {", ".join(south)}\nEast  --> {", ".join(east)}\n'
          f'West  --> {", ".join(west)}')

    print('\nLooking for the Ace of Spades...')

    if 'AS' in north:
        print('North player has it!')

    elif 'AS' in south:
        print('South player has it!')

    elif 'AS' in east:
        print('East player has it!')

    elif 'AS' in west:
        print('West player has it!')
