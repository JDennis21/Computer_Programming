#!/usr/bin/env python3

def mins_conversion(nums):
    secs = nums % 60
    mins = nums // 60
    return f'{int(mins)} minute{"s" if mins != 1 else ""}, {int(secs)} second{"s" if secs != 1 else ""}'


def avg(num, amount):
    return mins_conversion(num / len(amount))


def fast_runner(run_list):
    return min(run_list, key=lambda fast: fast[1])[0], mins_conversion(min(run_list, key=lambda fast: fast[1])[1])


def slow_runner(run_list):
    return mins_conversion(max(run_list, key=lambda slow: slow[1])[1])


def final_output():
    return f'\nTotal Runners: {len(runnerlist)}\nAverage Time:  {avg(time, runnerlist):}\n' \
           f'Fastest Time:  {fast_runner(runnerlist)[1]:}\nSlowest Time:  {slow_runner(runnerlist):}\n\n' \
           f'Best Time Here: Runner #{fast_runner(runnerlist)[0]}'


if __name__ == '__main__':

    runnerlist = []
    time = 0

    print("Park Run Timer\n~~~~~~~~~~~~~~\n\nLet's go!\n")

    while True:
        runner = input('>')
        try:
            if '::' in runner:
                time += int(runner.split('::', 1)[1])
                runnerlist.append((int(runner.split('::')[0]), int(runner.split('::')[1]),))
            elif runner.lower() == 'end':
                if len(runnerlist) == 0:
                    print('Nothing to do.')
                    break
                else:
                    print(final_output())
                    break
            else:
                print('Error in data stream. Ignoring. carry on.')
        except ValueError:
            print('Error in data stream. Ignoring. carry on.')
