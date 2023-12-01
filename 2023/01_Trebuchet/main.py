#
# https://adventofcode.com/2023/day/1
#


#
# part 1
#

def f(s, reverse = False):
    n = len(s)
    for i in reversed(range(n)) if reverse else range(n):
        if s[i].isdigit():
            return int(s[i])
    return -1

t = 0
with open('input.txt') as input:
    for s in input:
        beg, end = f(s), f(s, True)
        t += int(f'{beg}{end}')
print(f'part 1: {t}')


#
# part 2
#

def f(s, reverse = False):
    m = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    n = len(s)
    for i in reversed(range(n)) if reverse else range(n):
        if s[i].isdigit():
            return int(s[i])
        for k in m.keys():
            if i + len(k) <= n and s[i:i+len(k)] == k:
                return m[k]
    return -1

t = 0
with open('input.txt') as input:
    for s in input:
        beg, end = f(s), f(s, True)
        t += int(f'{beg}{end}')
print(f'part 2: {t}')
# part 1: 55017
# part 2: 53539
