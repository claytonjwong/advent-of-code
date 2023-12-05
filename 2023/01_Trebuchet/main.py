#
# https://adventofcode.com/2023/day/1
#

t1 = 0
t2 = 0
with open('input.txt') as input:
    m = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for s in input:
        digits = [c for c in s if c.isdigit()]
        t1 += int(f'{digits[0]}{digits[-1]}')
        digits = []
        for i in range(len(s)):
            for k in range(1, len(s) + 1 - i):
                it = s[i:i + k]
                if it in m:
                    digits.append(m[it])
        t2 += int(f'{digits[0]}{digits[-1]}')
print(f'part 1: {t1}')
print(f'part 2: {t2}')
# part 1: 55017
# part 2: 53539
