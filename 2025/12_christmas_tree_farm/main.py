#
# https://adventofcode.com/2025/day/12
#

from collections import defaultdict

cnt = defaultdict(int)
puzzles = []
with open('input.txt') as input:
    text = input.read()
    chunks = text.split('\n\n')
    for chunk in chunks:
        lines = chunk.splitlines()
        if lines[0].endswith(':'):  # shape
            id = int(lines[0][:-1])
            cnt[id] = sum(int(c == '#') for line in lines for c in line)  # shape id '#' count
        else:  # puzzles
            for line in lines:
                dims, ids = line.split(':')  # dimensions MxN and list of shape ids
                M, N = map(int, dims.split('x'))
                ids = list(map(int, ids.split()))
                puzzles.append((M, N, ids))

part1 = 0
ratio = 1.2  # suboptimal packing overhead per count of '#' in each shape, ie. ratio == 1.0 if we can perfectly pack
for puzzle in puzzles:
    M, N, ids = puzzle
    have = M * N
    need = ratio * sum(cnt[id] * quantity for id, quantity in enumerate(ids))
    part1 += int(need <= have)  # do we have what we need?
print(f'part 1: {part1}')
# part 1: 406
