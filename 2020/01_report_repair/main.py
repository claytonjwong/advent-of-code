#
# https://adventofcode.com/2020/day/1
#

A = []
with open('./input.txt') as input:
    A = [int(line.strip()) for line in input]

def sum2(exclude = -1, t = 2020, seen = set()):
    for i, x in enumerate(A):
        if i == exclude:
            continue
        y = t - x
        if y in seen:
            return x * y
        seen.add(x)
    return -1

def sum3(t = 2020):
    for i, x in enumerate(A):
        y = t - x
        z = sum2(i, y)
        if z != -1:
            return x * z
    return -1

print(f'Part 1: {sum2()}')
print(f'Part 2: {sum3()}')
