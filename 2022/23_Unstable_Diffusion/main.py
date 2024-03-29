#
# https://adventofcode.com/2022/day/23
#

from collections import defaultdict

have = set()
with open('input.txt') as input:
    [[have.add((i, j)) for j, c in enumerate(line.strip()) if c == '#'] for i, line in enumerate(input)]

def empty_spaces():
    i, u = min(i for i, _ in have), max(i for i, _ in have)
    j, v = min(j for _, j in have), max(j for _, j in have)
    return len([(x, y) for y in range(j, v + 1) for x in range(i, u + 1) if (x, y) not in have])

part1, part2 = 0, 0
d, dirs, round = 0, ['N', 'S', 'W', 'E'], 1
while True:
    move, same = defaultdict(set), set()
    for i, j in have:
        if not any(not (i == u and j == v) and (u, v) in have for v in [j - 1, j, j + 1] for u in [i - 1, i, i + 1]):
            same.add((i, j)) # none adjacent
            continue
        u, v = i, j
        for offset in range(len(dirs)):
            x = (d + offset) % len(dirs)
            if dirs[x] == 'N' and not len(set([(i - 1, j - 1), (i - 1, j), (i - 1, j + 1)]).intersection(have)): u = i - 1; break
            if dirs[x] == 'S' and not len(set([(i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]).intersection(have)): u = i + 1; break
            if dirs[x] == 'W' and not len(set([(i - 1, j - 1), (i, j - 1), (i + 1, j - 1)]).intersection(have)): v = j - 1; break
            if dirs[x] == 'E' and not len(set([(i - 1, j + 1), (i, j + 1), (i + 1, j + 1)]).intersection(have)): v = j + 1; break
        if u == i and v == j:
            same.add((i, j)) # cannot move
            continue
        move[(u, v)].add((i, j))
    have = same.copy()
    for next, prev in move.items():
        if len(prev) == 1:
            have.add(next)
        else:
            have |= prev
    if round == 10:
        part1 = empty_spaces()
    if not len(move):
        part2 = round
        break
    d, round = (d + 1) % len(dirs), round + 1

print(f'part 1: {part1}')
print(f'part 2: {part2}')
# part 1: 3788
# part 2: 921