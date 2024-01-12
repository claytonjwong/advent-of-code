#
# https://adventofcode.com/2023/day/1
#

t1 = 0
t2 = 0
with open('input.txt') as input:
    m1 = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    m2 = m1 | {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    f = lambda m: [m[s[i:i + k]] for i in range(len(s)) for k in range(1, len(s) + 1 - i) if s[i:i + k] in m]
    for s in input:
        d1 = f(m1); t1 += int(f'{d1[0]}{d1[-1]}')
        d2 = f(m2); t2 += int(f'{d2[0]}{d2[-1]}')
print(f'part 1: {t1}')
print(f'part 2: {t2}')
# part 1: 55017
# part 2: 53539
