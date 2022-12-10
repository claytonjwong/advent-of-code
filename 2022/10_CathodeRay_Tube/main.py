#
# https://adventofcode.com/2022/day/10
#

from collections import defaultdict

A = [0]
m = defaultdict(int)
lines = []
with open('input.txt') as input:
    for line in input:
        words = line.strip().split(' ')
        A.append(0 if len(words) == 1 else int(words[1]))

k = 0
for x in A:
    k += 1 if not x else 2
    m[k] = x

x, take, have = 1, set([20, 60, 100, 140, 180, 220]), []
for i in range(k + 1):
    x += m[i]
    if i in take:
        have.append(i * x)
print(f'part 1: {sum(have)}')
