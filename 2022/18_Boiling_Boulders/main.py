#
# https://adventofcode.com/2022/day/18
#

from collections import defaultdict

m = defaultdict(set)
def sides(i, j, k, SIDES = 6, cnt = 0):
    cnt += sum(1 for u, v in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)] if (u, v) in m[k])
    cnt += (i, j) in m[k - 1] if k - 1 in m else 0
    cnt += (i, j) in m[k + 1] if k + 1 in m else 0
    return SIDES - cnt

with open('input.txt') as input:
    for line in input:
        i, j, k = [int(x) for x in line.strip().split(',')]
        m[k].add((i, j))

t = 0
for k in m.keys():
    for i, j in m[k]:
        t += sides(i, j, k)
print(f'part 1: {t}')
# part 1: 3500