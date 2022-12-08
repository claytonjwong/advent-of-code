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

## [Day 7: No Space Left On Device](https://adventofcode.com/2022/day/7)
```python3
from bisect import bisect_left

class Node:
    def __init__(self, parent = None):
        self.size = 0
        self.kids = {}
        self.parent = parent

root = Node()
node = root
with open('input.txt') as input:
    for line in input:
        A = line.strip().split(' ')
        if A[1] == 'cd':
            f = A[2]
            if f == '/': node = root
            elif f == '..': node = node.parent
            else:
                if f not in node.kids:
                    node.kids[f] = Node(node)
                node = node.kids[f]
        elif A[0].isdigit():
            node.size += int(A[0])

class Accumulator:
    def __init__(self):
        self.part1 = 0
        self.A = []
        self.go()
        self.part2 = self.delete()
    def go(self, node = root):
        for kid in node.kids.values():
            node.size += self.go(kid)
        if node.size <= 1e5:
            self.part1 += node.size  # part 1: accumulate total of all folders of size <= 1e5
        self.A.append(node.size)     # part 2: append candidate node size to array
        return node.size
    def delete(self):
        self.A.sort()
        space = 7e7 - self.A[-1]
        target = 3e7 - space
        i = bisect_left(self.A, target)
        return self.A[i]

acc = Accumulator()
print(f'part 1: {acc.part1}')
print(f'part 2: {acc.part2}')
# part 1: 1391690
# part 2: 5469168
```

## [Day 8: Treetop Tree House](https://adventofcode.com/2022/day/8)
```python
A = []
with open('input.txt') as input:
    for line in input:
        A.append([int(x) for x in line.strip()])
M, N = len(A), len(A[0])

# part 1
seen, key = set(), lambda i, j: f'{i},{j}'
for i in range(M):
    l, r = -1, -1 # left/right
    for j in range(N):
        k = N - 1 - j
        if l < A[i][j]: l = A[i][j]; seen.add(key(i, j))
        if r < A[i][k]: r = A[i][k]; seen.add(key(i, k))
for j in range(N):
    u, d = -1, -1 # up/down
    for i in range(M):
        k = M - 1 - i
        if u < A[i][j]: u = A[i][j]; seen.add(key(i, j))
        if d < A[k][j]: d = A[k][j]; seen.add(key(k, j))

# part 2
best = 0
for i in range(1, M - 1):
    for j in range(1, N - 1):
        l, k = 0, j - 1 # left
        while 0 <= k:
            l += 1
            if A[i][j] <= A[i][k]: break
            k -= 1
        r, k = 0, j + 1 # right
        while k < N:
            r += 1
            if A[i][j] <= A[i][k]: break
            k += 1
        u, k = 0, i - 1 # up
        while 0 <= k:
            u += 1
            if A[i][j] <= A[k][j]: break
            k -= 1
        d, k = 0, i + 1 # down
        while k < M:
            d += 1
            if A[i][j] <= A[k][j]: break
            k += 1
        cand = l * r * u * d
        best = max(best, cand)

print(f'part 1: {len(seen)}')
print(f'part 2: {best}')
# part 1: 1681
# part 2: 201684
```