# AoC 2022
* [adventofcode.com/2022](https://adventofcode.com/2022)

## [Day 1: Calorie Counting](https://adventofcode.com/2022/day/1)
```python
A = []
with open('input.txt') as input:
    t = 0
    for line in input:
        line = line.strip()
        if len(line):
            t += int(line)
        else:
            A.append(t); t = 0
A.sort()
print(f'part 1: {A[-1]}')
print(f'part 2: {sum(A[-3:])}')
# part 1: 69883
# part 2: 207576
```

## [Day 2: Rock Paper Scissors](https://adventofcode.com/2022/day/2)
```python
cost = {
    'X': 1, 'lose': 0,
    'Y': 2, 'tie': 3,
    'Z': 3, 'win': 6,
}
m = {
    # lose
    'BX': cost['lose'] + cost['X'],
    'CY': cost['lose'] + cost['Y'],
    'AZ': cost['lose'] + cost['Z'],
    # tie
    'AX': cost['tie'] + cost['X'],
    'BY': cost['tie'] + cost['Y'],
    'CZ': cost['tie'] + cost['Z'],
    # win
    'CX': cost['win'] + cost['X'],
    'AY': cost['win'] + cost['Y'],
    'BZ': cost['win'] + cost['Z'],
}
lose = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
}
tie = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}
win = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
}

t1, t2 = 0, 0
with open('input.txt') as input:
    for line in input:
        play = ''.join(line.strip().split(' '))
        t1 += m[play]
        a, b = list(play)
        if b == 'X': t2 += cost['lose'] + cost[lose[a]]
        if b == 'Y': t2 += cost['tie'] + cost[tie[a]]
        if b == 'Z': t2 += cost['win'] + cost[win[a]]
print(f'part 1: {t1}')
print(f'part 2: {t2}')
# part 1: 12855
# part 2: 13726
```

## [Day 3: Rucksack Reorganization](https://adventofcode.com/2022/day/3)
```python
lower = lambda c: ord(c) - ord('a')
upper = lambda c: ord(c) - ord('A') + 26
cost = lambda c: 1 + (lower(c) if c.islower() else upper(c))

t1, t2 = 0, 0
with open('input.txt') as input:
    A = []
    for line in input:
        line = line.strip()
        n = len(line)
        a = set(list(line[:n // 2]))
        b = set(list(line[n // 2:]))
        same = a & b
        t1 += sum(cost(c) for c in same)
        A.append(a | b)
        if not (len(A) % 3):
            a, b, c = A; A = []
            same = a & b & c
            t2 += sum(cost(c) for c in same)
print(f'part 1: {t1}')
print(f'part 2: {t2}')
# part 1: 7674
# part 2: 2805
```

## [Day 4: Camp Cleanup](https://adventofcode.com/2022/day/4)
```python
t1, t2 = 0, 0
with open('input.txt') as input:
    for line in input:
        line = line.strip()
        A, B = line.split(',')
        i, j = [int(x) for x in A.split('-')]
        u, v = [int(x) for x in B.split('-')]
        t1 += (i <= u and v <= j) or (u <= i and j <= v)
        t2 += not (j <= u) and not (v <= i) # inversion: p is true if not p is impossible, ie. if i..j is not before inclusive-or not after u..v, then i..j and u..v must overlap
print(f'part 1: {t1}')
print(f'part 2: {t2}')
# part 1: 459
# part 2: 779
```

## [Day 5: Supply Stacks](https://adventofcode.com/2022/day/5)
```python
from collections import deque

def move(isStack):
    A = [
        [],                                       # 0
        ['N', 'B', 'D', 'T', 'V', 'G', 'Z', 'J'], # 1
        ['S', 'R', 'M', 'D', 'W', 'P', 'F'],      # 2
        ['V', 'C', 'R', 'S', 'Z'],                # 3
        ['R', 'T', 'J', 'Z', 'P', 'H', 'G'],      # 4
        ['T', 'C', 'J', 'N', 'D', 'Z', 'Q', 'F'], # 5
        ['N', 'V', 'P', 'W', 'G', 'S', 'F', 'M'], # 6
        ['G', 'C', 'V', 'B', 'P', 'Q'],           # 7
        ['Z', 'B', 'P', 'N'],                     # 8
        ['W', 'P', 'J'],                          # 9
    ]
    with open('input.txt') as input:
        for line in input:
            _, i, _, j, _, k = line.strip().split(' ')
            i, j, k = [int(x) for x in [i, j, k]]
            take = []
            for _ in range(i):
                take.append(A[j].pop())
            A[k].extend(take if isStack else take[::-1])
    return ''.join([row[-1] for row in A if len(row)])

print(f'part 1: {move(True)}')
print(f'part 2: {move(False)}')
# part 1: GFTNRBZPF
# part 2: VRQWPDSGP
```

## [Day 6: Tuning Trouble](https://adventofcode.com/2022/day/6)
```python
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
```