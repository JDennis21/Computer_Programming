#!/usr/bin/env python3

def mins_conversion(nums):
    secs = nums % 60
    mins = nums // 60
    return f'{int(mins)} minute{"s" if mins != 1 else ""} and {int(secs)} second{"s" if secs != 1 else ""}'


if __name__ == '__main__':

    runnerlist = []
    time = 0

    print('Park Run Timer\n~~~~~~~~~~~~~~\n')

    while True:
        runner = input('>')
        try:
            if '::' in runner:
                seconds = int(runner.split('::', 1)[1])
                runnerlist.append((int(runner.split('::')[0]), seconds,))
                time += seconds
            elif runner.lower() == 'end':
                if len(runnerlist) == 0:
                    print('Nothing to do.')
                    break
                else:
                    avg = mins_conversion(time / len(runnerlist))
                    fastest_runner = min(runnerlist, key=lambda slow: slow[1])
                    slowest_runner = max(runnerlist, key=lambda fast: fast[1])
                    print(f'\nTotal Runners: {len(runnerlist)}\nAverage Time: {avg}\n'
                          f'Fastest Time: {mins_conversion(fastest_runner[1])}\n'
                          f'Slowest Time: {mins_conversion(slowest_runner[1])}\n\nBest Runner #{fastest_runner[0]}')
                    break
            else:
                print('Ignoring invalid input.')
        except ValueError:
            print('Ignoring invalid input.')
