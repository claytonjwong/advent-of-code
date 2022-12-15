#
# https://adventofcode.com/2022/day/15
#

from collections import deque

sensors, beacons, seen = set(), set(), set()
def bfs(i, j, dist, T = int(2e6)):
    take = abs(T - i)
    if dist < take:
        return
    for k in range(take, dist + 1):
        for u, v in [(T, j + k - take), (T, j - k + take)]:
            if (u, v) not in beacons:
                seen.add((u, v))

with open('input.txt') as input:
    for k, line in enumerate(input):
        A = line.strip().split(' ')
        S = f'{A[2]}{A[3][:-1]}'
        B = f'{A[8]}{A[9]}'
        j, i = [int(word.split('=')[1]) for word in S.split(',')]; sensors.add((i, j))
        v, u = [int(word.split('=')[1]) for word in B.split(',')]; beacons.add((u, v))
        dist = abs(i - u) + abs(j - v)
        bfs(i, j, dist)
print(f'part 1: {len(seen)}')
# part 1: 5166077