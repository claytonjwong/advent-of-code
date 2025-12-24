#
# https://adventofcode.com/2025/day/11
#
from collections import defaultdict
from functools import cache

E = defaultdict(set)  # edges
with open('input.txt') as input:
    for s in input:
        beg, ends = s.strip().split(':')
        for end in ends.split(' '):
            E[beg].add(end)

@cache
def go(u, target):
    return 1 if u == target else sum(go(v, target) for v in E[u])

part1 = go('you', 'out')
print(f'part 1: {part1}')

part2 = go('svr', 'fft') \
      * go('fft', 'dac') \
      * go('dac', 'out')
print(f'part 2: {part2}')

# part 1: 466
# part 2: 549705036748518
