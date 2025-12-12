#
# https://adventofcode.com/2025/day/11
#

from collections import defaultdict, deque

E = defaultdict(set)  # edges
with open('example.txt') as input:
    for s in input:
        beg, ends = s.strip().split(':')
        for end in ends.split(' '):
            E[beg].add(end)

S = 'you'  # start
T = 'out'  # target
def go(u = S):
    return 1 if u == T else sum(go(v) for v in E[u])
print(f'part 1: {go()}')

# part 1: 466
