#
# https://adventofcode.com/2022/day/6
#

from collections import deque

PACKET_LEN = 4
MESSAGE_LEN = 14

part1, part2 = 0, 0
with open('input.txt') as input:
    i, P, M = 0, deque([]), deque([])
    while c:= input.read(1):
        P.append(c); M.append(c); i += 1
        if not (len(P) % PACKET_LEN):
            if not part1 and len(P) == len(set(P)): part1 = i
            P.popleft()
        if not (len(M) % MESSAGE_LEN):
            if not part2 and len(M) == len(set(M)): part2 = i
            M.popleft()
print(f'part 1: {part1}')
print(f'part 2: {part2}')
# part 1: 1155
# part 2: 2789