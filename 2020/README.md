# AoC 2020
* [adventofcode.com/2020](https://adventofcode.com/2020)

## [Day 1: Report Repair](https://adventofcode.com/2020/day/1)

```python
A = []
with open('./input.txt') as input:
    A = [int(line.strip()) for line in input]

def sum2(exclude = -1, t = 2020, seen = set()):
    for i, x in enumerate(A):
        if i == exclude:
            continue
        y = t - x
        if y in seen:
            return x * y
        seen.add(x)
    return -1

def sum3(t = 2020):
    for i, x in enumerate(A):
        y = t - x
        z = sum2(i, y)
        if z != -1:
            return x * z
    return -1

print(f'Part 1: {sum2()}')  # Part 1: 1006875
print(f'Part 2: {sum3()}')  # Part 2: 165026160 
```

## [Day 2: Password Philosophy](https://adventofcode.com/2020/day/2)

```python
from collections import Counter

A = []
with open('./input.txt') as input:
    A = [line.strip() for line in input]

one = 0
two = 0
for range, ch, word in [line.split(' ') for line in A]:
    lo, hi = map(int, range.split('-'))
    ch = ch[0]  # ignore ':'
    m = Counter(word)
    if ch in m and lo <= m[ch] <= hi:
        one += 1
    if (lo <= len(word) and ch == word[lo - 1]) ^ (hi <= len(word) and ch == word[hi - 1]):
        two += 1
print(f'Part 1: {one}')  # Part 1: 460
print(f'Part 2: {two}')  # Part 2: 251
```

## [Day 3: Toboggan Trajectory](https://adventofcode.com/2020/day/3)

```python
A = []
with open('./input.txt') as input:
    A = [line.strip() for line in input]
M = len(A)
N = len(A[0])

def traverse(down = 1, right = 3):
    cnt = 0
    i = 0
    j = 0
    def step(i, j):
        for _ in range(right):
            j = j + 1 if j < N - 1 else 0
        return i + down, j
    while i < M:
        if A[i][j] == '#':
            cnt += 1
        i, j = step(i, j)
    return cnt

print(f'Part 1: {traverse()}')
print(f'Part 2: {traverse(1, 1) * traverse(1, 3) * traverse(1, 5) * traverse(1, 7) * traverse(2, 1)}')

# Part 1: 232
# Part 2: 3952291680
```
