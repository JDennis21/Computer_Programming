#!/usr/bin/env python3

from statistics import mean as avg, stdev

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']

if __name__ == '__main__':

    rainfall_month = []
    rainfall_amount = []

    for month in MONTHS:
        rainfall = input(f'Enter rainfall for {month}:  {" " * (9 - len(month))}')
        if not rainfall.isdigit():
            rainfall_nums = rainfall[:len(rainfall) - 2]
        else:
            rainfall_nums = rainfall
        rainfall_month.append([int(rainfall_nums), month])
        rainfall_amount.append(int(rainfall_nums))

    print(f'\nMax Rainfall:  {max(rainfall_month)[0]}mm in {max(rainfall_month)[1]}.')
    print(f'Min Rainfall:  {min(rainfall_month)[0]}mm in {min(rainfall_month)[1]}.')

    print(f'\nAverage:             {round(float(avg(rainfall_amount)), 2)}mm.')
    print(f'Standard Deviation:  {round(float(stdev(rainfall_amount)), 2)}mm.')
