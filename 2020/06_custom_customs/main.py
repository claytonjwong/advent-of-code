#
# https://adventofcode.com/2020/day/6
#

A = []
with open('./input.txt') as input:
    A = [line.strip() for line in input]
A.append('')  # sentinel delimiter

m, cnt = {}, 0
one = 0
two = 0
for line in A:
    if not len(line):
        one += len(m)
        two += sum([1 for c in m if m[c] == cnt])
        m = {}; cnt = 0
    else:
        for c in line:
            m[c] = m[c] + 1 if c in m else 1
        cnt += 1

print(f'Part 1: {one}')  # Part 1: 6542
print(f'Part 2: {two}')  # Part 2: 3299
