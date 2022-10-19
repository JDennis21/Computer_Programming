#!/usr/bin/env python3

def run_num_splitter(nums):
    """Splits runners position and time into separate strings, 'nums' must be formatted as follows '001::231'"""
    return [int(nums[0:3]), int(nums[5:8])]


def sec_to_mins(nums):
    secs = nums % 60
    mins = nums // 60
    return f'{int(mins)} minute{"s" if mins > 1 else ""} and {int(secs)} second{"s" if secs > 1 else ""}'


if __name__ == '__main__':

    runnerlist = []
    time = 0

    print('Park Run Timer\n~~~~~~~~~~~~~~\n')

    while True:
        runner = input('>')
        if len(runner) == 8 and runner[3:5] == '::':
            seconds = int(runner[5:8])
            runnerlist.append(run_num_splitter(runner))
            time += seconds
        elif runner == 'END' or runner == 'end':
            if len(runnerlist) == 0:
                print('Nothing to do.')
                break
            else:
                avg = sec_to_mins(time / len(runnerlist))
                min(runnerlist)
                print(f'\nTotal Runners: {len(runnerlist)}\nAverage Time: {avg}\nFastest Time: {runner}\n'
                      f'Slowest Time: {runner}\nBest Runner #{runner}')
            break
        else:
            print('Ignoring invalid input.')
